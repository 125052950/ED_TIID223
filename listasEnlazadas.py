class Nodo:

    def __init__(self, numero):
        #Valor que tendrá el nodo
        self.numero = numero
        #Apunta al siguiente nodo
        self.siguiente = None

class ListasEnlazadas:

    def __init__(self):
        #Inicio del nodo
        self.cabeza = None

    def insertar_Nodo_al_Inicio(self, numero):
        #Ingresar el valor al inicio del nodo
        nuevo_nodo = Nodo(numero)

        if(self.cabeza is None):

            self.cabeza = Nodo(numero)

            return
    
        nuevo_nodo.siguiente = self.cabeza

        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):
        
        nuevo_nodo = Nodo(numero)

        if(self.cabeza == None):

            self.cabeza = nuevo_nodo

            return

        #Referencia temporal
        actual = self.cabeza
    
        while(actual.siguiente):
        
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def Imprimir_ListasEnlazadas(self):

        actual = self.cabeza

        while(actual):
            print(actual.numero, " → ", end = " ")
            actual = actual.siguiente
        print("None")

    def eliminar_al_inicio(self):
        #La lista esta vacia
        if self.cabeza is None:
            return None  

        nodo_eliminado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        nodo_eliminado.siguiente = None
        return nodo_eliminado.numero
    
    def eliminar_al_final(self):
        #La lista esta vacia
        if self.cabeza is None:
            return None 

        if self.cabeza.siguiente is None:
            nodo_eliminado = self.cabeza
            self.cabeza = None
            return nodo_eliminado.numero

        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente

        nodo_eliminado = actual.siguiente
        actual.siguiente = None
        return nodo_eliminado.numero

Mi_Lista = ListasEnlazadas()

Mi_Lista.Insertar_Nodo_al_Final(5)
Mi_Lista.Insertar_Nodo_al_Final(4)
Mi_Lista.Insertar_Nodo_al_Final(3)
Mi_Lista.Imprimir_ListasEnlazadas()
Mi_Lista.eliminar_al_inicio()
Mi_Lista.eliminar_al_final()
Mi_Lista.Imprimir_ListasEnlazadas()
