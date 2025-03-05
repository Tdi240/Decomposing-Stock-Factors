#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 10:53:05 2025

@author: haerdle
"""

import numpy as np
import matplotlib.pyplot as plt
from PyEMD import EMD

# Generate a sample signal
def generate_sample_signal(t):
    # A signal with multiple frequency components
    signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 10 * t) + 0.2 * np.sin(2 * np.pi * 20 * t)
    return signal

# Time vector
t = np.linspace(0, 1, 500)

# Generate the signal
signal = generate_sample_signal(t)

# Perform Empirical Mode Decomposition (EMD)
emd = EMD()
IMFs = emd(signal)

# Plot the original signal and IMFs with transparent background
plt.figure(figsize=(10, 8), facecolor='none')  # Set figure background to transparent

# Plot the original signal
plt.subplot(len(IMFs) + 1, 1, 1)
plt.plot(t, signal, label='Original Signal', color='blue', linewidth=3)
plt.legend()
plt.title('Original Signal')

# Plot each IMF
for i, imf in enumerate(IMFs):
    plt.subplot(len(IMFs) + 1, 1, i + 2)
    plt.plot(t, imf, label=f'IMF {i + 1}', color='orange', linewidth=3)
    plt.legend()

plt.tight_layout()

# Save the plot with a transparent background
plt.savefig('EMD_plot.png', transparent=True)

# Show the plot
plt.show()

