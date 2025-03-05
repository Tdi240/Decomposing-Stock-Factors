#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 10:53:05 2025

@author: haerdle, updated by ATG on Wed Mar 5 21:42 2025
"""
!pip install EMD-signal
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
fig, axes = plt.subplots(len(IMFs) + 1, 1, figsize=(10, 8), facecolor='none') 

# Set transparent background for all subplots
for ax in axes:
    ax.set_facecolor('none')  # Make subplot backgrounds transparent

# Plot the original signal
axes[0].plot(t, signal, label='Original Signal', color='blue', linewidth=3)
axes[0].legend()
axes[0].set_title('Original Signal')

# Plot each IMF
for i, imf in enumerate(IMFs):
    axes[i + 1].plot(t, imf, label=f'IMF {i + 1}', color='orange', linewidth=3)
    axes[i + 1].legend()

plt.tight_layout()

# Save the plot with a fully transparent background
plt.savefig('EMD_plot.png', transparent=True, bbox_inches='tight', dpi=300)

# Show the plot
plt.show()
