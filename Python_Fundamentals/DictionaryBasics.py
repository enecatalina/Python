aboutme = {"Name": "Catalina", "My age is":"23","My country of birth is the":"Romania", "My favorite language":"Python"}

for key,data in aboutme.iteritems():
     print key, " = ", data

##dojo example##
# def print_dictionary_values(dic):
#     for some_key, some_value in dic.iteritems():
#         print "My" + " " + some_key + " " + "is" + " " + str(some_value)
        
#         # alternate method:
#         # concatenating variables to strings commonly done with the .format() method (can be used on any string, or variable that
#             # contains a string
        
#         #print "My {} is {}".format(some_key, some_value)
