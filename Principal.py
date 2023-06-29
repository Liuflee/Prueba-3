
import functions as fn

def main():
    main_list = [[], [], [], [], [], [], [], []] #nombre. rut. fecha-nac, categoria, celular, identificador, edad, correo
    options = [
        "Grabar",
        "Buscar",
        "Mostrar Parejas",
        "Salir"
    ]

    while True:
        opc = fn.menu(options)
        if opc == 1:
            fn.add_player(main_list)
        elif opc == 2:
            fn.search_player(main_list)
        elif opc == 3:
            fn.print_pairs(main_list)
        else:
            fn.exit()
            break

main()