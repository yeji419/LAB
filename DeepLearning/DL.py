import matplotlib.pyplot as plt
import librosa.display
import librosa
import numpy as np
from scipy import signal
from scipy.fft import fft, ifft, fftfreq

sig_s, sr_s = librosa.load('JCT.wav', sr = 16000)
sig_m, sr_m = librosa.load('Coldplay_Yellow', sr = 16000)

 