# 与串行端口的数据通信
import serial


# 你想通过串行端口读写数据，典型场景就是和一些硬件设备打交道(比如一个机器人或传感器)。
# 打开一个串行端口
ser = serial.Serial('COM1',  # Device name varies
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)


ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()



