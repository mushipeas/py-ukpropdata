import argparse

# takes arguments passed when running the script
def parse(arg):
    if len(arg) < 5:
        return requestInput()
    return {
        "typeOfData":       arg[1],
        "typeOfProperty":   arg[2],
        "startYear":        int(arg[3]),
        "endYear":          int(arg[4])
    }

# requests arguments if none (or the wrong type) were provided
def requestInput():
    # work in progress - currently returns some default args
    return defaults

defaults = {
    "typeOfData":       "AvgMonthly",
    "typeOfProperty":   "SASM",
    "startYear":        2012,
    "endYear":          2013
    }