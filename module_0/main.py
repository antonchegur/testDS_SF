import numpy as np
def game_core_v3(predict, start, end):
    leftLimit = start #left limit
    rightLimit = end #right limit
    count = 1
    
    number = int((leftLimit + rightLimit)/2) #first init of number
    while number != predict:
        count+=1
        if number > predict: 
            rightLimit = number
        elif number < predict: 
            leftLimit = number
        number = int((leftLimit + rightLimit)/2)
    print (f"Вы угадали число {number} за {count} попыток.") #print the result
    return(count) #exit the loop

start = 1 #parameter for start number
end = 101 #parameter for final number

randomNumber = np.random.randint(start, end) #init of random number
print ("Загадано число от 1 до 100")
game_core_v3(randomNumber, start, end) #call our main function
