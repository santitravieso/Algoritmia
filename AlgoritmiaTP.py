import pyedflib
import numpy as np 

import matplotlib.pyplot as plt 

f= pyedflib.EdfReader("chb10_01.edf")
n= f.signals_in_file
signals_labels = f.getSignalLabels()
sigbufs = np.zeros((n,f.getNSamples()[0]))

print(n)

for i in np.arange(n):
    sigbufs[i,:]=f.readSignal(i)

print(sigbufs)

#fig = plt.figure()
#ax = plt.axes()
#for i in np.arange(n):
  #  sigbufs[i, :]= f.readSignal(i)
  #  ax.plot(f.readSignal(i))
   # plt.show()