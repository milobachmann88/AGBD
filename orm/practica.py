from sqlalchemy import Column, Integer, String, Float, Boolean, create_engine, select, func, or_
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

#comando para correr con orm
#primero rm productos.py para q no se sobreescriba la db
#.venv/bin/python practica.py

#----------------------------------------1-------------------------------
# 1. Definimos la clase (una sola vez)
class Base(DeclarativeBase):
    pass

class Producto(Base):
    __tablename__ = "productos"

    id      = Column(Integer, primary_key=True)
    nombre  = Column(String)
    precio   = Column(Float)
    stock  = Column(Integer)
    categoria = Column(String)
    activo = Column(Boolean)

# 2. Consultamos como si fueran objetos Python
engine = create_engine("sqlite:///productos.db")

productos = [
    Producto(nombre="Mouse", precio=250, stock=10, categoria="perifericos", activo= True),
    Producto(nombre="Teclado", precio=450, stock=8, categoria="perifericos", activo= True),
    Producto(nombre="Monitor", precio=1200, stock=5, categoria="Monitores", activo= True),
    Producto(nombre="Auriculares", precio=350, stock=15, categoria="Audio", activo= True),
    Producto(nombre="Webcam", precio=480, stock=7, categoria="Cámaras", activo= True),
]
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

with Session() as session:
    session.add_all (productos)
    session.commit()
    productos_menor_500 = session.query(Producto) \
                      .filter(Producto.precio < 500) \
                      .all()
    
    print ("Productos con precio menor a $500: ")
    for p in productos_menor_500:
        print(p.nombre, p.precio)  # ← atributos reales, no índices

#----------------------------------------2-------------------------------
productos_nuevos= [
    Producto(nombre="Teclado mecanico", precio=8500, stock=15, categoria="perifericos", activo= True),
    Producto(nombre="Mouse inalambrico", precio=4200, stock=30, categoria="perifericos", activo= False),
    Producto(nombre="Monitor 24 pulgadas", precio=62000, stock=8, categoria="Monitores", activo= True),
    Producto(nombre="Auriculares Bluetooth", precio=12300, stock=20, categoria="Audio", activo= True),
    Producto(nombre="SSD 1TB", precio=418500, stock=25, categoria="Almacenamiento", activo= True),
    Producto(nombre="RAM 16GB", precio=15600, stock=18, categoria="componentes", activo= True),
    Producto(nombre="Mousepad XL", precio=2100, stock=40, categoria="perifericos", activo= True),
    Producto(nombre="Hub USB-C", precio=5400, stock=6, categoria="accesorios", activo= False),
    Producto(nombre="Cable HDMI", precio=1800, stock=50, categoria="accesorios", activo= True),
    Producto(nombre="Webcam full HD", precio=9800, stock=12, categoria="perifericos", activo= True),
    Producto(nombre="Silla gamer", precio= None, stock= 3, categoria= None, activo= False) 
]

with Session() as session:
    session.add_all (productos_nuevos)
    session.commit()
    cantidad = session.query(Producto).count()

    print(" ")
    print("Ejercicio 2 ")
    print(" ")
    print(cantidad)
    print("Tengo 5 más pq son los que tenía antes")

#----------------------------------3-------------------------------------------------
with Session() as session:
    productos_perifericos = session.query(Producto) \
        .filter(Producto.categoria == "perifericos") \
        .all()

    print(" ")
    print("Ejercicio 3")
    print(" ")
    print("Productos de la categoría periféricos:")
    for p in productos_perifericos:
        print(p.nombre, p.precio)

#---------------------------------4-------------------------------------------------
with Session() as session:
    productos_mayor_10000_ordenados = session.query(Producto) \
                      .filter(Producto.precio >10000) \
                      .order_by(Producto.precio.desc())\
                      .all()
    print(" ")
    print("Ejercicio 4")
    print(" ")
    print ("Productos con precio menor a $10000 ordenados: ")
    for p in productos_mayor_10000_ordenados:
        print(p.nombre, p.precio)  # ← atributos reales, no índices

#-------------------------------5----------------------------------------------------
with Session() as session:
    productos_stock12_activos = session.query(Producto) \
                      .filter(Producto.stock <= 12) \
                      .filter(Producto.activo == True)\
                      .all()
    print(" ")
    print("Ejercicio 5")
    print(" ")
    print ("Productos con stock menor o igual a 12 activos ")
    for p in productos_stock12_activos:
        print(p.nombre, p.stock)
