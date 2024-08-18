# File to handle all the edge cases in application

# Checks to see if it's the correct type 
def checkType(type):
    # Convert the input to lowercase and check if it is 'concept' or 'memorization'
    if type.lower() not in ['concept', 'memorization']:
        return False
    else:
        return True

# Checks to see if the levels are correct
def checkLevels(levels):
    # Check if the levels are within the valid range.
    # The range is from 200 to 800 and should be a multiple of 100.
    if levels < 200 or levels > 800 or levels % 100 != 0:
        return False
    
    return True


# Checks to see if the subcatogeries are correct
def checkSubcatogeries(subcatogeries):
    wordCount = subcatogeries.count(',') + 1   
    # check if wordCount is in the range of [1,7] 
    return 0 < wordCount < 8

# Checks to see if the topic is correct
def checkTopic(topic):
    pass    

# Checks to see if the context is correct
def checkContext(context):
    pass    

# Check to see if the difficulity is correct
def checkDifficulity(difficulity):
    # The valid difficulty levels are:
    # elementary school, middle school, high school, ap, college, phd
    valid_levels = ['elementary school', 'middle school', 'high school', 'ap', 'college', 'phd']

    # Convert the input to lowercase and check if it is in the valid levels
    if difficulity.lower() not in valid_levels:
        return False
    else:
        return True

# check to see if's the correct subcategory count
def checkSubcategoryCount(subcategoryCount):
    return subcategoryCount < 8

# check to see if the subcategory count is greater or equal to the subcatogeries given
def checkSubcategoryCountGreater(subcategoryCount, subcatogeries):
    return subcategoryCount >= subcatogeries
