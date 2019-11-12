import skrf as rf
from pylab import *
# from skrf.data import wr2p2_short as short
# from skrf.data import wr2p2_delayshort as delayshort

short = rf.data.wr2p2_short
line = rf.data.wr2p2_line
delayshort = line ** short

short_2 = line.inv ** delayshort

if short_2 == short :
    print("good!")

figure()
# difference = (short - delayshort)
# difference.plot_s_mag(label='Mag of difference')
short.plot_s_mag(label='Mag of Probe')
line.plot_s_mag(label='Mag of DUT')
# delayshort.plot_s_mag(label='Mag of Measure')
short_2.plot_s_mag(label='Mag of DUT2')

draw();show();
