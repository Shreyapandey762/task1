import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths

# Load the dataset (adjust the path to your dataset location)
data = pd.read_csv('Simulator_readings.csv')

# Plot Time vs FHR1
plt.figure(figsize=(10, 5))
plt.plot(data['Time(ms)'], data['Fhr1(BPM)'], label='FHR1')
plt.xlabel('Time (ms)')
plt.ylabel('FHR1 (BPM)')
plt.title('Fetal Heart Rate (FHR1) over Time')
plt.legend()
plt.show()

# Plot Time vs UC
plt.figure(figsize=(10, 5))
plt.plot(data['Time(ms)'], data['Uc(TOCO)'], label='UC', color='orange')
plt.xlabel('Time (ms)')
plt.ylabel('UC (TOCO)')
plt.title('Uterine Contractions (UC) over Time')
plt.legend()
plt.show()

# Step 4: FHR Analysis (Epochs and Pulse Intervals)

# Number of data points per epoch (3.75 seconds = 15 data points since 4 data points per second)
points_per_epoch = int(3.75 * 4)

# Arrays to store the results for each epoch
epochs_fhr = []
pulse_intervals = []

# Loop over the data in chunks of points_per_epoch
for i in range(0, len(data), points_per_epoch):
    epoch_fhr = data['Fhr1(BPM)'][i:i + points_per_epoch].mean()
    epochs_fhr.append(epoch_fhr)
    
    # Calculate pulse interval in milliseconds (60000 ms / bpm)
    pulse_interval = 60000 / epoch_fhr
    pulse_intervals.append(pulse_interval)

print("Average FHR per epoch:", epochs_fhr)
print("Pulse Intervals per epoch (in ms):", pulse_intervals)

# Detect peaks in the UC (TOCO) data
uc_data = data['Uc(TOCO)']
peaks, _ = find_peaks(uc_data, height=5)  # You can adjust the height threshold as needed

# Calculate the width of each peak at half its maximum height
peak_widths_half = peak_widths(uc_data, peaks, rel_height=0.5)

# Convert widths from samples to time (each sample is 250 ms)
widths_in_seconds = peak_widths_half[0] * 0.25

# Filter peaks with width greater than 30 seconds
wide_peaks = widths_in_seconds[widths_in_seconds > 30]

# Calculate the average duration of the wide peaks
if len(wide_peaks) > 0:
    avg_peak_duration = wide_peaks.mean()
else:
    avg_peak_duration = 0

print(f"Number of peaks with width > 30 seconds: {len(wide_peaks)}")
print(f"Average duration of wide peaks: {avg_peak_duration:.2f} seconds")
