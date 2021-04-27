
#Python Challenge: Rock Paper Scissors 
#Make a two-player Rock-Paper-Scissors game. 

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

name1=input("Player One: Whats your name?")
name2=input("Player Two: Whats your name?")

print("We will play 2 out of 3.")

round=1

counter_Player_1=0
counter_Player_2=0

while round<=3:

    
    value1=input("Player1 : Rock - Scissor - Paper?")

   
    value2=input("Player2 : Rock - Scissor - Paper?")

    if (value1==value2):
        print("Tie")

    elif (value1=="Rock" and value2=="Scissor"):
        round+=1
        counter_Player_1+=1
        print( name1," wins")
        
    elif(value1=="Rock" and value2=="Paper"):
        round+=1
        counter_Player_2+=1
        print(name2," wins ")

    elif(value1=="Scissor" and value2=="Rock"):
        round+=1
        counter_Player_2+=1
        print(name2," wins ")

    elif(value1=="Scissor" and value2=="Paper"):
        round+=1
        counter_Player_1+=1
        print( name1," wins")

    elif (value1=="Paper" and value2=="Rock"):
        round+=1
        counter_Player_1+=1
        print( name1," wins")

    elif (value1=="Paper" and value2=="Scissor"):
        round+=1
        counter_Player_2+=1
        print(name2," wins ")

    #if there is in error in the input
    else:
        print("There was an error in your input")

print(name1, "has: ",counter_Player_1,"Points. ",name2,"has: ",counter_Player_2,"Points.")    
    
