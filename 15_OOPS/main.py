name = "Sumit"
age = 19

class student:
    name = "Amit"
    age = 18

    def about(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

#----------- step 1 --------------#

# student.about()





#----------- step 2 --------------#

# d = student().about()


class Details:
    def __init__(self, animal):
        self.animal = animal
        self.age = age

    def about(self):
        print("Hello", self.animal, self.age)

d = Details("Lion")
d.age = 20
d.about()

# print(d.animal, "belongs to the", d.group, "group.")

