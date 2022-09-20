#Game: guess a number

import numpy as np

number = np.random.randint (1,101) #guess a number

count = 0 #quantity of attempts

while True:
    count +=1
    predict_number = int (input ("guess the number from 1 to 100 "))
    
    if predict_number > number:
        print ("It must be less")
    elif predict_number < number:
        print ("It must be more")
    else:
        print (f"You guessed it,congratulations! The number is {number} in {count} tries")
        break# end of the game
