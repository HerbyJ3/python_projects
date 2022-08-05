import random
import string 
from string import digits, punctuation

#list of Dept's capitalized
choices = ['Accounting', 'Marketing', 'FinOps']

#converts list to first capital letters, to ensure case sensistivity
for i in range(len(choices)):
    choices[i] = choices[i].title()

#list of names to be randomized
list_one = ["Hosting", "Leaseweb", "TechTruce", "One_Big_Company", "Digital_Potion", "ServerMania_Data_Centre", "Above_Host", "Locomotion_Creative",
            "Platform_Twenty_Ltd", "Appy_Monkey", "Cinnamon_Entertainment_Group", "The_Mobile_App_Developers", "Out_of_House", "Hostezza", "AristoMedia", "Bridge_Fibre",
            "HOSTGAI", "Plug_&_Play Web_Design", "PrimeXeon_Limited", "Simple_Design_Websites", "Brighter", "Stax", "Weeb_Digital", "Stanton_Shallcross", "Clarity_CB1"]

#starting counter time
counter = 3
 
#function to randomize and generate the list of names + characters
def ec2name():
    for item in range(num):
        item = random.choice(list_one)
        digits = random.choices(string.digits, k=3) #list of random  3 digits
        letters = random.choices(string.ascii_letters, k=3) #list of random 3 letters
        together = digits + letters #list of random letters and numbers combined
        combined = ''.join(random.sample(together, len(together))) #list converted into a string with all characters merged together & shuffled
        print(item + combined)
           
#Input to enter the number of instances
num = int(input("Enter the number of EC2 instances: "))

#Input to enter Department   
dept = str(input("Please Enter Your Deptartment: ")).title()        

#conditional loop, if true to call ec2name function
while dept not in choices and counter >= 1:
    print("Unauthorized Department Access " + str(counter) + " Attempts Left")
    dept = str(input("Please Re-Enter Your Deptartment: ")).title()
    counter -= 1
else:
    ec2name()
