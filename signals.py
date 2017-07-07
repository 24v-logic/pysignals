import numpy as np
import matplotlib.pyplot as plt

class periodicWaveform():
    def __init__(self,A,f,p):
        self.amplitude = A
        self.frequency = f
        self.phase = p
        self.T = 2*np.pi/f
        self.analogFunction = str(self.amplitude)+"Cos("+str(self.frequency)+"pi*t -"+str(self.phase)+"pi)"

    def func(self,i):
        y =self.amplitude*np.cos(self.frequency*i - self.phase*np.pi)
        return y

def plot_period(waveForm):
    n = 360
    t_data = []
    y_data = []
    for i in range(n):
        t_data.append(i*waveForm.T/n)
        y_data.append(waveForm.func(t_data[i]))
    plt.ion()
    plt.title(waveForm.analogFunction)
    plt.axhline(y=0, color='b', linestyle='-')
    plt.plot(t_data,y_data)
    plt.ioff()

def coupled_example():
    f1 = periodicWaveform(1,8,-0.3)
    f2 = periodicWaveform(1.3, 3, 0)
    n = 360
    t_data = []
    y_data = []
    for i in range(n):
        t_data.append(i*f2.T/n)
        y_data.append(f1.func(t_data[i])+f2.func(t_data[i]))
    plt.ion()
    plt.title(f1.analogFunction + "+" + f2.analogFunction)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.plot(t_data,y_data)
    plt.ioff()
