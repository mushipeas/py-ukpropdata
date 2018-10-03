import matplotlib.pyplot as plt
import numpy as np

def plotMonthlyValues(regions, prices, heading):
    
    # plot
    plt.rcdefaults()
    fig, ax = plt.subplots()

    ax.barh(regions, prices, align='center',
            color='green', ecolor='black')
    ax.set_yticks(regions)
    ax.set_yticklabels(regions)
    #ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Price')
    ax.set_title(heading)

    plt.show()