#!/usr/bin/env python
import datetime as dt
import numpy as np
import scipy.stats as stats
#import matplotlib
import matplotlib.pyplot as plt
import rainfall

def plot_rainfall(data):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    for tuple in data:
        ax.plot(tuple[1], tuple[0])
    ax.set_ylabel('Monthly rainfall (mm)')
    ax.set_xlabel('Date')
    fig.autofmt_xdate()

    return fig

if __name__ == "__main__":
    import sys
    month = int(sys.argv[1])
    data = []
    rf1 = rainfall.Rainfall(sys.argv[2])
    data.append(rf1.list_data(start=dt.date(1980,1,1), end=dt.date(2010,1,1), months=[month]))
    rf2 = rainfall.Rainfall(sys.argv[3])
    data.append(rf2.list_data(start=dt.date(1980,1,1), end=dt.date(2010,1,1), months=[month]))

    f = plot_rainfall(data)

    values_1 = np.array(data[0][0])
    print values_1.max()
    values_2 = np.array(data[1][0])
    print values_2.max()
    print stats.normaltest(values_1)
    print stats.normaltest(values_2)
    print stats.pearsonr(values_1, values_2)

    
    plt.show()





