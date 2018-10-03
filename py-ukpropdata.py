#import geoplotlib as gpl
import dataPlot
import dataCombine as dc
import dataImport # old api
#import dataImport_new_api as dataImport  # new api
import pprint
pp = pprint.PrettyPrinter(indent=4)
from functools import reduce


# data import
dataPerRegion = dataImport.getDataPerRegion(2012, 2013)
#print('Number of regions: ' + str(len(dataPerRegion)))
#pp.pprint(dataPerRegion)

# collate average monthly price from dataPerRegion
avgPrice = dc.sumAvgPrice(dataPerRegion,"DSASM")

# data reducion for plotting
regions = list(dataPerRegion.keys())[30:60]
prices = avgPrice[30:60]
heading = "Average House Prices During 2012 - 2013"

# plot data
dataPlot.plotMonthlyValues(regions, prices, heading)