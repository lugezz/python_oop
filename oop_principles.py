from abc import ABC


# 1) Encapsulation

"""
To enclose something in or as if in a capsule.
"""


class Cat:

    def __init__(self):
        self.__sound = "meow"

    def speak(self):
        print("Cat says: {}".format(self.__sound))


c = Cat()
c.speak()

# change the sound
c.sound = "bow-wow"
c.speak()

# 2) Inheritance
"""
To receive a quality, characteristic, etc., from your parents or family.
"""


class Family:
    def __init__(self, family_name, number_of_members, country):
        self.family_name = family_name
        self.number_of_members = number_of_members
        self.country = country

    def member_says(self):
        print(f"Hey, I am from {self.family_name} family and there are {self.number_of_members} members in family")


class Family_detailed(Family):

    def which_country(self):
        print(f"The {self.family_name} family has roots from {self.country}")


a = Family("Rodrigues", 5, "Peru")
b = Family_detailed("Bezos", 15, "United States of America")

a.member_says()
b.member_says()
b.which_country()

# 2) Abstraction
"""
A general idea rather than one that relates to a particular object, person, or situation.

Abstract means a concept or an Idea which is not associated with any particular instance.
Using abstract class/Interface we express the intent of the class rather than the actual implementation.
In a way, one class shouldn't know the inner details of another to use it, just knowing the interfaces should be enough.
"""


class Company(ABC):

    def work(self):
        pass


class Manager(Company):

    def work(self):
        print("I assign work to and manage team")


class Employee(Company):

    def work(self):
        print("I complete the work assigned to me")


# Driver code
R = Manager()
R.work()

K = Employee()
K.work()


# 4) Polymorphism
"""
The condition of occurrence in several different forms.
"""


class Class1():
    def pt(self):
        print("This function determines class 1")


class Class2():
    def pt(self):
        print("This function determines class 2.")


obj1 = Class1()
obj2 = Class2()
for type in (obj1, obj2):  # Creating a loop to iterate through the obj1, obj2
    type.pt()
