## 安装依赖库
# !pip install -r requirements.txt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Function definitions

# 定义连续信号 f(t)
def continuous_signal(t):
    return np.sin(2 * np.pi * 0.1*t) + 0.5 * np.sin(6 * np.pi * 0.1*t)

# 周期单位冲激脉冲序列 p(t)
def dirac_pulse(t, Ts):
    return np.where(np.abs((t / Ts) % 1) < 1e-10, 1, 0)

# 计算信号的傅里叶变换(采用FFT)
def fourier_transform(signal, t):
    dt = t[1] - t[0]
    N = len(t)
    frequency = np.fft.fftfreq(N, dt)
    spectrum = np.fft.fft(signal)
    return frequency, spectrum

# 图形化界面
def update(val):
    Ts = slider.val
    t = np.arange(0, 10, Ts)

    f = continuous_signal(t)
    p = dirac_pulse(t, Ts)
    fs = f * p

    frequency_fs, spectrum_fs = fourier_transform(fs, t)

    ax1.clear()
    ax1.plot(t, f)
    ax1.set_xlabel('Time')
    ax1.set_ylabel('f(t)')
    ax1.set_title('Continuous Signal')

    ax2.clear()
    ax2.stem(t, p)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('p(t)')
    ax2.set_title('Pulse Signal')

    ax3.clear()
    ax3.stem(t, fs)
    ax3.set_xlabel('Time')
    ax3.set_ylabel('fs(t)')
    ax3.set_title('Sampled Signal')

    ax4.clear()
    ax4.plot(frequency_fs, np.abs(spectrum_fs))
    ax4.set_xlabel('Frequency')
    ax4.set_ylabel('Magnitude')
    ax4.legend(['Sampled Signal'])
    ax4.set_title('Frequency Spectrum')

    plt.tight_layout()
    plt.draw()

# Set up the initial parameters
Ts_init = 0.1

# Create the main figure
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
plt.subplots_adjust(left=0.1, bottom=0.25)

# Create a slider axis
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Sampling Period (Ts)', 0.01, 1.0, valinit=Ts_init)

# Attach the update function to the slider
slider.on_changed(update)

# Initialize the plots
update(Ts_init)

plt.show()
