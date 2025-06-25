'''
Programa: Sistema de bibliotecas.
Utilizar la lista de usuarios y personas definidas a continuación.
El programa debe mostrar un menú que permita:
1 - Buscar un usuario por su rut.
    1.1 - Si el usuario existe mostrar un menú para:
        1.1.1 - Realizar un préstamo de un libro, sólo si hay disponibles.
        1.1.2 - Realizar la devolución de un libro
            1.1.2.1 - Si el libro no existe, permitir registrar el libro que trajo la persona.
    1.2  - Si el usuario no existe, permitir registrar al usuario.
2 - Registrar un nuevo usuario.
3 - Registrar un nuevo libro.
4 - Salir

Debe hacer una función para:
1 - Buscar usuarios
2 - Registrar un usuario
3 - Registrar un libro

Debe usar try-except para verificar todos los posibles códigos peligrosos.
Debe usar mensajes amigables y coherentes con un programa pensado para el encargado de la 
biblioteca. Bien escritos y redactados, puede ayudarse de Chat GPT para esto.
'''

def buscar_usuario(rut):
    usuario_existente = False
    for usuario in usuarios:
        if usuario["rut"] == rut:
            usuario_existente = True
            return True
    return False

def buscar_libro(rut, titulo):
    for usuario in usuarios:
        if usuario["rut"] == rut:
            for libro in libros:
                if libro["titulo"].lower() == titulo.lower():
                    libro["cantidad_disponible"] = libro["cantidad_disponible"] - 1
                    usuario["libros"].append(libro["id"])
                    return True
            return False
    
def devolucion_libro(rut, titulo):
    for usuario in usuarios:
        if usuario["rut"] == rut:
            for libro in libros:
                if libro["titulo"].lower() == titulo.lower():
                    if libro["id"] in usuario["libros"]:
                            libro["cantidad_disponible"] = libro["cantidad_disponible"] + 1
                            usuario["libros"].remove(libro["id"])
                            return True
                    else:
                        print(f"El libro \"{titulo}\" no esta al nombre del usuario")
                        return False
            print(f"El Libro \"{titulo}\" no esta en los registro.")
            return False
        
def Registrar_un_usuario(nombre, apellido, rut):
    for usuario in usuarios:
        if usuario["rut"] == rut:
            print("Usuario ya registrado.")
            return False
    usuarios.append({"nombre": nombre, "apellido": apellido, "rut": rut, "libro": []})
    return True
def Registrar_un_libro(titulo, autor, isbn, paginas, cantidad_disponible):
    id = 0
    for libro in libros:
        id += 1
        if libro["titulo"].lower() == titulo.lower():
            print("El libro ya esta registrado, No se puede sobreescribir.")
            return False
    libros.append({"id": id+1, "titulo": titulo, "autor": autor, "ISBN": isbn, "paginas": paginas, "cantidad_disponible": cantidad_disponible})
    return True


