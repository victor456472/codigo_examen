from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, DateTime, String, Text, Float
from sqlalchemy.orm import sessionmaker

"""la ruta del engine debe ser modificada
    de la siguiente forma:
    mysql+pymysql://usuario:contraseña@localhost/products_bd
    """
engine = create_engine('mysql+pymysql://root:contraseña@localhost/products_bd')
Base = declarative_base()

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    tittle = Column(String(50))
    description = Column(Text)
    value = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    def __repr__(self):
        return "<User(fullname='%s', email='%s', password='%s', address='%s', phone='%s', born_date='%s')>" % (
            self.tittle,
            self.description,
            self.value,
            self.quantity,
        )

Session = sessionmaker(engine)
session = Session()


