#Get the name of the users
user1_name=input("Enter the name of User1: ")
user2_name=input("Enter the name of User2: ")
while True:
    #Get the options
 user1_option=input(user1_name+" Please choose the option from Rock,Paper,Scissor: ")
 user2_option=input(user2_name+" Please choose the option from Rock,Paper,Scissor: ")

#Run the algorithm to see who wins.
 if user1_option==user2_option:
    print("Its is a tie")
 elif user1_option=="Rock":
    if user2_option=="Scissor":
        print("Rock Wins")
    else:
        print("Paper wins")
 elif user1_option=="Scissor":
    if user2_option=="Paper":
        print("Scissor wins")
    else:
        print("Rock wins")
 elif user1_option=="Paper":
    if user2_option=="Rock":
        print("Paper wins")
    else:
        print("Scissor wins")
 else:
     print("Invalid option,You have not entered Rock,Paper or Scissor. Try again")
 x=input("Want to play Again Yes or No: ")
 if x=="Yes":
   pass
 elif x=="No":
    raise SystemExit
 else:
     print("You have selected an invalid option")
     raise SystemExit
    
     



