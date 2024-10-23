import csv
import numpy as np
import matplotlib.pyplot as plt
import mne

time = []
list_Ref1 = []
list_Ref2 = []
list_T3 = []
list_T4 = []
list_O1 = []
list_O2 = []
list_C1 = []
list_C2 = []
splitter = []

with open('Pa2_ExG.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    headers = [header.strip() for header in next(reader)]

    print(len(headers))
    print(headers)
    longnis = len(headers)
    for row in reader:
        time.append(float(row[0]))
        list_Ref1.append(float(row[1]))
        list_Ref2.append(float(row[2]))
        list_T3.append(float(row[3]))
        list_T4.append(float(row[4]))
        list_O1.append(float(row[5]))
        list_O2.append(float(row[6]))
        list_C1.append(float(row[7]))
        list_C2.append(float(row[8]))

    print('done')


with open('Pa2_Marker.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    headers = [header.strip() for header in next(reader)]

    for row in reader:
        print(row)
        splitter.append(float(row[0]))

print(splitter)
splitter.append(100000000000)
five_sec_segments = []
master_time = float(time[0])
splitter_pos = []
j = 0
for i in range(1, len(time)):
    now = float(time[i])
    if now >= splitter[j]:
        splitter_pos.append(len(five_sec_segments))
        master_time = now
        five_sec_segments.append(i)
        j += 1
    elif now - master_time >= 5:
        master_time = now
        five_sec_segments.append(i)
    else:
        continue

for i in splitter_pos:
    print(time[five_sec_segments[i]])

splitter_pos.append(len(five_sec_segments)-1)
print(five_sec_segments)
labels = ['baseline', '6Hz +3BPM', '6Hz -3BPM', '6Hz -6BPM',
          '8Hz +3BPM', '8Hz -3BPM', '8Hz -6BPM', 'pause',
          '10Hz +3BPM', '10Hz -3BPM', '10Hz -6BPM', 'extra', 'extra', 'extra', 'extra', 'extra', 'extra', 'extra']
n_channels = 8
sampling_freq = 250  # in Hertz
ch_names = ["A1", "A2", "T3", "T4", "O1", "O2", "C1", "C2"]
ch_types = ["eeg"] * 8
info = mne.create_info(ch_names, ch_types=ch_types, sfreq=sampling_freq)
info.set_montage("standard_1020")

for h in range(len(splitter_pos) - 1):
    #if h in skips:
        #continue
    begin = five_sec_segments[splitter_pos[h]]
    end = five_sec_segments[splitter_pos[h + 1]]


    data = np.array([[list_Ref1[begin: end]], [np.array(list_Ref2)[begin: end]],
                     [np.array(list_T3[begin: end])], [np.array(list_T4[begin: end])],
                     [np.array(list_C1[begin: end])], [np.array(list_C2[begin: end])],
                     [np.array(list_O1[begin: end])], [np.array(list_O2[begin: end])]])

    data = data.reshape(-1, data.shape[-1])
    raw = mne.io.RawArray(data, info)

    scalings = {'eeg': 8}

    raw.compute_psd(fmax=30).plot(picks="data", exclude="bads", amplitude=False)
    plt.title(labels[h])

    #raw.plot(duration=5, n_channels=8)
plt.figure()
plt.plot(list_C2)
plt.show()
