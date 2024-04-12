import datetime
import pyvisa
import socket
# #  MS5A234205742 - rigol MSO5104
rm = pyvisa.ResourceManager('@py')
print(rm.list_resources())


#
#
# scope = rm.open_resource('TCPIP::192.168.1.2::INSTR', timeout=1000, chunk_size=1024000, encoding='latin-1')
scope = rm.open_resource('TCPIP::192.168.1.2::INSTR')


scope.write(':STOP')

scope.write(':CLE')

scope.write(':RUN')
scope.write(':WAV:FORM BYTE')
scope.write(':WAV:SOUR CHAN1')
scope.write(':WAV:MODE RAW')

scope.write(':WAV:FORM BYTE')
scope.write(':WAV:DATA?')
# ident = scope.query()
waveform_data = scope.read_raw()

# print(waveform_data)

scope.close()
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('192.168.1.2', 5555))
# print('hello')
# sock.sendall(b'*IDN?\n')
# print(2)
# data = sock.recv(1024)
# #
# print(data.decode())
# #
# sock.close()
# print('done')