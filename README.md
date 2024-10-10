# FHR and UC Data Analysis

## 1. Plotting Graphs
- **Time vs FHR**: Displays the fetal heart rate (FHR) over time.
- **Time vs UC**: Displays uterine contractions (UC) over time.

## 2. FHR Analysis
- The data was divided into epochs of **3.75 seconds** (16 epochs per minute).
- For each epoch, the following were calculated:
  - **Average FHR**: `[139.2 bpm]`
  - **Pulse Interval**: `[431.03 ms]`

## 3. UC Peak Detection
- Peaks in the UC data were detected using SciPy’s `find_peaks` method.
- No peaks wider than **30 seconds** were found.
- Therefore, the average duration of wide UC peaks was: **0.00 seconds**.

## Conclusion
This analysis provides an overview of fetal heart rate and uterine contractions over time. The dataset used here was limited in size, resulting in no detected peaks wider than 30 seconds. For real-world applications, using larger datasets may yield more insightful results.
