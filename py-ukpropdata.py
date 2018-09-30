import matplotlib.pyplot as plt
import numpy as np
# import geoplotlib as gpl
import pprint
pp = pprint.PrettyPrinter(indent=4)
import dataImport # old api
# import dataImport_new_api as dataImport  # new api


# data import
dataPerRegion = dataImport.getDataPerRegion(2012, 2013)
print('Number of regions: ' + str(len(dataPerRegion)))
#print(list(dataPerRegion.keys()))

# import price data from dataPerRegion
# averagePriceSemiDetached for new api, averagePricesDetachedSASM for old
averagePricesDetachedSASM = []
for key in dataPerRegion:
        averagePricesSum = 0
        averagePriceNum = 0
        for date in dataPerRegion.get(key):
                averagePricesSum += dataPerRegion.get(key).get(date).get("averagePricesDetachedSASM", 0)
                averagePriceNum += 1
        averagePricesDetachedSASM.append(averagePricesSum/averagePriceNum)

# data allocation for plotting
regions = list(dataPerRegion.keys())[30:60]
year = "2012 - 2013"
y_pos = np.arange(len(regions))
prices = averagePricesDetachedSASM[30:60]

# plot
plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(y_pos, prices, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(regions)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Price')
ax.set_title('Average Detached Property Value in ' + year)

plt.show()