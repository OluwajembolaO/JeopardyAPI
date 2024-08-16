from caseLogic import *
from ai import *
from pContext import *

# parse to grab text -> return ARRAY
def parseSubcatogeries(subcatogeries):
    pass


# Develop prompt
def developPrompt(type, topic, context, difficulity, levels, subcatogeries, subcategoryCount):
    pass

# Function to grab all the data
def jeapordy(type, topic, context, difficulity, levels=500, subcatogeries = "", subcategoryCount = 5):
    print('Works')

    parseSubcatogeries()
    parseContext()
    # parse so it only returns the JSON data
    jeapordyOpenAI()
    return # 

print(jeapordy('ho', 500, 'ho', 'ho', 'ho', 'ho', 'ho')) # Works