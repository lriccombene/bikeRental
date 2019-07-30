import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,Float,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()

class E_product(base):
    __tablename__="product"
    id_product = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    value = Column(Float)

    def __init__(self):
        obj_conexion = configuracion()
        engine = create_engine(obj_conexion.config())
        Session = sessionmaker(bind=engine)
        self.session = Session()

    @classmethod
    def save(cls, obj_product):
        obj_E_product = cls()
        try:
            obj_E_product.name = obj_product.name
            obj_E_product.description = obj_product.description
            obj_E_product.category = obj_product.category
            obj_E_product.value = obj_product.value

            obj_E_product.session.add(obj_E_product)
            obj_E_product.session.commit()
            obj_E_product.session.close()

        except :
            obj_E_product.session.rollback()
            obj_E_product.session.close()
            return False

    def get_max_id(self):
        #import pdb; pdb.set_trace()
        max_id = self.session.query(func.max(E_product.id_product)).scalar()
        return max_id

    def get_max_id_simple(self):
        #import pdb; pdb.set_trace()
        max_id = self.session.query(func.max(E_product.id_product)).\
            filter_by(category = "simple").scalar()
        return max_id



    def get_product_id(self, id_product):
        #import pdb; pdb.set_trace()
        obj_product = self.session.query(E_product).\
            filter_by(id_product=id_product).first()
        self.session.close()
        try:
            a = obj_product.id_product
            return obj_product
        except:
            return False


    def update_product(self, obj_product):
        #import pdb; pdb.set_trace()
        obj_update= update(E_product).where(E_product.id_product==obj_product.id_product).\
        values(name=obj_product.name, value=obj_product.value)
        try:
            self.session.execute(obj_update)
            self.session.commit()
            self.session.close()
        except:
            return False