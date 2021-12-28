import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq, irfft

SAMPLE_RATE = 44100 # Гц
DURATION = 5

def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate*duration, endpoint=False)
    frequincies = x * freq
    y = np.sin((2*np.pi) * frequincies)
    return x, y

x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)
plt.plot(x, y)
plt.show()

_, tone1 = generate_sine_wave(1000, SAMPLE_RATE, DURATION)
_, tone2 = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
tone2 *= 0.3

tone12 = tone1+tone2

normalized_tone = np.int16((tone12 / tone12.max()) * 32767) # ?


plt.plot(normalized_tone[:1000])
plt.show()


N = SAMPLE_RATE*DURATION

yf = rfft(normalized_tone)
xf = rfftfreq(N, 1 / SAMPLE_RATE)




plt.plot(xf, np.abs(yf))
plt.show()


points_freq = len(xf) / (SAMPLE_RATE / 2)

target_idx =  int(points_freq * 4000)

yf[target_idx-2 : target_idx+2] = 0

plt.plot(xf, np.abs(yf))
plt.show()

new_sig = irfft(yf)
plt.plot(new_sig[:1000])
plt.show()

print(yf)