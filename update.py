import winreg
import struct

# 43 00 08 10 19 00 00 00

path = "System\CurrentControlSet\Control\MediaProperties\PrivateProperties\Joystick\OEM\VID_046D&PID_C24F"

names = ["OEMData", "OEMName"]
types = [winreg.REG_BINARY, winreg.REG_SZ]
values = [struct.pack('<Q', int("0x1910080043", 16)), "Logitech G29 Driving Force Racing Wheel USB"]

def main():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_WRITE)
        for i in range(2):
            winreg.SetValueEx(key, names[i], 0, types[i], values[i])
            print(names[i] + " -> " + str(values[i]))

        winreg.CloseKey(key)
        print("Key updated!")
    except:
        print("Could not open the key (HKEY_CURRENT_USER\\" + path + ")")
    
    
main()