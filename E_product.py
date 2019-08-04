'''
Este archivo contiene las clases que se comunican con la base 
de datos utizando la libreria SQLALCHEMY , Aqui existe la relacion 
entre clases que representa el modelo de base de datos que
 se utilizo Postgres. Producto - Promocion , Promocion - Detalle, 
 Producto - Detalle 


This file contains the classes that communicate with 
the database using the SQLALCHEMY library. Here is the 
relationship between classes that represents the database model used by Postgres. Product - Promotion, Promotion - Detail, Product - Detail



'''




import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy import func,Boolean, Numeric, update,Float,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import queue
from E_configuracion import configuracion

base = declarative_base()

class E_product(base):
    __tablename__="product"
    id_product = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    value = Column(Float)
    session=""

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
            #import pdb; pdb.set_trace()
            obj_E_product.session.add(obj_E_product)
            obj_E_product.session.commit()
            obj_E_product.session.close()
            return True

        except :
            obj_E_product.session.rollback()
            obj_E_product.session.close()
            return False

    def get_max_id(self):
        #import pdb; pdb.set_trace()
        max_id = self.session.query(func.max(E_product.id_product)).scalar()
        self.session.close()
        return max_id


    def get_max_id_sp(self,p_category):
        #import pdb; pdb.set_trace()
        max_id = self.session.query(func.max(E_product.id_product)).\
            filter_by(category = p_category).scalar()
        self.session.close()
        
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
            return obj_product

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


    def get_product_all(self):
        # import pdb;pdb.set_trace()
        obj_product = self.session.query(E_product).all()
        self.session.close()
        try:
            a = obj_product[0]
            return obj_product
        except:
            return obj_product

    def get_product_simple(self):
        # import pdb;pdb.set_trace()
        obj_product = self.session.query(E_product).\
                     filter_by(category = "simple").all()
        self.session.close()
        try:
            a = obj_product[0]
            return obj_product
        except:
            return obj_product





    def delete_product(self):
        sql = text('delete from product')
        result = self.session.execute(sql)
        try:
            self.session.commit()
            self.session.close()
            return True
        except:
            self.session.close()
            return False





class E_promotion(base):
    __tablename__="promotion"
    id_promotion = Column(Integer, primary_key=True, autoincrement=True)
    id_product = Column(Integer, ForeignKey('product.id_product'))
    item_min = Column(String)
    item_max= Column(String)
    discount= Column(Float)
    session=""

    def __init__(self):
        obj_conexion = configuracion()
        engine = create_engine(obj_conexion.config())
        Session = sessionmaker(bind=engine)
        self.session = Session()

    @classmethod
    def save(cls, obj_promotion):
        #import pdb; pdb.set_trace()
        obj_E_promotion = cls()
        try:
            obj_E_promotion.id_product = obj_promotion.id_product
            obj_E_promotion.item_min = obj_promotion.item_min
            obj_E_promotion.item_max = obj_promotion.item_max
            obj_E_promotion.discount = obj_promotion.discount
            obj_E_promotion.session.add(obj_E_promotion)
            obj_E_promotion.session.commit()
            obj_E_promotion.session.close()
            return  True

        except IntegrityError:
            obj_E_promotion.session.rollback()
            obj_E_promotion.session.close()
            return False

    def get_promotion_id_product(self,id_product):
        #import pdb; pdb.set_trace()
        obj_product = self.session.query(E_promotion).\
            filter_by(id_product=id_product).first()
        self.session.close()
        try:
            a = obj_product.id_product
            return obj_product
        except:
            return obj_product

    def get_promotion(self):
        #import pdb;pdb.set_trace()
        obj_promotion = self.session.query(E_promotion).all()
        self.session.close()
        try:
            a = obj_promotion[0]
            return obj_promotion
        except:
            return obj_promotion


    def update_promotion(self, obj_promotion):
        #import pdb; pdb.set_trace()
        obj_update = update(E_promotion).where(E_promotion.id_promotion == obj_promotion.id_promotion). \
        values(item_min=obj_promotion.item_min, item_max=obj_promotion.item_max)
        try:
            self.session.execute(obj_update)
            self.session.commit()
            self.session.close()
            return True
        except:
            return False

    def get_max_id(self):
        # import pdb; pdb.set_trace()
        max_id = self.session.query(func.max(E_promotion.id_promotion)).scalar()
        self.session.close()
        return max_id

    def calc_promotion(self,p_id_promotion):
        sql = text("select SUM((select pr.value from product pr " +
              "where pr.id_product=dp.id_product)) " +
              " from product p "
              " inner join promotion pm  on p.id_product = pm.id_product " +
              " inner join detail_promotion dp  " + 
              " on pm.id_promotion = dp.id_promotion " +
              " where pm.id_promotion="+str(p_id_promotion))
        result = self.session.execute(sql)
        try:
          print (result[0])
          self.session.close()
          return result
        except :
          self.session.close()
          return False


class E_detail_promotion(base):
    __tablename__ = "detail_promotion"
    id_detail_promotion = Column(Integer, primary_key=True, autoincrement=True)
    id_product = Column(Integer, ForeignKey('product.id_product'))
    id_promotion = Column(Integer, ForeignKey('promotion.id_promotion'))
    session=""

    def __init__(self):
        obj_conexion = configuracion()
        engine = create_engine(obj_conexion.config())
        Session = sessionmaker(bind=engine)
        self.session = Session()

    @classmethod
    def save(cls, obj_dtl_prom):
        #import pdb; pdb.set_trace()
        obj_E_detail_promotion = cls()
        try:
            obj_E_detail_promotion.id_product = obj_dtl_prom.id_product
            obj_E_detail_promotion.id_promotion = obj_dtl_prom.id_promotion
            obj_E_detail_promotion.session.add(obj_E_detail_promotion)
            obj_E_detail_promotion.session.commit()
            obj_E_detail_promotion.session.close()
            return True

        except IntegrityError:
            obj_E_detail_promotion.session.rollback()
            obj_E_detail_promotion.session.close()
            return False








