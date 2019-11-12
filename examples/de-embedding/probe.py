import skrf as rf
from pylab import *
# from skrf.data import wr2p2_short as short
# from skrf.data import wr2p2_delayshort as delayshort

from skrf import Network, Frequency
induct = Network('Inductor_0p6nH.s2p')
# induct = Network('2.s2p')
probe = Network('E_PROBE_THROUGH.S2P')
probe.frequency.unit = 'ghz'
print(probe.frequency_nb)
# round_sig(probe.frequency, 6) = 'ghz'

# probe = Network('1.S2P')

# Interpolate induct frequency form  probe Frequency
# probe.interpolate_from_f(induct.frequency)
# induct.interpolate_from_f(probe.frequency)
# if probe.frequency == induct.frequency :
#    print("good!")
# else :
# print("bad!")
# probe.write_touchstone('probe.freq')
# induct.write_touchstone('induct.freq')

# whatwewant = induct.inv ** probe


# short_2 = line.inv ** delayshort

# if short_2 == short :
# print("good!")

# figure()
# difference = (short - delayshort)
# difference.plot_s_mag(label='Mag of difference')
# induct.plot_s_db(m=0, n=0, label='Mag of inductor')
# probe.plot_s_db(m=0, n=0,label='Mag of probe')
# delayshort.plot_s_mag(label='Mag of Measure')
# whatwewant.plot_s_db(m=0, n=0,label='Mag of what we want')

# draw();show();