#-------------------------6-----------------------------------------
with Session() as session:
    productos_entre_5y20 = session.query(Producto) \
                      .filter(Producto.precio > 5000) \
                      .filter(Producto.precio < 20000)\
                      .all()
    print(" ")
    print("Ejercicio 6")
    print(" ")
    print ("Productos entre 5000 y 20000 ")
    for p in productos_entre_5y20:
        print(p.nombre)
#------------------------7----------------------------------------
with Session() as session:
    producto_caro = session.query(Producto) \
                      .order_by(Producto.precio.desc()) \
                      .first()
    print(" ")
    print("Ejercicio 7")
    print(" ")
    print ("Producto mas caro")
    print(producto_caro.nombre)

#------------------------8-------------------------------
with Session() as session:
    producto_inactivo = session.query(Producto)\
                        .filter(Producto.activo == False)\
                        .all()

    print(" ")
    print("Ejercicio 8")
    print(" ")
    print ("Productos inactivos")
#    for p in producto_inactivo:
#       print(producto_inactivo.nombre)

#------------------------extra---------------------------------------
with Session() as session:
    hub = session.get(Producto, 13)

    hub.activo = True
    hub.stock = 20

    session.commit()
    print("Hub USB-C actualizado")
    print(hub.nombre, hub.stock, hub.activo)

with Session() as session:
    productos_usb = session.query(Producto)\
                        .filter(Producto.nombre.contains("USB"))\
                        .all()
    print(" ")
    print("Extra")
    print(" ")
    print ("Productos con USB")
    for p in productos_usb:
        print(p.nombre)

#-----------------9------------------
with Session() as session:
    p_audio_componentes = session.query(Producto) \
                      .where (or_(Producto.categoria == "audio",Producto.categoria == "componentes")) \
                      .all()

    print(" ")
    print("Ejercicio 9")
    print(" ")
    print ("Productos de audio o componentes")
    for p in p_audio_componentes:
        print(p.nombre)
#--------------10----------------------
with Session() as session:
    productos_a = session.query(Producto) \
                      .filter(Producto.nombre.contains("a")) \
                      .all()

    print(" ")
    print("Ejercicio 10")
    print(" ")
    print ("Productos con a")
    for p in productos_a:
        print(p.nombre)
    print(f"Hay {len(productos_a)} productos")

#--------------11----------------------
with Session() as session:
    productos_m = session.query(Producto) \
                      .filter(Producto.nombre.startswith("M")) \
                      .all()

    print("\nEjercicio 11\n")
    print ("Productos que empiezan con M")
    for p in productos_m:
        print(p.nombre)

#--------------12----------------------
with Session() as session:
    productos_none = session.query(Producto) \
                      .filter(Producto.categoria==None) \
                      .all()

    print("\nEjercicio 12\n")
    print ("Productos con categoria none")
    for p in productos_none:
        print(p.nombre)

#si filtras por precio no pasa nada

#--------------13----------------------
with Session() as session:
    usb = session.query(Producto)\
        .filter(Producto.nombre == "Hub USB-C").first()
    idusb= usb.id
    producto_usb = session.get(Producto, idusb) 
    Producto.stock= 20
    Producto.activo= True
    session.commit()
                      

    print("\nEjercicio 13\n")
    print ("Hub USB-C actualizado:")
    print(producto_usb.nombre, producto_usb.stock, producto_usb.activo)
#-----------------14----------------------
with Session() as session:
    perifericos= session.query(Producto)\
                      .filter(Producto.categoria=="perifericos")\
                      .all()

    print("\nEjercicio 14\n")
    for p in perifericos:
        p.precio= p.precio + p.precio*0.1
        session.commit()
        print(p.nombre, p.precio)
#el teclado vale 9350

#------------15-----------------
with Session() as session: 
    hdmi = session.query(Producto)\
            .filter(Producto.nombre == "Cable HDMI").first()
    idhdmi= hdmi.id
    producto_hdmi = session.get(Producto, idhdmi) 
    session.delete(producto_hdmi)
    session.commit()
    cant= session.query(Producto).count()
print("\nEjercicio 15\n")
print(cant)
print("Tengo 5 mas pq son los que tenia inicialmente")

#--------------16-------------------------
with Session() as session:
    inactivos_menos200=session.query(Producto) \
                      .where (or_(Producto.precio < 200,Producto.activo == False)) \
                      .all()
    for p in inactivos_menos200:
        session.delete(p)
    session.commit()
    cantt= session.query(Producto).count()
    print("\nEjercicio 16\n")
    print(cantt)
#----------------extra-------------------------
