class OutOfRange(Exception):
    def __init__(self, message):
        self.message = message


def validation(data_type, mensaje, min=0, max=float("inf"), flag = True):
    while True:
        try:
            num = data_type(input(mensaje))
            if flag:
                if min <= num <= max:
                    break
                else:
                    raise OutOfRange(f"Ingrese un numero entre {min} y {max}")
            else:
                if len(str(num)) == 8:
                    break
                else:
                    raise OutOfRange("Ingrese un rut valido")
        except ValueError:
            print(f"Error: Ingrese un numero {data_type.__name__}")
        except OutOfRange as e:
            print("Error", e)
    return num

def category_validation():
    while True:
        try:
            category = input("Ingrese la categoría: ")
            if category.lower() in ("oro", "plata", "bronce"):
                break
            else:
                OutOfRange("Ingrese una categoría valida")
        except OutOfRange as e:
            print("Error", e)
    return category
        
def string_validation(flag):
    while True:
        if flag:
            string = input("Ingrese el mail del participante: ")
            if len(string) > 6:
                if "@" not in string:
                    print("El mail debe contener un @")
                elif "." not in string:
                    print("El mail debe contener un punto")
                else:
                    break
            else:
                print("El mail debe tener mas de 6 digitos")
        else:
            string = input("Ingrese el fono del participante: ")
            if len(string) == 9:
                break
            else:
                print("El numero de telefono debe tener 9 digitos")
    return string

def validation_pairs(main_list):
    while True:
        pair_num = input("Ingrese el nombre del equipo: ")
        break
    return pair_num      
    
def input_string(mensaje, flag):
    while True:
        string = input(mensaje)
        if string != "":
            if flag:
                if len(string) >= 2:
                    break
                else:
                    print(f"Ingrese un nombre con longitud mayor a 2 ")
            else:
                break
        else:
            print("No puede dejar el campo vacio")
    return string
       
def add_player(main_list):
    name = input_string("Ingrese el nombre del participante: ", True)
    rut = validation(int, "Ingrese el rut del participante (sin dv): ", flag=False)
    date = input_string("Ingrese la fecha de nacimiento: ", False)
    category = category_validation()
    phone = string_validation(False)
    pairs = validation_pairs(main_list)
    age = validation(int, "Ingrese la edad del participante: ", max=80)
    mail = string_validation(True)
    main_list[0].append(name)
    main_list[1].append(rut)
    main_list[2].append(date)
    main_list[3].append(category)
    main_list[4].append(phone)
    main_list[5].append(pairs)
    main_list[6].append(age)
    main_list[7].append(mail)
    print("Participante registrado con exito")


def search_player(main_list):
    while True:
        rut = validation(int, "Ingrese el rut del participante (sin dv)", flag=False)
        if rut in main_list[1]:
            index = main_list[1].index(rut)
            print(f"Participante: {rut}")
            print(f"Nombre: {main_list[0][index]}")
            print(f"Categoría: {main_list[3][index]}")
            print(f"Fono: {main_list[4][index]}")
            print(f"Correo: {main_list[7][index]}")
            break
        else:
            print("El rut no existe dentro de la lista de participantes")

def print_pairs(main_list):
    cont=[]
    pairs = input("Ingrese el nombre de la pareja a buscar: ")
    for i in range(len(main_list[5])):
        if pairs == main_list[5][i]:
            cont.append[i]
    print(f"Equipo: {pairs}")
    print(f"Participante 1: {main_list[5][cont[0]]}")
    print(f"Participante 1: {main_list[5][cont[1]]}")


def exit():
    print("Adiós, Anette Villalón")

def menu(options):
    print("Menú")
    print("-" * 50)
    for i, j in enumerate(options):
        print(f"{i + 1}   -  {j} ")
    chosen_option = validation(int, "Elija una opción: ", 1, len(options))
    return chosen_option