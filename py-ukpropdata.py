#import geoplotlib as gpl
import sys
import argumentParse as aParse
import dataPlot
import dataCombine as dc
import dataImport # old api
#import dataImport_new_api as dataImport  # new api
import pprint
pp = pprint.PrettyPrinter(indent=4)
from functools import reduce

# script arguments
if  len(sys.argv) > 1:
        args = aParse.parse(sys.argv)
else:
        args = aParse.requestInput()

# data import from file or api call
dataPerRegion = dataImport.getDataPerRegion(args.get("startYear"), args.get("endYear"))

# collate average monthly price from dataPerRegion
avgPricePerRegion = dc.sumAvgPrice(dataPerRegion,args.get("typeOfProperty"))

# data reducion for plotting
regions = list(dataPerRegion.keys())[30:60]
prices = avgPricePerRegion[30:60]
heading = ("Average " + str(args.get("typeOfProperty")) +
        " Prices During " + str(args.get("startYear")) +
        " - " + str(args.get("endYear")) )

# plot data
dataPlot.plotMonthlyValues(regions, prices, heading)