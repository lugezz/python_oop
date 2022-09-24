# Clases -----------------------------
class Computer:
    def __init__(self, cpu, ram): #Para inicializar los atributos (variables)
        print ('In init') #Este método se ejecuta solo
        self.cpu = cpu
        self.ram = ram

    def config (self):
        print (f'Config is CPU: {self.cpu}, RAM: {self.ram}')

com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)
print (type(com1))

#Computer.config() no se puede usar desde clase, sino del objeto com1
com1.config()
com2.config()

print ('-'* 90)
#------------
class Computer2:
    def __init__(self):
        self.name = "Navin"
        self.age = 30
    
    def update (self):
        self.age = 32

    def compare (self, other):
        return self.age == other.age

    def __str__(self):
        return str(self.age)

c1 = Computer2()
c2 = Computer2()

if c1.compare (c2):
    print ('They are the same')

c1.name = 'Artime'
c1.age = 40

print (c1.name, c1.age)
print (c2.name, c2.age)

print (c1)

print ('-'*90)

#---------------------
class Car:
    wheels = 4


    def __init__(self):
        self.mil = 10
        self.com = "BMW"

car1 = Car()
car2 = Car()

car1.mil = 8

print (car1.mil, car1.com, car1.wheels)
print (car2.mil, car2.com)
print (Car.wheels) # Se puede imprimir porque es una variable de clase
print ('-'*90)

# -------------------------
class Student:
    school = 'Telusko'

    def __init__(self, m1, m2, m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def average (self):
        return (self.m1 + self.m2 + self.m3) / 3

    def getM1(self):
        return self.m1

    def setM1 (self, value):
        self.m1 = value
    
    # Class method
    @classmethod
    def getSchool(cls):
        return cls.school

    #Static method
    def info ():
        print ('You are a student')

s1 = Student (22, 33, 44)
s2 = Student (12, 13, 14)

print (s1.average())
print (s2.average())

print (s1.getM1())

s1.setM1(84)
s2.setM1(84)

print (s1.getM1())
print (s2.getM1())

print(Student.getSchool())

Student.info()