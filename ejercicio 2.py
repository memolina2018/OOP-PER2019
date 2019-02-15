class contador():
    def __init__(self,numero):
        self.numero=numero
        
    def incrementar(self):
        incremento=self.numero + 1
        self.numero=incremento
        return self.numero
    def reducir(self):
        incremento=self.numero - 1
        self.numero=incremento
        return self.numero
    
    def get_numero(self):
        get_numero=self.numero
        return get_numero
    
uno=contador(1)
print("si le sumo una unidad a", uno.get_numero(),"obtengo:",uno.incrementar())
print("el nuevo contador, adquiere el valor de", uno.get_numero(),"y si lo reducimos en una unidad, se queda como ", uno.reducir())

    
