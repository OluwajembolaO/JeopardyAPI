# File to handle all the edge cases in application

# Checks to see if it's the correct type 

def checkType(type):
    pass

# Checks to see if the levels are correct
def checkLevels(levels):
    pass

# Checks to see if the subcatogeries are correct
def checkSubcatogeries(subcatogeries):
    pass

# Checks to see if the topic is correct
def checkTopic(topic):
    pass    

# Checks to see if the context is correct
def checkContext(context):
    pass    

# Check to see if the difficulity is correct
def checkDifficulity(difficulity):
    pass

# check to see if's the correct subcategory count
def checkSubcategoryCount(subcategoryCount):
    pass

# check to see if the subcategory count is greater or equal to the subcatogeries given
def checkSubcategoryCountGreater(subcategoryCount, subcatogeries):
    if subcategoryCount >= subcatogeries:
        raise ValueError("The number of subcategories must be less than or equal to the number of subcategories given")
    else:
        pass