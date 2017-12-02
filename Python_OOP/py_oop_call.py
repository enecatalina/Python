class Call(object):
    id = 1
    def __init__(self, caller, phonenumber, time, reason):
        self.id = Call.id
        self.caller = caller
        self.phonenumber = phonenumber
        self.time = time
        self.reason = reason
        Call.id += 1
        
    
    def display_info(self):
        print 'unique id' + str(self.id)
        print 'caller name' + self.caller
        print 'phone number' + str(self.phonenumber)
        print 'Time of call' + str(self.time)
        print 'reason for call' + self.reason
        # return self
    
call1 = Call("Cat",56179081,12,"cold")

# class Callcenter(object):

#     def __init__():
#         self.calls = []
#         self.queue_size = 0

#     def add(self, caller, phonenumber, time, reason):
#         Call(caller, phonenumber, time, reason)
#         Call.appead(self.calls)
#         # print 'word'
#         return self

#     def remove(self):
#         self.calls.pop(0)
#         return self
    
#     def info(self):
#         print 'Unique ID' + self.id
#         print 'name ' + self.caller
#         print 'phone number' + self.phonenumber
#         print 'Queue number' + len(self.queue_size)
#         return self

# call1 = Callcenter('JI', 21390-59166, 15,'EMERGENCY')
# call1.info()




    




    
