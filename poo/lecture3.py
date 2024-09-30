#crear una clase de alumnos con los atributos que usted crea por conveniente
#luego instanciara a 4 alumnos
class Alumno:
    def init (self,nombre,dni,edad,email,programa_estudio="APSTI"):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        self.email=email
        self.programa_estudio=programa_estudio
#metodos
def escribir(self):
    print("sty escribiendo")
def tarea(self,nombre_docente):
    print("haciendo la tarea de:",nombre_docente)
def terminar_tarea(self):
    print("terminando la tarea anterior")

maricielo=Alumno("maricielo",75869321,14,"yo@gmail")
maricielo.tarea("Alicia")
maricielo.terminar_tarea()
maricielo.tarea("Alvarez")



