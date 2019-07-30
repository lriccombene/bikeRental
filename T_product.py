import unittest
from E_product import E_product

class Testing_product(unittest.TestCase):


    def test_insert_product(self):
        obj_E_product = E_product()
        obj_E_product.name = "Rental by hour"
        obj_E_product.value = 5.0
        obj_E_product.description="Bike simple"

        #for the simple products the simple category for the
        # promotions is defined the promotion category
        obj_E_product.category ="simple"

        max_id=obj_E_product.get_max_id()
        old_id= int(max_id) + 1

        obj_E_product.save(obj_E_product)
        max_id = obj_E_product.get_max_id()
        self.assertEqual(old_id, max_id, "Test insert product OK")

    def test_update_product_simple(self):
        obj_E_product = E_product()
        #import pdb; pdb.set_trace()
        max_id = obj_E_product.get_max_id_simple()
        obj_product = obj_E_product.get_product_id(max_id)
        obj_product.name= "Test update"
        obj_product.value= 99.0
        obj_E_product.update_product(obj_product)
        obj_product_update= obj_E_product.get_product_id(max_id)
        self.assertEqual(obj_product_update.id_product, obj_product.id_product, "Test update product OK")
        self.assertEqual(obj_product_update.name, obj_product.name, "Test update product OK")




if __name__ == '__main__':
    unittest.main()