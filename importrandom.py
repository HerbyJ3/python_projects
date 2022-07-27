import random

numbers = [0,1,2,3,4,5]

for number in numbers:
    pass
for number in range(6):
    #print(number)
    pass

for i in range(len(numbers)):
    #print(i)
    pass

number = random.randint(0,10)

while(number !=5):
    print(number)
    number = random.randint(0,10)

print(number)

#################

number = random.randint(0,1000000)
counter = 0
while(number !=404):
    counter += 1
    number = random.randint(0,100000)
    if (counter > 5000):
        break

print(counter)