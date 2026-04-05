import random as rd 
# LEVEL 1 (Basic – Concept Clear)
# QUESTION 2.Design a number guessing system:
# Generate a random number between 1 and 10
# User guesses the number
# How will you check if the guess is too high or too low?

def show():
    try:
        num = int(input("Enter any number : "))
        random_number = rd.randint(1,10)
        if num>10:
            print("INVALID NUMBER : ")
            exit()
        print("-----------------------------------")
        print(f"COMPUTER NUMBER : {random_number}")
        if random_number>num:
            print(f"YOUR NUMBER LOW NUMBER {num}")
            print("------------------------------------")
        elif random_number <num:
            print(f"YOU ENTERED HIGH NUMBER : {num}") 
            print("------------------------------------")
        else:
            print(f"YOU ENTERED {num}> EQUAL")   
            print(f"-----------------------------------") 
    except ValueError as e :
        print("---------------")
        print(f"ERROR : {e}")  
        print("---------------")
show()

#-------------------------------------------
#QUESTION 3. You have a list:
# ["Ali", "Ahmed", "Sara", "Zara"]
# Select one random name each time
# Which function will you use and why?
#-------------------------------------------


# here i use choice function 
# b/c it return single name at a time 

def show_name(names_list):
    return rd.choice(names_list)
result = show_name(["Ali", "Ahmed", "Sara", "Zara"])
print("--------------------------")
print("NAME : ",result)




#-------------------------------------------
#QUESTION 4. Dice system:
# Roll 2 dice (each from 1–6)
# Think:
# How will you calculate the total?
# When will the user win? 
#-------------------------------------------


def dice_system():
    try:
        num1 = int(input("ENTER A NUMBER BETWEEN (1 TO 6) : "))
        num2 = int (input("ENTER A NUMBER BETWEEN (1 TO 6) : "))
        if num1 >6 or num2 >6 or num1 <0 or num2 <0:
            print("INVALID NUMBER")
            exit()
        r1 = rd.randint(1,6)
        r2 = rd.randint(1,6)
        result1 = num1+num2
        result2 = r1+r2
        if result1 >result2:
            print("--------------------")
            print(f"USER WIN {result1}")
            print("---------------------")
        elif result1 <result2:
            print("-----------------------") 
            print(f"COMPUTER WIN : {result2}")   
            print("------------------------") 
        else:
            print("-------------------")
            print("BOTH EQUAL NO WIN")
            print("--------------------")

    except ValueError as e:
        print("****************************************************")
        print(f"ERROR : {e}")        
        print("****************************************************")

dice_system()

#-------------------------------------------
# 5.Generate 5 random numbers between 1–50
# Numbers must NOT repeat
# Which function will you use and why?
#-------------------------------------------
#---------------------------------------
# i use randit function 
# b/c it give single num at a time 
#---------------------------------------------
def generate_5_num():
    print("--------------------------")
    print("4.PROGRAM HAS BEEN START !")
    print("-----------------------------")
    for i in range(1,6):
        print(f"NUM : {i} : GENERATED NUMBER : {rd.randint(1,50)}")
    else:
        print("--------------------------")
        print("PROGRAM HAS BEEN COMPLETE") 
        print("--------------------------")

generate_5_num()    
    
#-------------------------------------------
# 6.You have a list:
# ["apple", "banana", "mango", "grapes"]
# Select 2 random fruits
# Repetition IS allowed
# Which function will you use and why?
#-------------------------------------------


#-----------------------------------------
# i use choices function 
# b/c it give 2 fruits and also rep is allow 
#-----------------------------------------------

def select_fruit(list_fruits):
    return rd.choices(list_fruits,k=2)

result = select_fruit(["apple", "banana", "mango", "grapes"])
print("--------------------------------")
print(f"SELECTED FRUITS : {result}")
print("-----------------------------------")

#-------------------------------------------
# 7.Same list:
# Select 2 fruits
# Repetition is NOT allowed
# Explain the difference from the previous question
#-------------------------------------------


# here i will use sample b/c here rep is not allow 
# in choices rep is allow 
# its manin d/f

def select_fruit(list_fruits):

    return rd.sample(list_fruits,k=2)

result = select_fruit(["apple", "banana", "mango", "grapes"])
print("--------------------------------")
print(f"SELECTED FRUITS : {result}")
print("-----------------------------------")



#-------------------------------------------
#8. Game logic:
# "win" and "lose"
# Win probability should be 80%
# How will you design this logic?
#-------------------------------------------



def win_or_loss(items):
    return rd.choices(items ,weights=[70,30],k=1)

result = win_or_loss(['win','loss'])
print(result)


#-------------------------------------------
#9. Playlist system:
# You have 10 songs
# Each time the order should change
# Which function will you use?
#-------------------------------------------
#--------------------------------------
# choice b/c it select an single item 
#--------------------------------------
def Playlist_system(song_lst):
    return rd.choice(song_lst)

songs = [
    "Blinding Lights",
    "Shape of You",
    "Levitating",
    "Bad Habits",
    "Stay",
    "Save Your Tears",
    "Peaches",
    "As It Was",
    "Shivers",
    "Industry Baby"
]
result = Playlist_system(songs)
print("********************************")
print("SONG NAME /TYPE : ",result)
print("********************************")

