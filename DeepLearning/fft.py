from scipy import signal
from scipy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
import itertools as it

def fastft(y):
    t = np.linspace(0, 2*np.pi, 10000)[:-1]
    k = fftfreq(len(t))
    Y = fft(y)

    plt.figure(figsize=(12,16))
    plt.subplot(3,1,1)
    plt.legend()
    plt.xlabel('time'); plt.ylabel('f(t)'); plt.grid()
    plt.plot(t,np.sin(t), c='gray')
    plt.plot(t,y,linewidth=3.0,c ='black')

    plt.subplot(3,1,2)
    plt.legend()
    plt.xlabel('frequency(Hz)'); plt.ylabel('abs(xf)'); plt.grid(); plt.xlim(-0.05,0.05,10000000)
    plt.plot(k,abs(Y), c='forestgreen')

    plt.subplot(3,1,3)
    plt.ylabel('f(t)'); plt.grid()
    plt.plot(y,linewidth=3.0,c ='black')
    
    for i in range(10,101,30):
        Y = fft(y)
        Y[i+1:-i] = 0
        y_ifft = ifft(Y)
        
        plt.subplot(3,1,3)
        plt.plot(y_ifft, label="n=%d"%i)
        plt.legend()
    plt.show()
    
t = np.linspace(0, 2*np.pi, 10000)[:-1]
y = (signal.square((t-np.pi),duty = 0.5)+1)/2
print('1. Solution: \n')
print(fastft(y), "\n","\n")