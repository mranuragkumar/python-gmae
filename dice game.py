

import random
import time

roll_again = "yes"
count=0
while roll_again == "yes" or roll_again == "y" or roll_again == "Y" or roll_again == "Yes" or roll_again == "YES" :
    print("\nRolling the dice...")
    time.sleep(0.6)

    dice1 = int(input("Enter Your Prediction : "))
    dice2 = random.randint(1,6)

    print("\nThe values are : ")
    print("User = ",dice1,"\nDice = ",dice2)

    if dice1 == dice2 :
        print(("YOU WON !"))
        count += 5
        print(" SCORE : ", count)

    else:
        print("YOU LOSE !\nKEEP TRYING !")
        print("SCORE : ", count)
    roll_again = input("\nPLAY AGAIN ! (Y/N) ")

print("\nTOTAL SCORE : ",count)
