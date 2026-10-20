pila = []
while True:
    print("\n--- Menú de Pilas ---")
    print("1. Insertar en pila")
    print("2. Borrar en pila")
    print("3. Listar pila")
    print("4. Salir")
            
    opcion = input("Elige una opción: ")
            
    if opcion == '1':
        try:
            num = int(input("Ingresa un número: "))
            pila.append(num)
            print(f"Número {num} agregado a la pila.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            
    elif opcion == '2':
        if len(pila) > 0:
            eliminado = pila.pop() 
            print(f"Último elemento ({eliminado}) borrado de la pila.")
        else:
            print("No se puede borrar, la pila está vacía.")
            
    elif opcion == '3':
        print("Elementos en la pila actual:", pila)
                
    elif opcion == '4':
        print("Saliendo del programa...")
        break
                
    else:
        print("Opción no válida. Intenta de nuevo.")