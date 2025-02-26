"""
"""
import Modbus

def main():
    modbus = Modbus.Modbus(1)
    print(f"Modbus Address: {modbus.address_hex}")

    # Test setting invalid address
    try:
        modbus.address = 256
        print("Failed to set invalid address")
    except ValueError as e:
        print(e)

    # Test setting valid address
    modbus.address = 10
    print(f"Modbus Address: {modbus.address_hex}")

    # test read coils
    frame = modbus.Read_Coils(1, 10)

    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Read Coils successful")

    
    frame = modbus.Read_Discrete_Inputs(1, 10)
    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Read Discrete Inputs successful")
    
    frame = modbus.Write_Single_Coil(1, 1)
    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Write Single Coil successful")
    
    frame = modbus.Write_Multiple_Coils(1, [1, 2, 3])
    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Write Multiple Coils successful")
   
    frame = modbus.Read_Input_Registers(1, 10)
    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Read Input Registers successful")

    frame = modbus.Read_Holding_Registers(1, 10)
    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Read Holding Registers successful")

    frame = modbus.Write_Single_Register(1, 100)
    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Write Single Register successful")

    frame = modbus.Write_Multiple_Registers(1, [100, 200, 300])
    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Write Multiple Registers successful")

    frame = modbus.Read_Write_Multiple_Registers(1, 10, [100, 200, 300])
    if (modbus.Check_CRC(frame) == False):
        print("CRC check failed")
        exit()
    else:
        print("CRC check passed - Read Write Multiple Registers successful")
        


if __name__ == "__main__":
    main()