import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.where((t >= 0) & (t <= 2), (1/4) * t, 0)

N = 64 
T = 10 
t_continuous = np.linspace(0, T, 1000) 
t_discrete = np.linspace(0, T, N) 

# дискретизувати неперервний сигнал
x_continuous = f(t_continuous)
x_discrete = f(t_discrete)

# перетворення Фур'є для неперервного сигналу
X_continuous = np.fft.fft(x_continuous)
frequencies_continuous = np.fft.fftfreq(len(x_continuous), d=(t_continuous[1] - t_continuous[0]))

# амплітудний спектр неперервного сигналу
amplitude_spectrum_cont = np.abs(X_continuous)

# зсув частоти для амплітудного спектра неперервного сигналу
frequencies_continuous_shifted = np.fft.fftshift(frequencies_continuous)
amplitude_spectrum_cont_shifted = np.fft.fftshift(amplitude_spectrum_cont)

# графік амплітудного спектра неперервного сигналу
plt.figure(figsize=(12, 6))
plt.plot(frequencies_continuous_shifted, amplitude_spectrum_cont_shifted)
plt.title('Амплітудний спектр неперервного сигналу')
plt.xlabel('Частота [Гц]')
plt.ylabel('Амплітуда')
plt.grid(True)
plt.show()

# графіки неперервного та дискретизованого сигналів
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t_continuous, x_continuous, label='Неперервний сигнал', color='blue')
plt.title('Неперервний сигнал')
plt.xlabel('Час (с)')
plt.ylabel('Амплітуда')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.stem(t_discrete, x_discrete, label='Дискретизований сигнал', basefmt=" ", linefmt='orange')
plt.title('Дискретизований сигнал')
plt.xlabel('Час (с)')
plt.ylabel('Амплітуда')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# ручне ДПФ
def manual_dft(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# амплітуда для ручного ДПФ
X_discrete_manual = manual_dft(x_discrete)
frequencies_discrete_manual = np.fft.fftfreq(N, d=(t_discrete[1] - t_discrete[0]))

# ДПФ бібліотека
X_discrete_numpy = np.fft.fft(x_discrete)
frequencies_discrete_numpy = np.fft.fftfreq(N, d=(t_discrete[1] - t_discrete[0]))

# амплітуда ДПФ  біліотека
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(frequencies_discrete_manual, np.abs(X_discrete_manual), label='Амплітуда ручний обрахунок', color='blue')
plt.title('Амплітуда')
plt.xlabel('Частота')
plt.ylabel('y')
plt.xlim(0, 5) 
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(frequencies_discrete_numpy, np.abs(X_discrete_numpy), label='Амплітуда з використанням бібліотеки', color='orange')
plt.title('Амплітуда')
plt.xlabel('Частота')
plt.ylabel('y')
plt.xlim(0, 5) 
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# обернене ПФ
x_reconstructed = np.fft.ifft(X_discrete_numpy)

# порівняння сигналів (обернене і дискретне)
plt.figure(figsize=(12, 6))
plt.plot(t_discrete, x_discrete, label='Дискретне перетворення', color='orange')
plt.plot(t_discrete, np.real(x_reconstructed), label='Обернене перетворення', color='green', linestyle='--')
plt.title('Порівняння')
plt.xlabel('Час (с)')
plt.ylabel('Амплітуда')
plt.grid()
plt.legend()
plt.show()
