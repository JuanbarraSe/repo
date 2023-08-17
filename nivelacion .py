print("Bienvenido a " )
print("""   
                   ###                                  ##      ###      ###
  #####    ####      ##      ####             ##  ##              ##       ##      ####     #####
 ##       ##  ##     ##     ##  ##            ######    ###       ##       ##     ##  ##   ##
  ####    ##  ##     ##     ##  ##            ######     ##       ##       ##     ##  ##    ####
     ##   ##  ##     ##     ##  ##            ##  ##     ##       ##       ##     ##  ##       ##
 #####     ####     ####     ####    04       ##  ##    ####     ####     ####     ####    #####


""")
#solicitar nombre

nombre = input("Por favor ingresa tu nombre: ")

print("Hola ", nombre, ", bienvenido a SOLO MILLOS.")
print()
#calcular la edad
años = int(input("Para crear tu perfil, por favor ingresa en que año naciste  "))
fecha_actual=2023
edad = fecha_actual - años 
print("Tu edad es:", edad) 
#ciudad
ciudad = input("En que ciudad vives: ")
print("Tu ciudad es", ciudad,)
#para terminar escribir los datos recolectados
print("Gracias,", nombre, ". ahora crearemos un perfil con tus datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("ciudad: ", ciudad)
print("Gracias por tu informacion,  que  disfrutes de SOLO MILLOS ")
mensaje = input("Ahora puedes escribir tu primer mensaje. ¿como estas hoy?")
print("--------------------------------------------------")
print(nombre, "gracias por contarnos mas de ti")
print("--------------------------------------------------")
print("bien ahora   queremos saber mas de ti")
barrio = input(" ¿en que barrio vives?: ")
print("Tu barrio es:", barrio)
sexo = input(" Por favor ingresa tu sexo")
print("tu sexo es  :", sexo)
millos = input("¿apoyas a millos?: ")
print("apoyas a millos:", millos )
pais = input("ingrese su pais de nacimiento: ")
print("Tu pais de nacimiento es", pais,)
amigo= (input ("ahora queremos que nos recomiendes a un amigo o familiar, ingresa un correo electronico:  "))
print("gracias por recomendarnos a un familiar o amigo =)", )
def mostrar_menu():
    print("______menu____")
    print("1. opcion 1")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4. opcion 4")
    
    opcion = 0

    while opcion != 4:
        mostrar_menu()
    opcion =int(input("ingrese el numero de la opcion que desea: "))
    if opcion == 1:
         print("Has elegido la opcion 1. ")
    elif opcion == 2:
         print("Has elegido la opcion 2: ")
    elif opcion == 3:
         print("Has elegido la opcion 3. ") 
    elif opcion == 4:
         print("saliendo del menu...")    
    else:
         print("opcion invalida por favo eliga una opcion valida.")

print("GRACIAS POR ESTAR EN")
print("""###                                  ##  ##   ###      ###
  #####    ####      ##      ####             ##  ##              ##       ##      ####     #####
 ##       ##  ##     ##     ##  ##            ######    ###       ##       ##     ##  ##   ##
  ####    ##  ##     ##     ##  ##            ######     ##       ##       ##     ##  ##    ####
     ##   ##  ##     ##     ##  ##            ##  ##     ##       ##       ##     ##  ##       ##
 #####     ####     ####     ####    04       ##  ##    ####     ####     ####     ####    #####

""")
print(" adios, que tengas un lindo dia ")
