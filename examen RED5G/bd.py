from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, create_engine, DateTime, String
from sqlalchemy.orm import sessionmaker

"""la ruta del engine debe ser modificada
    de la siguiente forma:
    mysql+pymysql://usuario:contraseña@localhost/crud_exam
    """
engine = create_engine('mysql+pymysql://root:contraseña@localhost/crud_exam')
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    address = Column(String(50), nullable=False)
    phone = Column(String(50), nullable=False, unique=True)
    born_date = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User(fullname='%s', email='%s', password='%s', address='%s', phone='%s', born_date='%s')>" % (
            self.fullname,
            self.email,
            self.password,
            self.address,
            self.phone,
            self.born_date
        )
    
Session = sessionmaker(engine)
session = Session()
