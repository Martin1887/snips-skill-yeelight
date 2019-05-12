#!/usr/bin/env python2
# -*-: coding utf-8 -*-

from hermes_python.hermes import Hermes
import hermes_python
from snipsyeelight.snipsyeelight import SnipsYeelight

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def getPercentage(snips):
    """ Get the percentage value.

    :param snips: The snips object
    """
    if snips.slots.percent:
        res = snips.slots.percent[0].slot_value.value.value
        return unicode(res)
    return None

def getTemperature(snips):
    """ Get the temperature value.

    :param snips: The snips object
    """
    if snips.slots.temperature:
        res = int(snips.slots.temperature[0].slot_value.value.value)
        return unicode(res)
    return None

def getRoom(snips):
    """ Get the house_room value.

    :param snips: The snips object
    """
    if snips.slots.house_room:
        res = snips.slots.house_room[0].slot_value.value.value
        return unicode(res)
    return None

def getColor(snips):
    """ Get the color value.

    :param snips: The snips object
    """
    if snips.slots.color:
        res = snips.slots.color[0].slot_value.value.value
        return unicode(res)
    return None


def reduceBright(hermes, intent_message):
    """ Reduces the intensity in percentage in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    percent = getPercentage(intent_message)
    house_room = getRoom(intent_message)
    hermes.skill.light_down(percent, house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

def changeBright(hermes, intent_message):
    """ Changes the intensity in percentage in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    percent = getPercentage(intent_message)
    house_room = getRoom(intent_message)
    hermes.skill.light_on_set(intensity=percent, location=house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

def increaseBright(hermes, intent_message):
    """ Increases the intensity in percentage in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    percent = getPercentage(intent_message)
    house_room = getRoom(intent_message)
    hermes.skill.light_up(percent, house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

def reduceTemperature(hermes, intent_message):
    """ Reduces the temperature in percentage in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    percent = getPercentage(intent_message)
    house_room = getRoom(intent_message)
    hermes.skill.temperature_down(percent, house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

def changeTemperature(hermes, intent_message):
    """ Changes the temperature in percentage in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    temp = getTemperature(intent_message)
    house_room = getRoom(intent_message)
    if 1700 <= temp <= 6500:
        hermes.skill.light_on_set(temperature=temp, location=house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

def increaseTemperature(hermes, intent_message):
    """ Increases the temperature in percentage in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    percent = getPercentage(intent_message)
    house_room = getRoom(intent_message)
    hermes.skill.temperature_up(percent, house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

def changeColor(hermes, intent_message):
    """ Changes the color in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    color = getColor(intent_message)
    house_room = getRoom(intent_message)
    hermes.skill.light_on_set(color=color, location=house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

def turnOff(hermes, intent_message):
    """ Turns off in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    house_room = getRoom(intent_message)
    hermes.skill.light_off(house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

def turnOn(hermes, intent_message):
    """ Turns on in the indicated location.

    :param hermes: The hermes object.
    :param intent_message: The intent message with slots.
    """
    house_room = getRoom(intent_message)
    hermes.skill.light_on_set(location=house_room)
    current_session_id = intent_message.session_id
    hermes.publish_end_session(current_session_id, '')

if __name__ == "__main__":
    skill = SnipsYeelight()
    
    with Hermes(MQTT_ADDR.encode("ascii")) as h:
        h.skill = skill
        h.subscribe_intent("Martin1887:reducirBrilloYeelight", reduceBright) \
            .subscribe_intent("Martin1887:reduceBrightYeelight",reduceBright) \
            .subscribe_intent("Martin1887:cambiarBrilloYeelight", changeBright) \
            .subscribe_intent("Martin1887:changeBrightYeelight", changeBright) \
            .subscribe_intent("Martin1887:aumentarBrilloYeelight", increaseBright) \
            .subscribe_intent("Martin1887:increaseBrightYeelight", increaseBright) \
            .subscribe_intent("Martin1887:reducirTemperaturaYeelight",reduceTemperature) \
            .subscribe_intent("Martin1887:reduceTemperatureYeelight",reduceTemperature) \
            .subscribe_intent("Martin1887:cambiarTemperaturaYeelight", changeTemperature) \
            .subscribe_intent("Martin1887:changeTemperatureYeelight", changeTemperature) \
            .subscribe_intent("Martin1887:aumentarTemperaturaYeelight", increaseTemperature) \
            .subscribe_intent("Martin1887:increaseTemperatureYeelight", increaseTemperature) \
            .subscribe_intent("Martin1887:cambiarColorYeelight", changeColor) \
            .subscribe_intent("Martin1887:changeColorYeelight", changeColor) \
            .subscribe_intent("Martin1887:apagarYeelight", turnOff) \
            .subscribe_intent("Martin1887:turnOffYeelight", turnOff) \
            .subscribe_intent("Martin1887:encenderYeelight", turnOn) \
            .subscribe_intent("Martin1887:turnOnYeelight", turnOn) \
            .loop_forever()
