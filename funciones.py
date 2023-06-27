import msvcrt
import os
import numpy
import random
from colorama import Fore, Style


alumno = numpy.empty([10,7], object)

def printa(texto):
    print(f"{Fore.YELLOW} {Style.DIM} {texto} {Style.RESET_ALL} {Fore.RESET}")

def printv(texto):
    print(f"{Fore.GREEN} {Style.DIM} {texto} {Style.RESET_ALL} {Fore.RESET}")

def printr(texto):
    print(f"{Fore.RED} {Style.DIM} {texto} {Style.RESET_ALL} {Fore.RESET}")

def limpiar_pantalla():
    printa("<<PRESIONE UNA TECLA PARA CONTINUAR>>")
    msvcrt.getch()
    os.system('cls')

def titulo (texto):
    print(f"""
    {Fore.MAGENTA} *****************************
    {Style.BRIGHT}   {texto}   {Style.RESET_ALL}  
     ***************************** 
    """)

def validar_rut (rut):
    for i in range(10):
        if alumno[i,0] == rut:
            return 1
    return -1

def guardar_alumno(rut, nombre, edad, genero, promedio_notas, fecha_matricula, nombre_apoderado):
    if None in alumno:
        if validar_rut(rut) == -1:
            if rut >= 111111111 and rut <= 999999999: 
                if len(nombre) >=2 and len(nombre) <= 30:
                    if edad >=4 and edad <=17:
                        if genero == "M" or genero == "F":
                            if promedio_notas >= 4.5 and promedio_notas <= 7:
                                if len(nombre_apoderado) >=3:
                                    for i in range(10):
                                        if alumno[i,0] == None:
                                            alumno[i,0] = rut
                                            alumno[i,1] = nombre.capitalize()
                                            alumno[i,2] = edad
                                            alumno[i,3] = genero.upper()
                                            alumno[i,4] = promedio_notas
                                            alumno[i,5] = fecha_matricula
                                            alumno[i,6] = nombre_apoderado
                                            break
                                else:
                                    printr("el nombre de apoderado debe tener a lo menos 3 caracteres o mas ")
                            else:
                                printr("El promedio debe ser mayor a 4.5")
                        else:
                            printr("Genero ingresado no valido")
                    else:
                        printr("La edad debe ser mayor o igual a 4")
                else:
                    printr("El nombre debe tener a lo menos 2 caracteres \n max 30 caracteres")
            else:
                printr("Rut invalido")
        else:       
            printr("Este rut ya esta ingresado")
    else:
        printr("No hay espacio")


def buscar_alumno(rut):
    for i in range(10):
        if validar_rut(rut) == 1:
            printv("Rut de alumno encontrado")
            print(f"{i + 1} .- rut:{alumno[i,0]}, nombre:{alumno[i,1]}, edad:{alumno[i,2]}, genero:{alumno[i,3]}, promedio:{alumno[i,4]}, fecha de matricula:{alumno[i,5]}, apoderado:{alumno[i,6]}")
            break
        else:
            printr("ALUMNO NO ENCONTRADO")    
            break

anotaciones = []

anotaciones.append("alumno responsable ")
anotaciones.append("alumno Se porta mal en clase ")
anotaciones.append("alumno no responde ")
notas = []
notas.append("1.5")
notas.append("5")
notas.append("6")
notas.append("7")
alumno_regular = []
alumno_regular.append("Este alumno acredita que es alumno regular en el Colegio San Charlis")

def anotaciones (rut):
    rut = validar_rut(rut)

    if rut >= 0:
        print(f"""
        ---------------------------------
        Certificado de anotaciones 
        RUT: {alumno[rut,0]}
        NOMBRE ALUMNO: {alumno[rut,1]}
        ---------------------------------
        anotacion 1 = {anotaciones[random.randint(0,3)]}
        anotacion 2 = {anotaciones[random.randint(0,3)]}
        anotacion 3 = {anotaciones[random.randint(0,3)]}
        ---------------------------------
        """)    
    else:
        printr("ESTE ALUMNO NO EXISTE")

def notas (rut):
    rut = validar_rut(rut)

    if rut >= 0:
        print(f"""
        ---------------------------------
        Certificado de anotaciones 
        RUT: {alumno[rut,0]}
        NOMBRE ALUMNO: {alumno[rut,1]}
        ---------------------------------
        nota 1 = {notas[random.randint(0,4)]}
        nota 2 = {notas[random.randint(0,4)]}
        nota 3 = {notas[random.randint(0,4)]}
        ---------------------------------
        """)    
    else:
        printr("ESTE ALUMNO NO EXISTE")

def alumno_regular (rut):

    rut = validar_rut(rut)

    if rut >= 0:
        print(f"""
        ---------------------------------
        Certificado de anotaciones 
        RUT: {alumno[rut,0]}
        NOMBRE ALUMNO: {alumno[rut,1]}
        ---------------------------------
        alumno regular : {alumno_regular}
        ---------------------------------
        """)    
    else:
        printr("ESTE ALUMNO NO EXISTE")


#: Rut, nombre completo, edad, género, promedio de notas, fecha matricula y nombre del apoderado.