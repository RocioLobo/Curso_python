#el usuario podra ver las listas de horarios disponibles.
horarios_disponibles=["12:00-14:00","15:00-16:00","17:00-19:00","20:00-21:00"]
print("horas_disponibles: ")
for horarios in horarios_disponibles:
    print(horarios)
#el usuario podra reservar en uno de los horarios disponibles.
horarios_seleccionada=input("ingrese un horario de la lista por favor: ")
reserva_lista=True
if reserva_lista:
    print("su reserva fue realizada con exito.")
#el usuario podra pagar por alquiler de la reserva realizada.
    costo_alquiler=20
    pago_realizado= True
    if pago_realizado:
#el usuario podra verificar su alquiler el cual le mostrar los detalles como la fecha, hora y costo del alquiler que realizo.

        print("pago del alquiler realizado.")
        print("detalles del alquiler.")
        print(f"fecha y hora: {horarios_seleccionada}")
        print(f"costo: $ {costo_alquiler}")
    



