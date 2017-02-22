#Кости 2.1
import random #include random library

dp = 1000 #player's deposit
dc = 1000 #comp's deposit

print("Select the game mode: ")
choice = int(input("1 - player vs player. 2 - player vs computer\n")) #select the game mode

#start game
while (dp > 1 and dc > 1):
    if(choice == 1): #game vs player
        print("First player's deposit: ",dp)                #print deposit every cycle
        print("Second player's deposit: ", dc)
        bet1 = int(input("First player's bet: "))           #first player bet
        while 1:                                            #Cycle for checking the correct input
            fp = int(input("Bet on the number(2-12): "))    #first player bet on bones
            if(fp < 2 or fp > 12):                          #Checking..
                print("Make bet in the range of 2-12 please")
            else:
                dp = dp - bet1                              #first player's bet
                break
        bet2 = int(input("Second player's bet: "))
        while 1:                                            #Cycle for checking the correct input
             sp = int(input("Bet on the number(2-12): "))
             if(sp < 2 or sp > 12):                         #Checking..
                 print("Make bet in the range of 2-12 please")
             else:
                 dc = dc - bet2             #second player's bet
                 break
        a = random.randint(1,6)     #random
        b = random.randint(1,6)     #for
        sum = a + b                 #throw
        print("Throw...")
        print(a,"and",b, "in total",sum)        #print result
        if fp == sum:                           #check first player for win
            print("The first player win!!!") 
            dp = dp + bet1 + bet2               #wining bet
        elif sp == sum:                         #check second player for win
            print("The second player win!!!")
            dc = dc + bet1 + bet2               #wining bet
        else:  
            print("Nobody guessed")      #nobody huesos
            input("Press Enter to continue..")
        if(dp < 1):                                     #checking for loses first player
            print("The first player out of money =(")
            print("Game Over")
            exit()
        elif(dc < 1):                                   #checking for loses second player
            print("The secind player out of money =(")
            print("Game Over")
            exit()

    if(choice == 2): #game vs computer
        print("Player's deposit: ",dp)    #print deposit every cycle
        print("Computer's deposit: ", dc)
        bet1 = int(input("Player's bet: "))             #first player bet
        while 1:                                        #Cycle for checking the correct input
            fp = int(input("Bet on the number(2-12): "))#first player bet on bones
            if(fp < 2 or fp > 12):                          #Checking..
                print("Make bet in the range of 2-12 please")
            else:
                dp = dp - bet1                  #bet
                dc = dc - bet1                  #bet
                break
        bet2 = bet1                     #comp's bet = player's bet
        sp = random.randint(2,12)   #random
        a = random.randint(1,6)     #for
        b = random.randint(1,6)     #throw
        sum = a + b 
        print("Throw...")
        print(a,"and",b, "in total",sum) #print result
        if fp == sum:                   #check player for win
            print("The player win!!!") 
            dp = dp + bet1 + bet2       #wining bet
        elif sp == sum:                   #check computer for win 
            print("Computer win!!!")
            dc = dc + bet1 + bet2       #wining bet
        else:  
            print("Nobody guessed")     #nobody huesos
            input("Press Enter to continue..")
        if(dp < 1):                     #checking player for loses 
            print("The player out of money =(")
            print("Game Over")
            exit()
        if(dc < 1):                        #checking compyter for loses 
            print("Computer out of money =(")
            print("Game Over")
            exit()
input("Press Enter to exit.")