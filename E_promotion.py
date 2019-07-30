import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,Float,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()

class E_promotion(base):
      __tablename__="promotion"
      id_promotion = Column(Integer, primary_key=True, autoincrement=True)
      id_product = Column(Integer, ForeignKey('product.id_product'))
      item_min =  Column(String)
      item_max= Column(String)
      discount= Column(Float)

      def __init__(self):
          obj_conexion = configuracion()
          engine = create_engine(obj_conexion.config())
          Session = sessionmaker(bind=engine)
          self.session = Session()

      @classmethod
      def save(cls, obj_promotion):
          obj_E_promotion = cls()
          try:

              obj_E_promotion.id_product = obj_promotion.id_product
              obj_E_promotion.item_min = obj_promotion.item_min
              obj_E_promotion.item_max = obj_promotion.item_max
              obj_E_promotion.discount = obj_promotion.discount

              obj_E_promotion.session.add(obj_E_promotion)
              obj_E_promotion.session.commit()
              obj_E_promotion.session.close()

          except IntegrityError:
              obj_E_promotion.session.rollback()
              obj_E_promotion.session.close()
              return False



      def actualizar(self,obj_promotion):
          #pyqtRemoveInputHook()
          #import pdb; pdb.set_trace()
          obj_update= update(E_promotion).where(E_promotion.id_product==obj_promotion.id_product).\
          values(item_min=obj_promotion.item_min )

          self.session.execute(obj_update)
          self.session.commit()
          self.session.close()