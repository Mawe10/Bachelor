import matplotlib.pyplot as plt
# Open the file in read mode
HRV = []
with open('Pa1base.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        HRV.append(float(line))


plt.plot(HRV)
plt.xlabel('RR-Intervalle')
plt.ylabel('Zeit in ms')
plt.title('Tachogramm Beispiel an der Baseline von Pa1')
plt.show()
