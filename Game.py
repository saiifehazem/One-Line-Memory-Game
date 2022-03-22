import random
import os
import time

#Checking Score Function
def check_Score(p1Score,p2Score):

    if ( p1Score > p2Score and p1Score > 5 ) :
      print("Congratulation Player 1, You Win !")
      return

    elif ( p1Score < p2Score and p2Score > 5 ) :
      print("Congratulation Player 2, You Win !")
      return
    
    elif ( p1Score == p2Score == 5) :
      print("Draw")
      return 

#Assigning score values, List of plays values
p1Score = 0 
p2Score = 0
shownList = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
shownList1 = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
hiddenList = ['A','A','B','B','C','C','D','D','E','E','F','F','G','G','H','H','I','I','J','J']
random.shuffle(hiddenList)

while (True) :
  if (shownList != ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']):
    #Player One Play
    welcMsg = print(f"Welcome: {shownList}")
    play1Msg = print(f"Player#1 - Score {p1Score}")
    play1 = int(float(input("")))
    play2 = int(float(input("")))

    #Checking Entered Play Valid or Not.
    if (play1 <= 20 and play2 <= 20 and play1 >= 1 and play2 >= 1 and play1 != play2 ) :
      #Assigning The Play To The Lists
        if (hiddenList[play1 - 1] == hiddenList[play2 - 1] and (shownList[play1 - 1] != '*') and (shownList[play2 - 1] != '*')):
          shownList[play1 - 1] = '*'
          shownList[play2 - 1] = '*'
          print(f"Welcome: {shownList}")
          os.system('cls')
          p1Score += 1
          check_Score(p1Score,p2Score)

        elif (hiddenList[play1 - 1] != hiddenList[play2 - 1] ) :
            if (shownList[play1 - 1] == '*') or (shownList[play2 - 1] == '*'):
              if(shownList[play1-1] == '*') :
                  shownList[(play2-1)] = hiddenList[(play2-1)]
                  print(f"Welcome: {shownList}")
                  shownList[play2-1] = shownList1[play2-1]
                  time.sleep(2)
                  os.system('cls')

              elif(shownList[play2-1] == '*') :
                  shownList[play1-1] = hiddenList[play1-1]
                  print(f"Welcome: {shownList}")
                  shownList[play1-1] = shownList1[play1-1]
                  time.sleep(2)
                  os.system('cls')

            elif (shownList[play1 - 1] != '*' and shownList[play2 - 1] != '*') :
                shownList[play1 - 1]= hiddenList[play1 - 1]
                shownList[play2 - 1] = hiddenList[play2 - 1]
                print(f"Welcome: {shownList}")
                shownList[play1 - 1] = shownList1[play1 - 1]
                shownList[play2 - 1] = shownList1[play2 - 1]
            time.sleep(2)
            os.system('cls')

    else : 
        print("Wrong Play")

    #Player 2 Play
    welcMsg = print(f"Welcome: {shownList}")
    pla2Msg = print(f"Player#2 - Score {p2Score}")
    play11 = int(input())
    play22 = int(input())

    if (play11 <= 20 and play22 <= 20 and play11 >= 1 and play22 >= 1 and play11 != play22 ) :
        if (hiddenList[play11 - 1] == hiddenList[play22 - 1]):
          shownList[play11 - 1] = '*'
          shownList[play22 - 1] = '*'
          print(f"Welcome: {shownList}")
          os.system('cls')
          p2Score += 1
          check_Score(p1Score,p2Score)

        elif (hiddenList[play11 - 1] != hiddenList[play22 - 1] ) :
            if (shownList[play11 - 1] == '*') or (shownList[play22 - 1] == '*'):
              if(shownList[play11-1] == '*') :
                  shownList[(play22-1)] = hiddenList[(play22-1)]
                  print(f"Welcome: {shownList}")
                  shownList[play22-1] = shownList1[play22-1]
                  time.sleep(2)
                  os.system('cls')

              elif(shownList[play22-1] == '*') :
                  shownList[play11-1] = hiddenList[play11-1]
                  print(f"Welcome: {shownList}")
                  shownList[play11-1] = shownList1[play11-1]
                  time.sleep(2)
                  os.system('cls')

            elif (shownList[play11 - 1] != '*' and shownList[play22 - 1] != '*' ) :
                shownList[play11 - 1]= hiddenList[play11 - 1]
                shownList[play22 - 1] = hiddenList[play22 - 1]
                print(f"Welcome: {shownList}")
                shownList[play11 - 1] = shownList1[play11 - 1]
                shownList[play22 - 1] = shownList1[play22 - 1]
            time.sleep(2)
            os.system('cls')

    else : 
        print("Wrong Play")

