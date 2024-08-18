from caseLogic import *
from ai import *
from pContext import *

# parse to grab text -> return ARRAY
def parseSubcatogeries(subcatogeries):
    pass


# Develop prompt
def developPrompt(type, topic, context, difficulty, levels, subcategories, subcategoryCount):
    # Start building the prompt with topic, context, difficulty, and level range
    prompt = (
        f"You are creating a Jeopardy-style game focused on the topic '{topic}'. "
        f"The purpose of this game is {type}. For reference, consider the following context: '{context}'. "
        f"The game should be {difficulty} level and should have a maximum level of {levels}. "
        f"Please create {subcategoryCount} subcategories related to the main topic '{topic}'. "
        f"Format the response as a well-structured JSON object as follows:\n\n"
        "{\n"
        "  'Subcategories': {\n"
    )

    # Loop through to create JSON structure for the specified number of subcategories
    for i in range(1, subcategoryCount + 1):
        subcategory_placeholder = (
            f"    '{subcategories}{i}': {{\n"
        )
        prompt += subcategory_placeholder
        
        # Loop to create questions for each level from 100 to the specified levels
        for level in range(100, levels + 100, 100):
            question_placeholder = (
                f"      '{level}': {{'Question': 'Question {level} for {subcategories}{i}', 'Answer': 'Answer {level}'}},\n"
            )
            prompt += question_placeholder
            
        # Remove trailing comma from the last question and close the subcategory
        prompt = prompt.rstrip(',\n') + "\n    },\n"

    # Remove the trailing comma from the last subcategory and close the JSON structure
    prompt = prompt.rstrip(',\n') + "\n  }\n"
    prompt += "}\n\n"
    prompt += "Please return ONLY the JSON data in the format specified above."

    return prompt

# Example call
output = developPrompt('concept', 'Math', 'this is a context', 'AP', 500, 'math', 5)
print(output)

# Function to grab all the data
def jeopardy(type, topic, context, difficulity, levels=500, subcatogeries = "", subcategoryCount = 5):
    print('Works')

    parseSubcatogeries()
    parseContext()
    # parse so it only returns the JSON data
    jeapordyOpenAI()
    return # 

print(jeopardy('ho', 500, 'ho', 'ho', 'ho', 'ho', 'ho')) # Works