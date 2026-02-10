# #class student:
#     def __init__(self, name):
#         self.name = name

# s1 = student("john")
# print(s1.name) #delete nahi  hoga kuki s1 ke pass name attribute hai 
# del s1 
# print(s1.name) #error aayega kuki s1 delete ho chuka hai 





# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass

# acc = account(12345, "john123")
# print(acc.acc_no)
# print(acc.acc_pass)







# class person:
#     __name = "john"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()    

# p1 = person()
        
# print(p1.welcome())




# class car:
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class toyato(car):
#     def __init__(self, name):
#         self.name = name

# car1 = toyato("fortuner")            
# car2 = toyato("innova")

# print(car1.start())



class student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((phy + chem + maths) / 3) + "%"

    def calculate_percentage(self):
        self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

stu1 = student(80, 90, 85)
print(stu1.percentage)

stu1.phy = 85
print(stu1.phy)
stu1.calculate_percentage()
print(stu1.percentage)



    