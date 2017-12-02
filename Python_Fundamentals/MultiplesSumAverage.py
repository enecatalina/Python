#odd numbers from 1 -1000
for i in range(1,1000):
    if i%2 != 0:
        print i

# prints all the multiples of 5 from 5 to 1,000,000.
for i in range(5,1000000):
    if i%5 == 0:
        print i

# prints the average of the values in the list:
x = [1, 2, 5, 10, 255, 3]
print(sum(x)/len(x))


#odd numbers way #2
for count in range(1, 1001, 2):
    print count

#multiples of 5 #2
for count in range(5,1000001,5):
    print count

#average #3 part 1
my_numbers = [1, 2, 5, 10, 255, 3]
sum = 0
for i in my_numbers:
    sum += i
print sum

#average #3 part 2
print sum/len(my_numbers)