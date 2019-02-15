class Fecha():
    def __init__(self,dia,mes,anno):
        self.dia=dia
        self.mes=mes
        self.anno=anno
    def comprobarFecha(self):
        if 0<=self.anno<=2019:
            continue
        else:
            print('Modifique el anno')
        meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Octubre','Noviembre','Diciembre']
        if self.mes in meses:
            if self.mes != 'Febrero':
                if self.mes == meses[0] or self.mes == meses[2] or self.mes == meses[4] or self.mes == meses[6] or self.mes == meses[7] or self.mes == meses[9] or self.mes == meses[11]:
                    if 1<=self.dia<=31:
                        continue
                    else:
                        print('Dia erroneo')
                if self.mes == meses[3] or self.mes == meses[5] or self.mes == meses[8] or self.mes == meses[10]:
                     if 1<=self.dia<=30:
                         continue
                     else:
                         print('Dia erroneo')
             if self.mes == 'Febrero':
                 if 1<=self.dia<=28:
                     continue
                 else:
                     print('Dia erroneo')
        return

     def sumarDia(self):
         return ('Mañana será:',self.dia+1)

f = Fecha(8,'Marzo',2000)
print(f.comprobarFecha())
print(f.sumarDia())
