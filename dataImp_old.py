import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

def requestData(yearMonth, p=0):
    request = requests.get('http://landregistry.data.gov.uk/data/hpi/month/'+ yearMonth +'.json?_page=' +str(p))
    totalresults = request.json()['result']['totalResults']
    maxlastval = request.json()['result']['startIndex']+request.json()['result']['itemsPerPage']
    items = request.json()['result']['items']
    page = p
    if maxlastval < totalresults:
        return items + requestData(yearMonth,page+1)
    #pp.pprint(items)
    return items

def getPlottableData( startYear, endYear ):
#    print("Main Function Run")
    dataByLocation = {}
    for year in range(startYear, endYear):
        for month in range(1, 12):
            items = requestData(str(year)+'-'+str(month).zfill(2))
            #pp.pprint(items)
            for item in items:
                region = item['refRegionName']['_value']
                refPeriod = item['refPeriod']
                if region in dataByLocation:
                    dataByLocation[region][refPeriod] = item
                else:
                    dataByLocation[region] = {}
                    dataByLocation[region][refPeriod] = item
    return dataByLocation

#dataByLocation = getPlottableData(2011, 2014)
#pp.pprint(dataByLocation)
