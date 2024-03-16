import librosa
import matplotlib.pyplot as plt
import numpy as np

x, sr = librosa.load("001-sibutomo.wav")
mfcc = librosa.feature.mfcc(x ,sr=sr)

N = len(x)
dt = 1 / sr
F = np.fft.fft(x)
freq = np.linspace(0, sr, N)
amp = np.abs(F)
plt.bar(freq, amp)
plt.xlim(0, max(freq)/2)
plt.savefig("powerspectol.png")
plt.clf()
print("Complete!")
