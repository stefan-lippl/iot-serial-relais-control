import serial
import codecs
import os
from typing import List
from argparse import ArgumentParser


class SerialManager():
    """Controlles the USB Relais to turn it on and off"""

    def get_connected_ports(self) -> List[str]:
        """ Get a list of all available USB Ports
        - RETURN
            - available_relais: (List[str]) with all ports as a string
        """
        
        available_relays = list()
        ttys = os.popen("ls /dev/tty.usb*").read()

        for tty in ttys.split("\n"):
            try:
                available_relays.append(tty.split("-")[1])
            except:
                pass
        return available_relays


    def set_serial(self, number: str, on_or_off: str) -> None:
        """ Set the status of the relais to on or off
        - ARGS
            - number: (str, required) Name/Number of the port where the relais is located 
            - on_or_off: (str, required) Action, which state should the relais get: on or off
        - RETURN
            - None
        """

        port = '/dev/tty.usbserial-' + number
        ser = serial.Serial(port, 9600, timeout=1)

        if on_or_off == "off":
            ser.write(codecs.decode(b'a00100a1', "hex"))
            ser.close()
        else:
            ser.write(codecs.decode(b'A00101A2', "hex"))
            ser.close()


if __name__ == '__main__':
    parser = ArgumentParser(description='Copy an object from one bucket to another, or in the same bucket')
    parser.add_argument('-a', '--action', help='(required, str) GET available USB ports or set the state of a port to on or off', type=str, required=True)
    parser.add_argument('-p', '--port', help='(optional, str) ', default=True, type=str, required=False)
    parser.add_argument('-s', '--state', help='(optional, str) ', default=True, type=str, required=False)

    args = parser.parse_args()
    action = args.action

    serialmanager = SerialManager()

    if action == 'get':
       ports = serialmanager.get_connected_ports()
       print(ports)

    elif action == 'set':
        port = args.port
        state = args.state
        serialmanager.set_serial(number=port, on_or_off=state)

    else:
        print("Wrong action. Please choose between 'get' or 'set'.")
    


