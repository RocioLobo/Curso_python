#tarea
#Ejercico 1
#crear una clase banco
#sus atributos seran nombre,apellido,dni,numero de cuenta y saldo inicial
#como metodos podremos hacer deposito retirar dinero y ver estado de cuenta.


#crear una clase banco
class banco:
#sus atributos seran nombre,apellido,dni,numero de cuenta y saldo inicial
    def __init__ (self,nombre,apellido,dni,numero_cuenta,saldo_inicial):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo_inicial=saldo_inicial
#como metodos podremos hacer deposito retirar dinero y ver estado de cuenta.
#metodos
def depositar(self,cantidad):
    if cantidad > 0:
        self.saldo_inicial=self.saldo_inicial+cantidad
        resultado=f"deposito realizado: {self.saldo_inicial}"
        return resultado
# def retirar_dinero(self,nombre_docente):
#     print("haciendo la tarea de:",nombre_docente)
# def ver_estado_de_cuenta(self):
#     print("terminando la tarea anterior")

rocio=banco("rocio","lobo",76004955,12345558866,100)
# print(rocio.depositar(30))
print(rocio.saldo_inicial)

                              

#Ejercicio 2
#crear una clase de agencia
#con sus atributos nombre y apellidos del pasajero dni numero de asiento fecha de viaje
#sus metodos seran ingresar origen,ingresar destino,cancelar viaje,ver estado de pasaje

#crear una clase de agencia
class Agencia:
#con sus atributos nombre y apellidos del pasajero dni numero de asiento fecha de viaje.
    def _init_(self, nombre_pasajero, apellido_pasajero, dni, numero_asiento, fecha_viaje):
        self.nombre_pasajero = nombre_pasajero
        self.apellido_pasajero = apellido_pasajero
        self.dni = dni
        self.numero_asiento =numero_asiento
        self.fecha_viaje = fecha_viaje

#sus metodos seran ingresar origen,ingresar destino,cancelar viaje,ver estado de pasaje.

    def ingresar_origen(self, origen):
        self.origen = origen
        self.estado = "Origen Ingresado"
   def ingresar_destino(self, destino):
        self.destino = destino
        self.estado = "Destino Ingresado"

    def cancelar_viaje(self):
        self.estado = "Cancelado"

    def ver_estado_pasaje(self):
        print(f"Estado del pasaje: {self.estado}")
        print(f"Nombre del pasajero: {self.nombre_pasajero} {self.apellido_pasajero}")
        print(f"DNI: {self.dni}")
        print(f"Asiento: {self.asiento}")
        print(f"Fecha de viaje: {self.fecha_viaje}")
        if self.origen:
            print(f"Origen: {self.origen}")
        if self.destino:
            print(f"Destino: {self.destino}")