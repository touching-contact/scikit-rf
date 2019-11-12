import skrf as rf
from pylab import *
from skrf.data import wr2p2_short as short
from skrf.data import wr2p2_delayshort as delayshort

figure()
difference = (short - delayshort)
difference.plot_s_mag(label='Mag of difference')
short.plot_s_mag(label='Mag of measured')
delayshort.plot_s_mag(label='Mag of Probe')

draw();show();
