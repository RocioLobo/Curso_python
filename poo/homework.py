#tarea
#Ejercico 1
#crear una clase banco
#sus atributos seran nombre,apellido,dni,numero de cuenta y saldo inicial
#como metodos podremos hacer deposito retirar dinero y ver estado de cuenta.

#crear una clase banco
class Banco:
#sus atributos seran nombre,apellido,dni,numero de cuenta y saldo inicial
    def _init_(self, nombre, apellido, dni, numero_cuenta, saldo_inicial):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial
#como metodos podremos hacer deposito retirar dinero y ver estado de cuenta.

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto} realizado. Saldo actual: {self.saldo}")

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes.")

    def ver_estado_cuenta(self):
        print("----- Estado de Cuenta -----")
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"DNI: {self.dni}")
        print(f"Número de Cuenta: {self.numero_cuenta}")
        print(f"Saldo: {self.saldo}")
        print("---------------------------")

# Ejemplo de uso
cliente1 = Banco("Juan", "Perez", "12345678A", "1234567890", 1000)

cliente1.depositar(500)
cliente1.retirar(200)
cliente1.ver_estado_cuenta()

                              
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