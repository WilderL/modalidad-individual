from coordena import Coordenada
from lista import Lista
import os.path


def main():
    if os.path.isfile("data.txt"):
        listas = []
        file = open("daata.txt", "r")
        rectangulos = file.read()
        file.close()
        rectangulos = rectangulos.split("\n")
        print(rectangulos)
        for rectangulo in rectangulos:
            listas.append(rectangulo.split(","))
            print(listas)

        areas = []
        # obtencion de areas de lso triangulos
        for lista in listas:
            count_coordenadas = 0
            y = 0
            x = 0
            for coordenada in lista:
                if count_coordenadas == 0:
                    x = int(coordenada)
                elif count_coordenadas == 2:
                    x = int(coordenada) - x

                if count_coordenadas == 1:
                    y = int(coordenada)
                elif count_coordenadas == 3:
                    y = int(coordenada) - y
                count_coordenadas += 1
                if count_coordenadas == 4:
                    area = x * y
                    areas.append(area)
                    print(areas)
                    count_coordenadas = 0

        # obtener areas restantes
        for lista1 in listas:
            x = 0
            y = 0
            for lista2 in listas:
                if lista1 is lista2:
                    continue
                else:
                    # lado X izquierdo
                    if lista1[0] == lista2[0]:
                        # lado Y izquierdo
                        if lista1[1] == lista2[1]:
                            x = int(lista2[2]) - int(lista2[1])
                            y = int(lista2[3]) - int(lista2[0])
                        # lado Y derecho
                        elif lista1[1] == lista2[3]:
                            pass
                    # lado X derecho
                    elif lista1[0] == lista2[2]:
                        # lado Y izquierdo
                        if lista1[1] == lista2[1]:
                            pass
                        # lado Y derecho
                        elif lista1[1] == lista2[3]:
                            x = int(lista2[2]) - int(lista2[1])
                            y = int(lista2[3]) - int(lista2[0])

                    # lado en X inferior
                    if lista1[0] <= lista2[0] <= lista1[2]:
                        # lado en X superior
                        if lista1[0] <= lista2[2] <= lista1[2]:
                            #lado Y izquierda
                            if lista1[1] <= lista2[3] <= lista1[4]:
                                x = lista2[]
                            else:
                                pass
                        elif lista1[1] <= lista2[3] <= lista1[4]:
                            pass

                    # lado en Y
                    if lista1[0] <= lista2[2] <= lista1[1]:
                        if lista1[1] <= lista2[1] <= lista1[4]:
                            pass
                        elif lista1[1] <= lista2[3] <= lista1[4]:
                            pass

        area_total = 0
        for area in areas:
            area_total += area

        print("El area toral es:", area_total)


    else:
        print("No existe el archivo")



main()
