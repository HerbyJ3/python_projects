

import random

#imports special charavters, i.e punctuation
from string import digits, punctuation
from urllib import request 

digits = list(digits)
special_char = list(punctuation)
jib = ""
a = chr(random.randint(65, 90))
b = chr(random.randint(65, 90)).lower()


#create a list with all these special characters in
  
for i in range(5):
    random_stuff = special_char[random.randint(0, 31)] 
    random_digit = digits[random.randint(0, 9)] 
    jib = jib + random_stuff + random_digit
    combined = ''.join(random.sample(jib, len(jib)))
    

    
print(a + b + combined)
