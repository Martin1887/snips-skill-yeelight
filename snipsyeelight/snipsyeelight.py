# -*-: coding utf-8 -*-
""" Yeelight skill for Snips. """

import json
import time
import os
import errno
import sys
import socket

from yeelightbulb import YeelightBulb
from color_utils import COLORS


class SnipsYeelight:
    """ Yeelight skill for Snips. """

    def __init__(self):
        """ Initialisation. """
        self.MCAST_GRP = '239.255.255.250'
        self.MCAST_PORT = 1982
        self.MULTICAST_TTL = 2

        sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP,
                        socket.IP_MULTICAST_TTL, self.MULTICAST_TTL)
        sock.settimeout(10)

        self.id = 0
        self.SEARCH_MSG = 'M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1982\r\nMAN: "ssdp:discover"\r\nST: wifi_bulb'

        sock.sendto(self.SEARCH_MSG, (self.MCAST_GRP, self.MCAST_PORT))

        self.recv_lights(sock)

    def recv_lights(self, sock):
        """ Get the responses of all conected bulbs

        :param host: The sender host.
        :param port: The sender port.
        """
        self.bulbs = []

        while True:
            try:
                # 10240 is the buffer size in bytes
                data = sock.recv(2048)
                ip = ''
                _power = False
                _bright = 0
                _rgb = 0
                name = ''
                for line in data.split('\n'):
                    clean = line.strip().lower()
                    if 'location' in clean:
                        ip_port = clean.replace(
                            'location: yeelight://', '').split(':')
                        ip = ip_port[0]
                        port = int(ip_port[1])
                    elif 'power' in clean:
                        if 'on' in clean:
                            _power = True
                        else:
                            _power = False
                    elif 'bright' in clean:
                        _bright = int(clean.split(':')[1].strip())
                    elif 'rgb' in clean:
                        _rgb = int(clean.split(':')[1].strip())
                    elif 'name' in clean:
                        name = clean.split(':')[1].strip()
                self.bulbs.append(YeelightBulb(ip, port, name))
            except socket.timeout:
                break

    def light_on_set(self, color=None, temperature=None, intensity=None, location=None):
        """ Turn on Yeelight lights in [location] at [intensity] with [color] color.

        :param color: The new color or None.
        :param temperature: The new temperature or None.
        :param intensity: The new intensity or None.
        :param: location: The location of the lights.
        """
        light_ids = self._get_light_ids_from_room(location)

        state = {
            'id': self.id,
            'method': 'set_power',
            'params': [
                'on',
                'smooth',
                500,
                2
            ]
        }
        self._post_state_to_ids(state, light_ids)

        if intensity is not None:
            intensity = int(intensity)
            state = {
                'id': self.id,
                'method': 'set_bright',
                'params': [
                    intensity,
                    'smooth',
                    500
                ]
            }
            self._post_state_to_ids(state, light_ids)
        if color is not None:
            color = COLORS.get(color, 0)
            state = {
                'id': self.id,
                'method': 'set_rgb',
                'params': [
                    color,
                    'smooth',
                    500
                ]
            }
            self._post_state_to_ids(state, light_ids)
        if temperature is not None:
            state = {
                'id': self.id,
                'method': 'set_ct_abx',
                'params': [
                    temperature,
                    'smooth',
                    500
                ]
            }
            self._post_state_to_ids(state, light_ids)

    def light_off(self, location):
        """ Turn off Yeelight lights in [location].

        :param: location: The location of the lights.
        """
        light_ids = self._get_light_ids_from_room(location)

        state = {
            'id': self.id,
            'method': 'set_power',
            'params': [
                'off',
                'smooth',
                500,
                2
            ]
        }
        self._post_state_to_ids(state, light_ids)

    def temperature_up(self, temp_augmentation, location):
        """ Increase Yeelight temperature by percentage.

        :param temp_augmentation: The percentage of temperature augmentation.
        :param: location: The location of the lights.
        """
        # Firstly, turn on the bulbs
        self.light_on_set()

        try:
            temp_augmentation = int(temp_augmentation)
        except (ValueError, TypeError):
            temp_augmentation = 10

        light_ids = self._get_light_ids_from_room(location)

        for light_id in light_ids:
            state = {
                'id': self.id,
                'method': 'adjust_ct',
                'params': [
                    temp_augmentation,
                    'smooth',
                    500
                ]
            }
            self._post_state(state, light_id)

    def temperature_down(self, temp_reduction, location):
        """ Decrease Yeelight temperature by percentage.

        :param temp_reduction: The percentage of temperature reduction.
        :param: location: The location of the lights."""
        try:
            temp_reduction = int(temp_reduction)
        except (ValueError, TypeError):
            temp_reduction = 10
        self.temperature_up(-temp_reduction, location)

    def light_up(self, intensity_augmentation, location):
        """ Increase Yeelight lights' intensity.

        :param intensity_augmentation: The percentage of bright augmentation.
        :param: location: The location of the lights.
        """
        # Firstly, turn on the bulbs
        self.light_on_set()

        try:
            intensity_augmentation = int(intensity_augmentation)
        except (ValueError, TypeError):
            intensity_augmentation = 10

        light_ids = self._get_light_ids_from_room(location)

        for light_id in light_ids:
            state = {
                'id': self.id,
                'method': 'get_prop',
                'params': [
                    'bright'
                ]
            }
            intensity = int(self._post_state(state, light_id)['result'][0])
            if intensity + intensity_augmentation > 100:
                intensity = 100
            elif intensity + intensity_augmentation < 0:
                intensity = 0
            else:
                intensity += intensity_augmentation

            state = {
                'id': self.id,
                'method': 'set_bright',
                'params': [
                    intensity,
                    'smooth',
                    500
                ]
            }
            self._post_state(state, light_id)

    def light_down(self, intensity_reduction, location):
        """ Lower Yeelight lights' intensity.

        :param intensity_reduction: The percentage of bright reduction.
        :param: location: The location of the lights.
        """
        try:
            intensity_reduction = int(intensity_reduction)
        except (ValueError, TypeError):
            intensity_reduction = 10
        self.light_up(-intensity_reduction, location)

    def _post_state_to_ids(self, params, light_ids):
        """ Post a state update to specyfied Yeelight lights.

        :param: params: Yeelight request parameters.
        :pram light_id: id:port of Yeelioght bulb.
        """
        try:
            for light_id in light_ids:
                self._post_state(params, light_id)
                time.sleep(0.2)
        except Exception:
            return

    def _post_state(self, params, light_id):
        """ Post a state update to a given light.

        :param params: Yeelight request parameters.
        :param light_id: id:port of Yeelight bulb.
        """
        if (light_id is None) or (params is None):
            return

        print("Setting state for light " + str(light_id) + ": " + str(params))
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(light_id)
            sock.sendall(b'{}\r\n'.format(json.dumps(params)))
            data = sock.recv(1024)
            sock.close()
            data = json.loads(data.strip())
        except:
            print("Request timeout. Is the Yeelight Bridge reachable?")
            pass

        self.id += 1

        return data

    def _get_light_ids_from_room(self, room):
        """ Returns the list of lights in a [room] or all light_ids if [room] is None.

        :param room: The room where search lights.
        """

        if room is not None:
            room = room.lower()
        if room is None:
            return [(b.ip, b.port) for b in self.bulbs]

        selected = []
        for b in self.bulbs:
            if room in b.name:
                selected.append(b)

        return [(b.ip, b.port) for b in selected]


if __name__ == "__main__":
    sy = SnipsYeelight()
