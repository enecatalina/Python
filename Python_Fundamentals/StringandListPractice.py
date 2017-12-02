words = "It's thanksgiving day. It's my birthday,too!"
str_new = words.replace("day", "month")
print(str_new)

x_list = [2,54,-2,7,12,98]
biggest = max(x_list)
print(biggest)
smallest = min(x_list)
print(smallest)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[7] #only for a specific list
print x[0], x[len(x) - 1] #used for any list

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
first_list = x[:len(x)/2]
second_list = x[:len(x)/2]
print first_list
print second_list
second_list.insert(0,first_list)
print second_list