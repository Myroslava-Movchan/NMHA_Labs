import numpy as np
import matplotlib.pyplot as plt

# функція сигналу
def generate_signal():
    t = np.linspace(0, 10, 500, endpoint=False) # генеруються рівновіддалені точки
    signal = np.piecewise(t, [t < 2], [lambda t: 0.25 * t, 0])
    return t, signal

# Вейвлет Хаара
def haar_wavelet_transform(signal):
    cA = (signal[::2] + signal[1::2]) / 2 # апроксимуючі коефіцієнти
    cD = (signal[::2] - signal[1::2]) / 2 # деталізуючі коефіцієнти
    return cA, cD

def inverse_haar_wavelet_transform(cA, cD, mode="both"):
    approx = np.repeat(cA, 2)
    detail = np.repeat(cD, 2)
    if mode == "approx":
        return approx
    elif mode == "detail":
        return detail
    else:
        return approx + detail

# Мексиканський капелюх (імітація дискретного перетворення)
def discrete_wavelet_transform(signal): # так само, як хаара, але без ділення на 2
    cA = signal[::2] + signal[1::2]
    cD = signal[::2] - signal[1::2]
    return cA, cD

def inverse_wavelet_transform(cA, cD, mode="both"):
    approx = np.repeat(cA, 2) / 2
    detail = np.repeat(cD, 2) / 2
    if mode == "approx":
        return approx
    elif mode == "detail":
        return detail
    else:
        return approx + detail

# генеруємо сигнал
t, signal = generate_signal()

# мексиканський капелюх - дискретне перетворення
cA_mex, cD_mex = discrete_wavelet_transform(signal)
rec_sig_mex = inverse_wavelet_transform(cA_mex, cD_mex)
rec_approx_mex = inverse_wavelet_transform(cA_mex, cD_mex, mode="approx")
rec_detail_mex = inverse_wavelet_transform(cA_mex, cD_mex, mode="detail")

# вейвлет Хаара - дискретне перетворення
cA_haar, cD_haar = haar_wavelet_transform(signal)
rec_sig_haar = inverse_haar_wavelet_transform(cA_haar, cD_haar)
rec_approx_haar = inverse_haar_wavelet_transform(cA_haar, cD_haar, mode="approx")
rec_detail_haar = inverse_haar_wavelet_transform(cA_haar, cD_haar, mode="detail")

# побудова графіків
fig, axes = plt.subplots(4, 2, figsize=(14, 16))

# оригінальний сигнал і коефіцієнти (Мексиканський капелюх)
axes[0, 0].plot(t, signal, label="Original Signal")
axes[0, 0].plot(t[:len(cA_mex)*2:2], cA_mex, label="Approximation Coefficients")
axes[0, 0].plot(t[:len(cD_mex)*2:2], cD_mex, label="Detail Coefficients")
axes[0, 0].set_title("Mexican Hat - Signal and Coefficients")
axes[0, 0].legend()

# відновлення сигналу (Мексиканський капелюх)
axes[1, 0].plot(t, signal, label="Original Signal")
axes[1, 0].plot(t, rec_approx_mex, label="Reconstructed from Approximation")
axes[1, 0].plot(t, rec_detail_mex, label="Reconstructed from Detail")
axes[1, 0].plot(t, rec_sig_mex, label="Reconstructed Full Signal")
axes[1, 0].set_title("Mexican Hat - Reconstructed Signals")
axes[1, 0].legend()

# оригінальний сигнал і коефіцієнти (Хаар)
axes[0, 1].plot(t, signal, label="Original Signal")
axes[0, 1].plot(t[:len(cA_haar)*2:2], cA_haar, label="Approximation Coefficients")
axes[0, 1].plot(t[:len(cD_haar)*2:2], cD_haar, label="Detail Coefficients")
axes[0, 1].set_title("Haar - Signal and Coefficients")
axes[0, 1].legend()

# відновлення сигналу (Хаар)
axes[1, 1].plot(t, signal, label="Original Signal")
axes[1, 1].plot(t, rec_approx_haar, label="Reconstructed from Approximation")
axes[1, 1].plot(t, rec_detail_haar, label="Reconstructed from Detail")
axes[1, 1].plot(t, rec_sig_haar, label="Reconstructed Full Signal")
axes[1, 1].set_title("Haar - Reconstructed Signals")
axes[1, 1].legend()

# деталізовані графіки коефіцієнтів для кожного підходу
axes[2, 0].plot(t[:len(cA_mex)*2:2], cA_mex, label="Approximation Coefficients")
axes[2, 0].plot(t[:len(cD_mex)*2:2], cD_mex, label="Detail Coefficients")
axes[2, 0].set_title("Mexican Hat - Coefficients")
axes[2, 0].legend()

axes[2, 1].plot(t[:len(cA_haar)*2:2], cA_haar, label="Approximation Coefficients")
axes[2, 1].plot(t[:len(cD_haar)*2:2], cD_haar, label="Detail Coefficients")
axes[2, 1].set_title("Haar - Coefficients")
axes[2, 1].legend()

# графіки відновлення для кожного підходу
axes[3, 0].plot(t, rec_approx_mex, label="Reconstructed from Approximation")
axes[3, 0].plot(t, rec_detail_mex, label="Reconstructed from Detail")
axes[3, 0].plot(t, rec_sig_mex, label="Reconstructed Full Signal")
axes[3, 0].set_title("Mexican Hat - Reconstructed Details")
axes[3, 0].legend()

axes[3, 1].plot(t, rec_approx_haar, label="Reconstructed from Approximation")
axes[3, 1].plot(t, rec_detail_haar, label="Reconstructed from Detail")
axes[3, 1].plot(t, rec_sig_haar, label="Reconstructed Full Signal")
axes[3, 1].set_title("Haar - Reconstructed Details")
axes[3, 1].legend()

plt.tight_layout()
plt.show()
