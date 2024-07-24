# #crear una lista de 5 alumnos cada alumno almacenaremos su nombre apellido y edad

# #insertar al final de la lista los datos de antony
# # eliminar de la lista si existe los datos de abel
# # buscar y mostrar el alumno en la pocicion 4 de la lista.

# lista_alumnos=[
#     {
#         "nombre":"abel",
#         "apellido":"castillo",
#         "edad":20,
#     },{
#         "nombre":"ruth",
#         "apellido":"morales",
#         "edad":18,

#     },{
#         "nombre":"flor",
#         "apellido":"lucana ",
#         "edad":18,

#     },{
#         "nombre":"luz",
#         "apellido":"jimenez",
#         "edad":19,

#     },{
#         "nombre":"antony",
#         "apellido":"quispe",
#         "edad":25,
        
#     }
# ]

# lista_alumnos.remove({
#         "nombre":"abel",
#         "apellido":"castillo",
#         "edad":20,
        
# })
# indice=lista_alumnos.index({
    
#         "nombre":"luz",
#         "apellido":"jimenez",
#         "edad":19,
#     })
# print(lista_alumnos[indice]) 



# #2.Crear una lista con 4 diccionarios donde tendran los datos de sus mascotas (nombre ,edad ,sexo ,raza)

# #Tareas
# # mostrar la lista con los 4 diccionarios
# # editar el tercer registro y cambiarle la edad sin modificar la lista original
# # mostrar la lista original y luego la lista con el tercer registro modificado.

# lista_mascotas=[

#     {
#         "nombre":"chocolate",
#         "edad":2,
#         "sexo":"macho",
#         "raza":"pitbul"
#     },{
#         "nombre":"miel",
#         "edad":4,
#         "sexo":"hembra",
#         "raza":"terries"
#     },{
#         "nombre":"pinina",
#         "edad":3,
#         "sexo":"hembra",
#         "raza":""

#     },{
#         "nombre":"samuel",
#         "edad":7,
#         "sexo":"macho",
#         "raza":"pastor"


        
#     }
# ]

# lista_mascotas[3]["edad"]=1
# print(lista_mascotas)




# # OTRA MANERA DE RESOLVER

# lista_mascotas=[

#     {
#         "nombre":"chocolate",
#         "edad":2,
#         "sexo":"macho",
#         "raza":"pitbul"
#     },{
#         "nombre":"miel",
#         "edad":4,
#         "sexo":"hembra",
#         "raza":"terries"
#     },{
#         "nombre":"pinina",
#         "edad":3,
#         "sexo":"hembra",
#         "raza":""

#     },{
#         "nombre":"samuel",
#         "edad":7,
#         "sexo":"macho",
#         "raza":"pastor"


        
#     }
# ]
# print(lista_mascotas)
# copia_lista=lista_mascotas.copy()
# copia_lista[3]["edad"]=1
# print(copia_lista)


# #un empresario de alquiler de autos desea guardar en una base  datos la informacion de sus vehiculos, proceso que desea automatizar con un sistema informatico,las acciones que puede realizar el empresario son:
# #ver la lista de autos que tiene,podra tambien actualizar la lista y agregar un nuevo vehiculo

# #CASOS DE USO

# # COMO:
# #empresario de alquiler de autos.

# # QUIERE:
# # o  desea guardar la inoformacion de sus vehiculos ,como tambien automatizar con un sistema informatico para ver las acciones que puede realizar como :

# # PARA:
# # que pueda ver la lista de autos, 
# #tambien actualizar  y agregar un nuevo vehiculo

# #PROGRAMACION


# lista_vehiculos= [
   
#     {
#         "modelo":"sentra",
#         "marca":"nissan",
#         "color":"plomo",
#         "año":2012,
#         "precio":30.000
#     },{

#         "modelo":"yaris",
#         "marca":"toyota",
#         "color":"rojo",
#         "año":2011,
#         "precio":50.000
        

#     },{
       
#        "modelo":"starex",
#         "marca":"hyundai",
#         "color":"verde",
#         "año":2009,
#         "precio":80.000
        

   
#     }
# ]
# print(lista_vehiculos)
# lista_vehiculos[1]["color"]="dorado",
# lista_vehiculos.append({"modelo":"addx","marca":"toyota", "color":"azul", "año":2017, "precio":70.000 })
# print(lista_vehiculos)



#crear una lista de los primeros 20 numero primos haciendo uso de compresion.

números_primos = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1) if num != i)]
primos = [num for num in números_primos][:20]
print(primos)