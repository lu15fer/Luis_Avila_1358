import xlrd

from Array3D import Array3D

def main():
    
    A3 = Array3D(35,14,35)
    print("Bienvenido, aqui podras consultar la precipitacion de 1985 a 2019...")
    for anio in range(1985,2020,1):
        for i in range(35):
            for j in range(14):
                #print(anio)
                path = "./Precipitacion/" + str(anio)+"Precip.xls"
                #print(path)
                archivo = xlrd.open_workbook(filename = path)
                hoja= archivo.sheet_by_index(0)
                #Aguascalientes,enero de todos los años
                #print(hoja.cell_value(2,1))
                A3.set_item(i,j,anio-1985,hoja.cell_value(i,j))
        pass
    exit=False
    back_menuprinci=False
    back_menu=False
    Anio=None
    mes=None
    estado=None
    while exit !=True:
        anio=None
        anio=int(input("Selecciona un año de 1985 a 2019 o 0 para salir: "))
        if anio >= 1984 and anio <= 2020:
            while back_menuprinci!=True:
                estado=None
                print("Selecciona el estado o 0 para regresar:")
                for i in range(A3.get_num_rows()-2):
                    print(f"{i+1}) {A3.get_item(i+2,0,anio-1985)}")
                    pass
                estado=int(input("Opcion: "))
                if estado>=1 and estado<=33:
                    while back_menu!=True:
                        print("Selecciona un mes o 0 para regresar:")
                        for i in range(A3.get_num_cols()-1):
                            print(f"{i+1} {A3.get_item(1,i+1,anio-1985)}")
                            pass
                        mes=int(input("Opcion: "))
                        if mes>=1 and mes<=13:
                            print(f"La precipitacion fue: {A3.get_item(estado+1,mes,anio-1985)}")
                            print("\n")
                            back_menu=True
                            back_menuprinci=True
                            pass
                        elif mes==0:
                            back_menu=True
                            pass
                        else:
                            print("opcion equivocada")
                            pass
                        pass
                    back_menu=False
                    pass
                elif estado==0:
                    back_menuprinci=True
                    pass
                else:
                    print("Estado incorrecto")
                    pass
                pass
            back_menuprinci=False
            pass
        
        elif anio==0:
            print("fin del Programa")
            exit=True
            pass
        
        else:
            print("Año incorrecto")
            pass
        
        pass

main()

