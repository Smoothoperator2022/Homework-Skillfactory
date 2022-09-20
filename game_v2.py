# Computer guesses the number and conjectures it ***

import numpy as np

def random_predict (number: int = 1) -> int:
    """_Randomly guesses the number_
    Args:
        number (int, optional): _riddled number_. Default to 1
    Returns:
        int: _Quantity of tries_
    """
    count = 0
    
    while True:
        count +=1
        predict_number = new_func()
        if number == predict_number:
            break
    return count

def new_func():
    predict_number = np.random.randint (1,101) #supposed number
    return predict_number

print (f"Quantity of tries:{random_predict()}")

def score_game (random_predict) -> int:
    """For how many attempts in average from 1000 tries it will guess our algorythm
     
    Args:
        random_predict ([type]): guess function.
    Returns:
        int: _Quantity of tries in average_
    """
    count_list = [] # list for saving quantity of terms
    np.random.seed (1) #fixing seed for replay
    random_array = np.random.randint (1,101, size =(1000)) # guess list of numbers
    
    for number in random_array:
        count_list.append (random_predict (number))
    
    score = int (np.mean (count_list)) #find quantity of tries in average
    print (f'Your algorythm guess the number in average for: {score} tries')
    return score

#RUN

if __name__=='__main__':
    score_game(random_predict)


#random_array = np.random.randint (1,101, size =(1000))
#count_list = []
#for number in random_array:
#        count_list.append (random_predict (number))
#print (random_array)
#print (count_list)