historial = []

historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("Historial: ", historial)

pagina_actual = historial[2]
print("Página actual: ", pagina_actual)

pagina_salida = historial.pop()
print("Saliendo de: ", pagina_salida)

print("Historial actualizado: ", historial)