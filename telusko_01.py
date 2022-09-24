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