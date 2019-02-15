class Libro():
    def __init__(self,nombre,sinopsis,date,estado):
        self.nombre=nombre
        self.sinopsis=sinopsis
        self.date=date
        self.estado=estado
        
    def prestamo(self):
        prestamo=self.estado
        print("Actualmente, el libro se encuentra",prestamo)
        return prestamo

    def dame_info(self):
        dame_nombre=self.nombre
        dame_sinopsis=self.sinopsis
        dame_date=self.date
        return print("El libro", dame_nombre,"publicado en", dame_date,"trata sobre: ", dame_sinopsis)
    
Harry_potter=Libro("Harry Potter","Un niño mago y sus aventuras","1999","prestado")

Harry_potter.prestamo()
Harry_potter.dame_info()
