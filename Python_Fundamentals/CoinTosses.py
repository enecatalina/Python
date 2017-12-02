import random 

heads = 0
tails = 0
flip_count = 0

while flip_count < 5000:
    coin = random.randint(1,2)
    if coin == 1:
        print("Throwing a coin...It's a Head")
        heads += 1
        flip_count += 1
    elif coin == 2:
        print("Throwing a coin...It's a Tails")
        tails += 1
        flip_count += 1
    print("Got" + str(heads) +  " heads so far and " + str(tails) + " tails so far!")