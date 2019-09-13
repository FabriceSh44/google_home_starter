from serial import Serial

def apply_action(action):
    dico = {"power":b"2", "speed":b"3", "light":b"4"}
    ser= Serial("/dev/ttyAMA0")
    ser.baudrate =9600

    ser.write(dico[action])
    print("Applied {}".format(action))
