"""
Reglas del juego de la vida

Regla 1: si una celula que se encuentra viva tiene 0 o un vecino muere
por soledad para la siguiente generacion. Donde los vecinos son las
8 celulas que lo rodean inmediatamente

Regla 2: Una celula viva que tienen 2 o 3 vecinos sobrevive para la siguiente
generacion

Regla 3: Una celula viva que tiene 4 o mas vecinos mueren por sobrepoblacion
para la siguiente generacion

Regla 4: Una celula muerta con exactamente con 3 vecinos vivos resulta en un
nacimiento cuya vida empieza en la siguiente generacion. Todas las
demas celular muertas permanecen muertas para la siguiente  generacion


"""
from Array2D import Array2D
class JuegoDeLaVida:
    def __init__(self,rows,cols,generaciones,poblacion_inicial):
        self.__cuadro=Array2D(rows,cols)
        self.__filas=rows
        self.__columnas=cols
        self.__generaciones=generaciones
        self.__cuadro.Clearing(0)
        for cell in poblacion_inicial: 
            self.__cuadro.set_item(cell[0],cell[1],1)
    def to_string(self):
        print(self.__cuadro.to_string())
    def configure_next_generation(self, nueva_generacion):
        self.__cuadro.Clearing(0)
        for i in nueva_generacion:
            self.__cuadro.set_item(i[0],i[1],1)
    def set_cell_death(self,row,col):
        self.__cuabro.set_item(row,col,0)
    def set_cell_alive(self,row,col):
        self.__cuabro.set_item(row,col,1)
    def is_live_cell(self,row,col):
        if self.__cuadro.get_item(row,col) == 1:
            return True
        else:
            return False
    def calcula_vecinos(self,x,y):
        vecinos=[x-1,y-1,x+1,y+1]
        if vecinos[0]==-1:
            vecinos[0]=0
        if vecinos[1]==-1:
            vecinos[1]=0
        if vecinos[3]==self.__columnas:
            vecinos[3]=self.__columnas-1
            pass
        if vecinos[2]==self.__filas:
            vecinos[2]=self.__filas-1
            pass
        return vecinos
    def get_num_vecinos_vivos(self,col,row):
        limites=self.calcula_vecinos(col,row)
        cont=0
        for x in range(limites[0],limites[2]+1,1):
            for y in range(limites[1],limites[3]+1,1):
                if self.is_live_cell(x,y):
                    if x==col and y == row:
                        pass
                    else:
                        cont+=1
        return cont
#pruebas
def main():
    inicial=[[1,3],[2,2],[2,3],[2,4],[1,1]]
    reglas=False
    while reglas != True :
        num=int(input('Digite el valor del Arreglo : '))
        if num>=5 :
            reglas=True
        else:
            print("ERROR, Ingresa un valor valido")
    numy=num
    Generacion=False
    while Generacion != True:
        num_generaciones=int(input('Digite el numero de generaciones que desea: '))
        if num_generaciones>0:
            Generacion = True
        else:
            print("Digite un numero entero para las Generaciones")	
    juego=JuegoDeLaVida(num,numy,num_generaciones,inicial)
    save_data2=[]
    for x in range(num_generaciones +1):
        print(f"Generacion: {x}")
        for r in range(num):
            for c in range(numy):
                if juego.is_live_cell(r,c):
                    if juego.get_num_vecinos_vivos(r,c) == 0 or juego.get_num_vecinos_vivos(r,c)==1 :
                        pass
                    if juego.get_num_vecinos_vivos(r,c) == 2 or juego.get_num_vecinos_vivos(r,c)==3:
                        lista=[r,c]
                        save_data2.append(lista)
                        pass
                    if juego.get_num_vecinos_vivos(r,c)>3:
                        pass
                    pass
                if juego.is_live_cell(r,c) != True: 
                    if juego.get_num_vecinos_vivos(r,c) > 2 and juego.get_num_vecinos_vivos(r,c)<4 :
                        lista=[r,c]
                        save_data2.append(lista)
                        pass
                    else:
                        pass
                    pass
                pass
            pass
        juego.to_string()
        juego.configure_next_generation(save_data2)
        for p in range(len(save_data2)):
            save_data2.pop()
            pass
        pass 

    
    
main()
