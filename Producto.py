class Producto:
    def __init__(self, referencia, tipo, nombre, 
                 pvp,  descripcion, productor=None, 
                 distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor


adorno = Producto('000A','ADORNO','Vaso Adornado',15,
                  'Vaso de porcelana con dibujos') 

print(adorno)
print(adorno.tipo)  
