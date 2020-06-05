#El polimorfismo se refiere a una propiedad de la herencia por la que objetos de distintas subclases pueden responder a una misma acción común. 
#En Python, todas las clases son subclases de una superclase común llamada object, por tanto, todas las clases son polimórficas por defecto.
class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
    REFERENCIA\t{}
    NOMBRE\t{}
    PVP\t\t{}
    DESCRIPCIÓN\t{}\n
    """.format(self.referencia,self.nombre,self.pvp,self.descripcion)
               
               
class Adorno(Producto):
    pass

adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")
#print(adorno)


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
    REFERENCIA\t{}
    NOMBRE\t{}
    PVP\t\t{}
    DESCRIPCIÓN\t{}
    PRODUCTOR\t{}
    DISTRIBUIDOR\t{}\n
    """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

alimento = Alimento(2035, "Botella de Aceite de Oliva", 5, "250 ML")
alimento.productor = "La Aceitera"
alimento.distribuidor = "Distribuciones SA"
#print(alimento)


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
    REFERENCIA\t{}
    NOMBRE\t{}
    PVP\t\t{}
    DESCRIPCIÓN\t{}
    ISBN\t{}
    AUTOR\t{}\n
    """.format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)


libro = Libro(2036, "Cocina Mediterránea",9, "Recetas sanas y buenas")
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"
#print(libro)

productos = [adorno, alimento]
productos.append(libro)

#Polimorfismo - En Python todos las clases són polimorfiscos por defecto.

#Todas las clases son subclases de la superclase Object.

#Este método recibe objetos de distintas clases y accede al atributo pvc dando
#por hecho que existe en ellos
def rebajar_producto(p, rebaja):
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

print(alimento)
print("\n")
alrebajado = rebajar_producto(alimento, 50)
print(alrebajado)

copia_al = alimento
copia_al.referencia = 1111
print(copia_al)
print(alimento)

