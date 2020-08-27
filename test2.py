import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib.animation as animation
from matplotlib.pyplot import MultipleLocator

x = []
btc = []
etc = []
eos = []

with open("/Users/lin/PycharmProjects/AnimationGraph/BTC_ETC_EOS.csv", 'r') as csvfile:
    next(csvfile)
    csvdata = csv.reader(csvfile, delimiter=',')
    for row in csvdata:
        x.append(int(row[0]))
        btc.append(int(row[1]))
        # handle empty ETC values
        if row[2] != '':
            etc.append(int(row[2]))
        else:
            etc.append(None)
        # handle empty EOS values
        if row[3] != '':
            eos.append(int(row[3]))
        else:
            eos.append(None)

dayarr = np.array(x)
btcarr = np.array(btc)
etcarr = np.array(etc)
eosarr = np.array(eos)

fig, ax = plt.subplots()
btcline, = ax.plot(dayarr, btcarr, color='y')
etcline, = ax.plot(dayarr[:len(etcarr)], etcarr, color='g')
eosline, = ax.plot(dayarr[:len(eosarr)], eosarr, color='b')

plt.yscale('log')
# plt.yticks([1, 100,10000,1000000,100000000, 10000000000],[1, 100, "10,000", "1,000,000","100,000,000","10,000,000,000"])
# ax.yaxis.set_major_locator(MultipleLocator(100))
# ax.plot(dayarr, btcarr)
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.ticklabel_format(style='plain')

def animate(num, dayarr, btcarr, etcarr, eosarr, btcline, etcline, eosline):
    btcline.set_data(dayarr[:num], btcarr[:num])
    eosline.set_data(dayarr[:num], eosarr[:num])
    etcline.set_data(dayarr[:num], etcarr[:num])
    # line.axes.axis([0, 4000, 0, 100000000])
    return [btcarr, etcarr, eosarr]
    # ax.clear()
    # ax.plot(dayarr, btcarr)


# plt.plot(dayarr, btcarr, label="BTC")
# plt.plot(dayarr[:len(etcarr)], etcarr, label="ETC")
# plt.plot(dayarr[:len(eosarr)], eosarr, label="EOS")
# plt.plot(dayarr, etcarr, label='etc')
# plt.plot(dayarr, eosarr, label='eos')
plt.title('Cumulative Transactions from Origin Day')
plt.xlabel('Days from Origin')
plt.ylabel('Cumulative Transaction Count')
# plt.legend(loc='lower right')
plt.xlim((0, len(dayarr)))
ani = animation.FuncAnimation(fig, animate, len(dayarr), fargs=[dayarr, btcarr, etcarr, eosarr, btcline, etcline,eosline], interval=1, blit=False)
plt.show()
