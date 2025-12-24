"""
Docstring for Modbus.Modbus
"""
from SerialPort import SerialPort
from typing import Literal


class Modbus():

    def __init__(self, mode : Literal["RTU", "ASCII", "UDP","TCP"] = "RTU", **args) -> None:
        self.__mode = mode # save for later

        match mode:
            case "RTU":

                try:
                    self.__port     = args["port"]
                    self.__baudrate = args["baudrate"]

                except KeyError as e:
                    raise KeyError(f"Modbus mode {mode} requires port and baudrate.")

                # optional settings
                if "parity" in args.keys():
                    self.__parity = args["parity"]

                if "stopbits" in args.keys():
                    self.__stopbits = args["stopbits"]

                if "bytesize" in args.keys():
                    self.__bytesize = args["bytesize"]

                if "timeout" in args.keys():
                    self.__timeout = args["timeout"]

                self.__conn = SerialPort(self.__port, self.__baudrate)

            case _:
                raise NotImplementedError(f"Modbus mode {mode} is not implemented.")
            
    def __del__(self):
        self.__conn.__del__()   # call the desctructor for the correct connection !


    @staticmethod
    def RTU_CRC(data : bytes) -> bytes:
        return data # Stumped for now @todo fix this function

    @staticmethod
    def add_MBAP(data : bytes) -> bytes:
        pass

    def openConnection(self):
        self.__conn.open()