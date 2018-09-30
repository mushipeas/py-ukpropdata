import json
import os
import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)

month_storage_directory = './downloads/monthDataNewApi/'
if not os.path.exists(month_storage_directory):
    os.makedirs(month_storage_directory)

# function that takes data from api - writes to file - accesses file if data is already present
def requestMonthData(yearMonth):
    month_file = month_storage_directory + yearMonth + '.json'
    # check if data is present
    if os.path.exists(month_file):
        # file exists
        with open(month_file) as json_file:  
            monthData = json.load(json_file)
    else:
        # file doesn't exist
        monthData = requestDataFromApi(yearMonth)
        # write data to json file
        with open(month_file, 'w') as outfile:  
            json.dump(monthData, outfile)

    return monthData


# function that calls api to get month's data (all pages)
def requestDataFromApi(yearMonth, p=0):
    request = requests.get('http://landregistry.data.gov.uk/data/ukhpi/month/'+ yearMonth +'.json?_page=' +str(p))
    totalresults = request.json()['result']['totalResults']
    maxlastval = request.json()['result']['startIndex']+request.json()['result']['itemsPerPage']
    items = request.json()['result']['items']
    page = p
    if maxlastval < totalresults:
        return items + requestDataFromApi(yearMonth,page+1)
    #pp.pprint(items)
    return items

# function that collates data from all months in range
def getDataPerRegion( startYear, endYear ):
#    print("Main Function Run")
    dataByRegion = {}
    for year in range(startYear, endYear):
        for month in range(1, 12):
            items = requestMonthData(str(year)+'-'+str(month).zfill(2))
            #pp.pprint(items)
            for item in items:
                region = item['refRegion']['label'][0]['_value']
                refMonth = item['refMonth']
                if region in dataByRegion:
                    dataByRegion[region][refMonth] = item
                else:
                    dataByRegion[region] = {}
                    dataByRegion[region][refMonth] = item
    return dataByRegion
