from collections import deque

# Crear y agregar elementos.
cola = deque(["Ana", "Carlos"])

cola.append("Jorge")
cola.append("Andres")
print("Cola actual: ", cola)

atendido = cola.popleft()
print(f"Se atendio a: {atendido}")

print("Cola restante: ", cola)

atendido = cola.popleft()
print(f"Se atendió a: {atendido}")
print("Cola restante: ", cola)