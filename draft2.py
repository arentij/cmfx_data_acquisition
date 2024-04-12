import serial

# Open serial port, change '/dev/usb1' to the appropriate port
ser = serial.Serial('/dev/ttyACM0', 1000000)  # 9600 is the baud rate

try:
    while True:
        # Read one byte from the serial port
        incoming_byte = ser.read(1)

        # Decode incoming byte to a character
        incoming_char = incoming_byte.decode('utf-8')
        print(incoming_char)
        # Check if the received character is 'X'
        if incoming_char == 'X':
            print("Hello World")

except KeyboardInterrupt:
    # Close the serial port when Ctrl+C is pressed
    ser.close()
    print("\nSerial port closed.")
