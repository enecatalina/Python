import random
for x in range(50):  
    random_num = random.randint(60,100)
    if random_num >= 60 and random_num <=69:
        message = "Your grade is a D"
    elif random_num <= 79:
        message= "Your grade is a C"
    elif random_num <= 89:
        message = "Your grade is a B "
    else:
        message = "Your grade is a A"
    print message
    