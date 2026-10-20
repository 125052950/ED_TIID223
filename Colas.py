from collections import deque
cola = deque()
        
while True:
    print("\n--- Menú de Colas ---")
    print("1. Insertar cola")
    print("2. Borrar en cola")
    print("3. Listar cola")
    print("4. Salir")
            
    opcion = input("Elige una opción: ")
            
    if opcion == '1':
        try:
            num = int(input("Ingresa un número: "))
            cola.append(num)
            print(f"Número {num} agregado a la cola.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
            
    elif opcion == '2':
        if cola:
            atendido = cola.popleft()
            print(f"Se sacó el elemento: {atendido}")
        else:
            print("No se puede borrar, la cola está vacía.")
            
    elif opcion == '3':
        print("Cola actual: ", list(cola))
                
    elif opcion == '4':
        print("Saliendo del programa")
        break
                
    else:
        print("Opción no válida. Intenta de nuevo.")