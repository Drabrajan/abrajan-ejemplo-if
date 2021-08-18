import os
def main():
    

    os.system("clear")
    #escribe tu código abajo de esta línea
    angulo = int(input("angulo en grados del triangulo: "))

    if angulo < 90:
        print("Agudo")
    elif angulo==90:
        print("Recto")
    elif (angulo > 90) and (angulo < 180):
        print("obtuso")
    elif angulo == 180:
        print("llano")
    else:
        print("concavo")

if __name__=='__main__':
    main()
