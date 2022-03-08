# import random
from secrets import choice
import string 

def PassGenerator():
    specialChar = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
    
    speciChar =  "".join(specialChar)

    stringArr = string.ascii_uppercase + string.digits +  string.ascii_lowercase + speciChar 

    isMySecret= "-".join(["".join([choice(stringArr ) for _ in range(4)]) for j in range(4)])

    print(isMySecret)

PassGenerator()
