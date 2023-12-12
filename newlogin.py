# use a dictionary to save the students details 
students={
    #the names and matric number can be changed 
    20183476:"some name 1",
    20183477:"some name 2",
    20183478:"some name 3",
    20183479:"some name 4",
    20183480:"some name 5",
    20183481:"some name 6",
    20183482:"some name 6",
    20183483:"some name 7",
    20183484:"some name 8",
    20183485:"some name 9",
    20183486:"some name 10",
}
#create a loop that keep asking for matric number when the
#mat number is valid and not valid , but stops the program when
#the input is empty
print("==================================================")
print("")
print("WELCOME TO STUDENTSHIP CONFIRMATION PORTAL")
print("")
while True:
    #create a variable that takes in the matric number
    
    print("Note: leave the input field empty to shut the app")
    print("")
    matNum=input("input your matric number :")
    
    #check if the input is empty and break the loop
    if (str(matNum) == ""):
        print("")
        print("GoodBye")
        break
    
    #check if the matric number is in the dictionary,
    #we have and print the message
    
    elif((int(matNum)) in students):
        print("")
        print("Congratulation "+students[int(matNum)]+" ,You are a bonafide CSC student")
        print("")
        print("==================================================")
    else:
        print("")
        print("you are not a registered student")
        print("")
        print("==================================================")
    
print("")
print("==================================================")


