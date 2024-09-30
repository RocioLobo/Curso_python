#tarea
#Ejercico 1
#crear una clase banco
#sus atributos seran nombre,apellido,dni,numero de cuenta y saldo inicial

#como metodos podremos hacer deposito retirar dinero y ver estado de cuenta.
class banco:
    def init (self,nombre,apellido,dni,numero_cuenta,saldo inicial):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo_inicial=saldo_inicial


#Ejercicio 2
#crear una clase de agencia
#con sus atributos nombre y apellidos del pasajero dni numero de asiento fecha de viaje
#sus metodos seran ingresar origen,ingresar destino,cancelar viaje,ver estado de pasaje