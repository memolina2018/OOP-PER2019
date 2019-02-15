class Alumno():
    def __init__(self,matricula,nombre,nota1,nota2,nota3):
        self.matricula=matricula
        self.nombre=nombre
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
    def get_matricula(self):
        return ('El numero de matricula del alumno es:',self.matricula)
    def get_nombre(self):
        return ('El alumno se llama:',self.nombre)
    def get_notafinal(self):
        media = (self.nota1+self.nota2+self.nota3)/3
        if media >= 4.8:
            return ('El alumno ha aprobado con una nota media:',media)
        elif media <= 4.8:
            return ('El alumno ha suspendido con una nota media:',media)

a = Alumno(00100,'Juan',3,8.7,6)
print(a.get_notafinal())