#-------------------------------------------
#10. Lottery system:
# 100 participants
# Select 5 winners
# No repetition
# Design the logic
#-------------------------------------------
def Lottery_System(names):
    return rd.sample(names,k=5)
participants = [
"Ali Khan", "Ayesha Ahmed", "Hassan Raza", "Sara Malik", "Zain Qureshi",
"Fatima Noor", "Bilal Shah", "Hina Iqbal", "Omar Farooq", "Mariam Khan",
"Ahmad Siddiqui", "Sania Tariq", "Usman Ali", "Laiba Hassan", "Khalid Javed",
"Sumaira Aslam", "Imran Riaz", "Areeba Saeed", "Noman Akhtar", "Sadaf Iqbal",
"Shahbaz Tariq", "Hira Khalid", "Waseem Ahmed", "Mahnoor Raza", "Farhan Malik",
"Sana Shahid", "Faisal Anwar", "Iqra Nadeem", "Adnan Hussain", "Zoya Shah",
"Saad Khan", "Mehwish Ali", "Tariq Jamil", "Rabia Farooq", "Asad Riaz",
"Amna Qureshi", "Shahzad Iqbal", "Mona Khalid", "Hamza Ahmed", "Areej Siddiqui",
"Nadeem Shah", "Huma Tariq", "Arham Raza", "Zunaira Malik", "Usama Khan",
"Sadia Ahmed", "Owais Farooq", "Iqbal Hussain", "Fiza Shah", "Bilal Riaz",
"Komal Noor", "Azhar Siddiqui", "Mahwish Ali", "Hassan Javed", "Aiman Khan",
"Shahrukh Riaz", "Maryam Tariq", "Taimoor Ahmed", "Ayesha Khalid", "Shayan Malik",
"Sumaiya Noor", "Ahmad Farooq", "Saba Shah", "Fahad Qureshi", "Nimra Riaz",
"Uzair Khan", "Hira Ahmed", "Ammar Siddiqui", "Sara Javed", "Hamid Raza",
"Zainab Ali", "Fawad Shah", "Rabia Khalid", "Danish Malik", "Iqra Ahmed",
"Talha Riaz", "Areeba Shah", "Faraz Khan", "Sania Noor", "Usman Ahmed",
"Mehreen Tariq", "Saad Riaz", "Hina Khalid", "Omer Malik", "Mahnoor Shah",
"Bilal Ahmed", "Sadia Riaz", "Hamza Khan", "Zoya Farooq", "Shahbaz Ali",
"Amina Noor", "Faisal Ahmed", "Komal Riaz", "Tariq Khan", "Maryam Shah",
"Uzair Ahmed", "Hira Malik", "Adnan Riaz", "Sana Shah", "Hamid Khan",
"Areej Farooq", "Owais Ahmed", "Mona Khalid", "Ahmad Shah", "Sadaf Riaz"
]

result = Lottery_System(participants)
print("---------------------------")
print("PROGRAM HAS BEEN START !")   
print("----------------------------") 
for key,value  in enumerate(result,start=1):
    print(f"WINER {key} : NAME {value} 🎉")
else:
    print("---------------------------")
    print("PROGRAM HAS BEEN COMPLETE")   
    print("----------------------------")     


#-------------------------------------------
# 11.Password generator:
# Password must include:
# 2 uppercase letters
# 2 numbers
# 2 symbols
# How will you use random here?
#-------------------------------------------



def password_generator(ch,num,sym):
    try:

        select_ch = rd.choices(ch,k=2)
        select_num = rd.choices(num,k=2)
        select_symb = rd.choices(symb,k=2)
        return select_ch+select_num+select_symb
    except TypeError as e:
        print("----------------------------------")
        print(f"ERROR : {e}")
        print("----------------------------------")



up_Char = ['A','B','C','D','E','F']
nums = ['1','2','3','4','5']
symb = ['!','@','#','$','%','*']

result = password_generator(up_Char,nums,symb)
print("------------------------------------------")
print(f"GENERATED PASSWORD : {"_".join(result)}")
print("------------------------------------------")



#-------------------------------------------
# 12.AI decision system:
# AI chooses:
# Attack (70%)
# Defend (30%)
# How will random be used?
#-------------------------------------------



def Ai_Decision_System(items):
    return rd.choices(items,weights=[70,30],k=1)

result = Ai_Decision_System(['Attack','Defend'])
print("----------------------")
print(f"RESULT : {result}")
print("----------------------")


#-----------------------------------------------------------
#13. You want:
# Random numbers
# But SAME output every time you run the program
# Which concept will you use and why?
#-----------------------------------------------------------

# print(random.choice(['junaid','jawad','zubair']))  # same number again
def same_output(name_lst):
    state = rd.getstate()
    print("------------------------------------------")
    print("FIRST TIME OUTPUT : ",rd.choice(name_lst))
    rd.setstate(state)
    print("SECOND TIME OUTPUT : ",rd.choice(name_lst))
    print("------------------------------------------")

same_output(['junaid','jawad','zubair'])


    