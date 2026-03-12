import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.grid()
    plt.plot(time, voltage)
    plt.ylim(0, max_voltage)
    plt.show()

def plot_sampling_period_hist(time):
    dif_time = []
    for i in range(len(time) - 1):
        dif_time.append(time[i+1]-time[i])

    plt.figure(figsize=(10,6))
    plt.hist(dif_time)
    plt.xlim(0, 0.06)
    plt.grid()
    plt.show()