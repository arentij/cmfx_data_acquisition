import numpy
from seabreeze.spectrometers import Spectrometer, list_devices
import matplotlib.pyplot as plt
from datetime import datetime
print('SpectrometerInitiated')
devices = list_devices()
start_read = datetime.now()

# spect = Spectrometer.from_first_available()
spect = Spectrometer(devices[0])
print('Found the spectrometer')
spect.integration_time_micros(130000)

after_read = datetime.now()
time_to_read = (after_read - start_read).total_seconds()
print(time_to_read)
for i_aquisition in range(40):
    waves = spect.wavelengths()

    start_mkaing_array = datetime.now()
    if i_aquisition == 0:
        inten = spect.intensities()
    else:
        inten = numpy.vstack([inten ,spect.intensities()])
    print((datetime.now()-start_mkaing_array).total_seconds())
    if i_aquisition >0:
        plt.plot(waves, inten[i_aquisition])
        plt.show()
# for i in range(10):

spect.close()


