class empleado():
    def __init__(self,nombre,salario,puesto):
        self.nombre=nombre
        self.salario=salario
        self.puesto=puesto

    def get_info(self):
        print("Nombre del empleado:", self.nombre, "\nSalario: ", self.salario, "\nPuesto:",self.puesto)

    def despedir(self):
        self.puesto= "Ninguno"
        self.salario=0
        return print("*El empleado ha sido despedido*\n")
emp1=empleado("Jose Rodriguez",2000,"Ejecutivo")
emp1.get_info()

emp1.despedir()
emp1.get_info()
