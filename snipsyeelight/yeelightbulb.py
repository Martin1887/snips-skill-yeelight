class YeelightBulb:

    def __init__(self, ip, port, name, room=None):
        """ Initialisation

        :param ip: The IP of the bulb
        :param port: The port of the bulb
        :param name: The name of the bulb
        :param room: The room where is the bulb
        """
        self.ip = ip
        self.port = port
        self.name = name
        # TODO: research if in a updated version of the protocol the room is
        # returned, currently the room is searched in the name
        self.room = room

    def __str__(self):
        return '{}:{}'.format(self.ip, self.port)
