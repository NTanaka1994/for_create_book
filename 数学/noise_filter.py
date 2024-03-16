import numpy as np
import librosa
from scipy.io.wavfile import write

x, sr = librosa.load("001-sibutomo.wav")
N = len(x)
freq = np.linspace(0, sr, N)
F = np.fft.fft(x)

F = F / (N / 2)
F[0] = F[0] / 2

F2 = F.copy()

F2[(freq>5000)] = 0
F2[(freq<50)] = 0

x2 = np.fft.ifft(F2)
x2 = np.real(x2*N)

write("filterd.wav", rate=sr, data=x2)