usuarios = [
    {"nombre": "Ana", "apellido": "González", "rut": "13816108-7", "libros": []},
    {"nombre": "Luis", "apellido": "Rodríguez", "rut": "13872719-2", "libros": []},
    {"nombre": "Camila", "apellido": "Pérez", "rut": "12182343-5", "libros": []},
    {"nombre": "Jorge", "apellido": "Muñoz", "rut": "14044461-9", "libros": []},
    {"nombre": "María", "apellido": "Rojas", "rut": "16149391-0", "libros": []},
    {"nombre": "Diego", "apellido": "Díaz", "rut": "10407062-4", "libros": [0]},
    {"nombre": "Lucía", "apellido": "Soto", "rut": "19306158-3", "libros": []},
    {"nombre": "Pablo", "apellido": "Torres", "rut": "14864522-5", "libros": []},
    {"nombre": "Valentina", "apellido": "Contreras", "rut": "15592214-1", "libros": []},
    {"nombre": "Tomás", "apellido": "Silva", "rut": "10516040-5", "libros": []}
]

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "ISBN": "978-0307474728", "paginas": 432, "cantidad_disponible": 5},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ISBN": "978-0451524935", "paginas": 328, "cantidad_disponible": 3},
    {"id": 3, "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "ISBN": "978-1451673319", "paginas": 194, "cantidad_disponible": 7},
    {"id": 4, "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "ISBN": "978-0060934347", "paginas": 992, "cantidad_disponible": 2},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "ISBN": "978-1400034956", "paginas": 128, "cantidad_disponible": 4},
    {"id": 6, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "ISBN": "978-0156013987", "paginas": 96, "cantidad_disponible": 10},
    {"id": 7, "titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "ISBN": "978-0156007757", "paginas": 352, "cantidad_disponible": 3},
    {"id": 8, "titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "ISBN": "978-0143034902", "paginas": 512, "cantidad_disponible": 6},
    {"id": 9, "titulo": "El túnel", "autor": "Ernesto Sabato", "ISBN": "978-9500420305", "paginas": 160, "cantidad_disponible": 2},
    {"id": 10, "titulo": "Pedro Páramo", "autor": "Juan Rulfo", "ISBN": "978-6073142360", "paginas": 144, "cantidad_disponible": 8}
]

while True:
    print("""\n****Menu De Opciones****
1. Buscar un usuario por su rut.
2. Registrar un nuevo usuario.
3. Registrar un nuevo libro.
4. Salir.
    """)
    try:
        opcion = 0
        opcion = int(input("Escoja una opcion (1-4): "))
    except ValueError as error:
        print("Caracter no valido.")
        print(error)
  
    if opcion == 1:
        rut = input("Inserte el rut a buscar (12345678-0): ")
        if buscar_usuario(rut):
            while True:
                print("""\n*** Menu de Opciones *** 
1. Realizar Prestamo de un libro.
2. Realizar Devolucion de un libro.
3. Atras.
            """)
                try:
                    sub_opcion = 0
                    sub_opcion = int(input("escoja una opcion (1-3): "))
                except ValueError as error:
                    print(error)
                    print("Caracter no valido")
                
                if sub_opcion == 1:
                    titulo = input("Inserte el titulo del libro que desea pedir: ")
                    if buscar_libro(rut, titulo):
                        print("Libro prestado exitosamente.")
                    else:
                        print(f"El libro \"{titulo}\" no esta en el registro.")
                elif sub_opcion == 2:
                    titulo = input("Inserte el titulo del libro a devolver: ")
                    if devolucion_libro(rut, titulo):
                        print("Libro devuelto exitosamente")
                    else:
                        print("El libro no se puede devolver.")
                elif sub_opcion == 3:
                    break
        else:
            print(f"El Rut \"{rut}\" no esta registrado")
    elif opcion == 2:
        nombre = input("Inserte el nombre del usuario a registrar: ").capitalize()
        apellido = input("Inserte el apellido del usuario a registrar: ").capitalize()
        rut = input("Inserte el rut del usuario a registrar (12345678-0): ")
        if Registrar_un_usuario(nombre, apellido, rut):
            print("Usuario registrado.")
        else:
            print("No se pudo registar el usuario.")

    elif opcion == 3:
        try:
            titulo = input("Inserte el titulo del libro a registrar: ")
            autor = input("Inserte el autor del libro a registrar: ")
            isbn = input("Inserte el ISBN del libro a registrar: ")
            paginas = int(input("Inserte la cantidad de paginas del libro a registrar: "))
            cantidad_disponible = int(input("Inserte la cantidad de libro disponibles a registrar: "))
            if cantidad_disponible >= 1 and paginas >= 1:
                if Registrar_un_libro(titulo, autor, isbn, paginas, cantidad_disponible):
                    print(f"El libro \"{titulo}\" fue registrado.")
                else:
                    print(f"El libro \"{titulo}\" no se pudo registar.")
            else:
                print("Los valores no pueden ser negativos.")
        except ValueError as error:
            print("Caracter no valido.")
            print(error)

    elif opcion == 5:
        print(libros)
    
    elif opcion == 6:
        print(usuarios)
         
    else:
        print("Opcion no valida, intentelo de nuevo.")

    for usuario in usuarios:
        print(usuario["nombre"])