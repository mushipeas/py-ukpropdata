import pprint
pp = pprint.PrettyPrinter(indent=4)
from functools import reduce

keys = {
    "DSASM":"averagePricesDetachedSASM",
    "FMSASM":"averagePricesFlatMaisonetteSASM",
    "SA":"averagePricesSA",
    "SASM":"averagePricesSASM",
    "SDSASM":"averagePricesSemiDetachedSASM",
    "TSASM":"averagePricesTerracedSASM"
}

def sumAvgPrice(dataPerRegion,key):
    avgPrice = []
    for region in dataPerRegion:
        avgPriceSum = reduce(lambda x, y:x + dataPerRegion.get(region).get(y).get(keys.get(key), 0), dataPerRegion.get(region),0)
        avgPrice.append(avgPriceSum/len(dataPerRegion.get(region)))
    #pp.pprint(avgPrice)
    return avgPrice

def sumAvgPriceOldV(dataPerRegion):
    avgPrice = []
    for key in dataPerRegion:
        avgPriceSum = 0
        Months = 0
        for date in dataPerRegion.get(key):
            avgPriceSum += dataPerRegion.get(key).get(date).get(keys.get(key), 0)
            Months += 1
        avgPrice.append(avgPriceSum/Months)
    return avgPrice
