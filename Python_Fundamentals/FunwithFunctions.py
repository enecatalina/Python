# def print_odds():
#     for num in range(1,256):
#         if num%2 !=0:
#             print "Number is",num 
#             print "This is an odd number"
#         if num%2 == 0:
#             print "Number is",num 
#             print "This is an even number"
# print_odds()

# #multiply numbers
# my_list = [2,4,10,16]
# # def multiply(list):
# my_new_list = [i * 5 for i in my_list]
# print my_new_list

# #dojo way of multiply
# def multiply(arr, num):
#     for x in range(0, len(arr)):
#         arr[x] *= num
#     return arr
# numbers_array = [3, 6, 8, 10, 67]
# print multiply(numbers_array, 5)

# def layered_multiples(arr):
#     print arr
#     new_array = []
#     for x in arr:
#         val_arr = []
#         for i in range(0,x):
#             val_arr.append(1)
#         new_array.append(val_arr)
#     return new_array

# x = layered_multiples(multiply([2,4,5],3))
# print x