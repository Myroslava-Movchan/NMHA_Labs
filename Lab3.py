import numpy as np
import matplotlib.pyplot as plt

N = 64
I = 10
delta_t = I / N
frequency = 1 / delta_t

# генеруємо рівновіддалені точки в інтервалі для дискретизації
t = np.linspace(0, I, N)

# функція неперервного сигналу
def f(t):
    return np.where((0 <= t) & (t <= 2), (1/4) * t, 0)

# дискретизація сигналу
x_n = np.array([f(t[n]) for n in range(N)])

# перетворення Фур'є неперервного сигналу
X_cont = np.fft.fft(f(t))

# амплітудний спектр неперервного сигналу
amplitude_spectrum_cont = np.abs(X_cont)

# зсув частоти для неперервного спектра
frequencies_cont = np.fft.fftfreq(N, delta_t)
frequencies_cont_shifted = np.fft.fftshift(frequencies_cont)
amplitude_spectrum_cont_shifted = np.fft.fftshift(amplitude_spectrum_cont)

# графік амплітудного спектра неперервного сигналу
plt.figure(figsize=(12, 6))
plt.plot(frequencies_cont_shifted, amplitude_spectrum_cont_shifted)
plt.title('Амплітудний спектр неперервного сигналу')
plt.xlabel('Частота [Гц]')
plt.ylabel('Амплітуда')
plt.show()

# амплітудний спектр дискретного сигналу (без використання перетворення Фур'є з бібліотеки)
X_dft = np.zeros(N, dtype=complex)
frequencies_dft = np.zeros(N)
for k in range(N):
    X_dft[k] = sum(x_n[n] * np.exp(-2j * np.pi * k * n / N) for n in range(N))
    frequencies_dft[k] = k / (N * delta_t)

amplitude_spectrum_dft = np.abs(X_dft)

# зсув частоти для дискретного спектра без перетворення фур'є з бібліотеки
# переміщуємо нульову частоту в центр
frequencies_dft_shifted = np.fft.fftshift(frequencies_dft)
amplitude_spectrum_dft_shifted = np.fft.fftshift(amplitude_spectrum_dft)

# графік амплітудного спектра дискретного сигналу (без використання перетворення Фур'є з бібліотеки)
plt.figure(figsize=(12, 6))
plt.plot(frequencies_dft_shifted, amplitude_spectrum_dft_shifted)
plt.title('Амплітудний спектр дискретного сигналу (без використання перетворення Фур`є з бібліотеки)')
plt.xlabel('Частота [Гц]')
plt.ylabel('Амплітуда')
plt.show()

# амплітудний спектр дискретного сигналу (numpy)
X_k = np.fft.fft(x_n)
amplitude_spectrum_np = np.abs(X_k)

# зсув частоти для дискретного спектра (numpy)
frequencies_np = np.fft.fftfreq(N, delta_t)
frequencies_np_shifted = np.fft.fftshift(frequencies_np)
amplitude_spectrum_np_shifted = np.fft.fftshift(amplitude_spectrum_np)

# графік амплітудного спектра дискретного сигналу (numpy)
plt.figure(figsize=(12, 6))
plt.plot(frequencies_np_shifted, amplitude_spectrum_np_shifted)
plt.title('Амплітудний спектр дискретного сигналу (з numpy)')
plt.xlabel('Частота [Гц]')
plt.ylabel('Амплітуда')
plt.show()

# обернене перетворення Фур'є частотного спектру 
x_prime = np.fft.ifft(X_k)

# графік порівняння оригінального та відновленого сигналу
plt.figure(figsize=(12, 6))
plt.stem(t, x_n, label='Оригінальний сигнал', linefmt='b-', markerfmt='bo', basefmt='b')
plt.plot(t, np.real(x_prime), label='Відновлений сигнал', color='r', linestyle='--')
plt.title('Порівняння оригінального та відновленого сигналу')
plt.xlabel('Час [с]')
plt.ylabel('Амплітуда')
plt.legend()
plt.grid(True)
plt.show()

