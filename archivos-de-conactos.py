import os

CARPETA = 'contactos/'  #Carpeta de contactos (constante)
EXTENSION = '.txt' #Extension de archivos (constante)

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta existe o no
    crear_directorio()
    #Muestra el menu de opciones
    mostrar_menu()
    #Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: ')
        opcion = int(opcion)
        #Ejecutar las opciones
        match(opcion):
            case 1:
                agregar_contacto()
                preguntar = False
            case 2:
                editar_contacto()
                preguntar = False
            case 3:
                mostrar_contactos()
                preguntar = False
            case 4:
                buscar_contacto()
                preguntar = False
            case 5:
                eliminar_contacto()
                preguntar = False
            case _:
                print('Opcion no valida, intente de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\nEliminado correctamente')
    except:
        print('no existe ese contacto')
    app()

def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')
    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\nInformacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('No se encontró el contacto/no existe')
        app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]
    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #imprime los contenidos 
                print(linea.rstrip())
            print('\r\n')
    app()

def editar_contacto():
    nombre_anterior = input('Escribe el nombre del contacto a editar: \r\n')
    #Revisar si el archivo ya existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:
            nombre_contacto = input('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo telefono: \r\n')
            categoria_contacto = input('Cateogria contacto: \r\n')

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')
        archivo.close()
        #Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
        print('\r\nContacto editado correctamente \r\n')
    else:
        print('Ese contacto no existe')
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del contacto: \r\n')
    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
            telefono_contacto = input('Agrega el telefono: \r\n')
            categoria_contacto = input('Categoria contacto: \r\n')

            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')
        archivo.close()
        print('\r\nContacto creado correctamente \r\n')
    else:
        print('Ese contacto ya existe')
    app()

def mostrar_menu():
    print('Seleccione del menu lo que desea hacer: \n1)Agregar nuevo contacto \n2)Editar contacto \n3)Ver contacto \n4)Buscar contacto \n5)Eliminar contacto')

def crear_directorio():
    if not os.path.exists(CARPETA): #Revisa si la carpeta existe
        os.makedirs(CARPETA) #crea la carpeta
    else:
        print('La carpeta ya existe')

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()