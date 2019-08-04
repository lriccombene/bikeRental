import unittest
from E_product import E_product,E_promotion

'''In this class point 1,2,3,4 is applied, which allows 
to create products with different price and name, 
the products separate them in promotion and simple. 
In particular, simple products are used individually 
or in promotions.
Use Python 3 Unittest libraries

En esta clase se aplica el punto 1,2,3,4 que permite 
crear productos con distintos precio y nombre , 
los productos los separe en promoción y simple .
En particular las productos simples son utilizados 
individualmente o en promociones .

Utilice las libreria Unittest de python 3 


'''


class Testing_product(unittest.TestCase):


    '''Este test funciona con al menos un resgistro en la base
        para empezar poroduct'''

        #get_product_all
    def test_7(self):
        obj_E_product = E_product()
        obj = obj_E_product.get_product_all()
        self.assertIsNotNone(obj)

    #test_get_product_simple
    def test_6(self):
        obj_E_product = E_product()
        obj = obj_E_product.get_product_all()
        self.assertIsNotNone(obj)

    #test_get_max_id
    def test_5(self):
        obj_E_product = E_product()
        max_id = obj_E_product.get_max_id()
        self.assertIsNotNone(max_id)
    
    #test_get_max_id_sp
    def test_4(self):
        obj_E_product = E_product()
        max_id = obj_E_product.get_max_id_sp("simple")
        self.assertIsNotNone(max_id)
    
    #test_get_product_id
    def test_3(self):
        obj_E_product = E_product()
        max_id = obj_E_product.get_max_id_sp("simple")
        obj_product = obj_E_product.get_product_id(max_id)
        self.assertIsNotNone(obj_product)
    
        #test_insert_product
    def test_1(self):
        obj_E_product = E_product()
        obj_E_product.name = "Rental by hour"
        obj_E_product.value = 5.0
        obj_E_product.description="Bike simple"
        #for the simple products the simple category for the
        # promotions is defined the promotion category
        obj_E_product.category ="simple"
        result=obj_E_product.save(obj_E_product)
        self.assertEqual(True, result, "Test insert product OK")

    #test_update_product_simple
    def test_2(self):
        obj_E_product = E_product()
        #import pdb; pdb.set_trace()
        max_id = obj_E_product.get_max_id_sp("simple")
        obj_product = obj_E_product.get_product_id(max_id)
        obj_product.name = "Test update"
        obj_product.value= 99.0
        obj_E_product.update_product(obj_product)
        obj_product_update = obj_E_product.get_product_id(max_id)
        self.assertEqual(obj_product_update.id_product, obj_product.id_product, "Test update product OK")
        #self.assertEqual(obj_product_update.name, obj_product.name, "Test update product OK")

    #def test_start(self):
    #    obj_E_product = E_product()
    #    result = obj_E_product.delete_product()
    #    self.assertEquals(True, result, "Test strat delete product OK")




if __name__ == '__main__':
    unittest.main()
