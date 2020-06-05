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

#print(productos)

for producto in productos:
    print(producto, "\n")

print("\n")

for producto in productos:
   print(producto.referencia, producto.nombre)

print("\n")

# Dona error pq autor només és un atribut d'una subclasse.
for producto in productos:
   print(producto.autor)

print("\n")


# isistance comprovar si es d'un tipus o altre.
for p in productos:
    if( isinstance(p, Adorno) ):
        print(p.referencia, p.nombre)
    elif( isinstance(p, Alimento) ):
        print(p.referencia, p.nombre, p.productor)
    elif( isinstance(p, Libro) ):
        print(p.referencia, p.nombre, p.isbn)   

