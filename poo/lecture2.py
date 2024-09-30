class Personaje:
    #"atributos"
    def _init(self,nombre,edad,usuario,bando,raza): # (doble guion bajo _. cuando instancie (asignar a una variable) me permitira pasar por parametro
        self.nombre=nombre #estan preestablecidos)
        self.edad=edad #self siempre hace referencia a su objeto
        self.usuario=usuario
        self.bando=bando
        self.raza=raza
    def mostrar_personaje(self): # metodo
        return {
             "nombre":self.nombre,
             "edad":self.edad,
             "usuario":self.usuario,
             "bando":self.bando,
             "raza":self.raza,
        }

luffy=Personaje("luffy",18,"gomu gomu no mi","pirata","humano") #(estoy instanciando)
print(luffy.nombre)
print(luffy.mostrar_personaje()) # metodo
#dentro del atributo nombre esta eso, asi que pondemos imprimir sin problema
cobby=Personaje("cobby",15,"no","sword","humano")
print(cobby.bando)
king=Personaje("king",40,"zoan","pirata","lunaria")
print(king.raza) #mostar atributo
print(king.mostrar_personaje())#cuando quiero ejecutar un metodo y ()