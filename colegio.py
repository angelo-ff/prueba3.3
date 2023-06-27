import funciones as fun


while True:
    fun.limpiar_pantalla()

    fun.printa("Colegio San Charlis" )

    fun.titulo("MATRICULA DE ALUMNOS ")
    print("1) MATRICULAR ALUMNO")
    print("2) BUSCAR ALUMNO")
    print("3) CERTIFICADO  ALUMNO")
    print("0) SALIR")    

    opcion = int(input("Seleccione : "))

    if opcion == 0:
        break
    elif opcion >=1 and opcion <=3:
        if opcion == 1:
            fun.titulo("MATRICULACION DE  ALUMNO")
            rut = int(input("Ingrese rut del alumno sin guion y puntos \nSi termina en k seleccione 0: "))
            pnombre = input("Ingrese primer nombre  del alumno : ").capitalize()
            while len(pnombre) <3:
                pnombre = input("Nombre muy corto minimo 3 caracteres : ")
            snombre = input("Ingrese segundo nombre  del alumno : ").capitalize()
            while len(snombre) <3:
                snombre = input("Nombre muy corto minimo 3 caracteres : ")
            appaterno = input("Ingrese primer apellido   del alumno : ").capitalize()
            while len(appaterno) <3:
                appaterno = input("Nombre muy corto minimo 3 caracteres : ")
            apmaterno = input("Ingrese segundo apellido  del alumno : ").capitalize()
            while len(apmaterno) <3:
                apmaterno = input("Nombre muy corto minimo 3 caracteres : ")
            nombre =(f"{pnombre},{snombre},{appaterno},{apmaterno}")
            edad = int(input("Ingrese la edad del alumno : "))
            genero = input("Ingrese genero del alumno \n(F/M) : ").upper()
            promedio_notas = float(input("Ingrese el promedio del alumno : "))
            fecha_matricula = input("Ingrese fecha de matricula : ")
            nombre_apoderado = input("Ingrese nombre del apoderado : ")
            fun.guardar_alumno(rut, nombre, edad, genero, promedio_notas, fecha_matricula, nombre_apoderado)

        elif opcion == 2:
            fun.titulo("Buscar alumno")
            rut = int(input("Ingrese rut : "))
            fun.buscar_alumno(rut)
        elif opcion == 3:
            fun.titulo("CERTIFICADOS")
            print("1) certificado de anotaciones")
            print("2) certificado de notas")
            print("3) certificado de alumno regular")
            opcion = int(input("Seleccione : "))
            if opcion == 1:
                rut = int(input("Ingrese rut : "))
                fun.anotaciones(rut)
            elif opcion == 2:
                rut = int(input("Ingrese rut : "))
                fun.notas(rut)
            elif opcion == 3:
                rut = int(input("Ingrese rut : "))
                fun.alumno_regular    
        else:
            fun.printr("Opcion no valida")



