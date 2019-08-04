import unittest
from E_product import E_product, E_promotion,E_detail_promotion

'''
En esta clase se aplica el punto 4 que permite crear promociones 
con distintos productos , los productos los divide en promoción 
y simple y en particular las promociones utilizan un detalle 
que contiene productos simples

In this class point 4 is applied that allows to create 
promotions with different products, the products divide 
them in promotion and simple and in particular the promotions 
use a detail that contains simple products



'''
class Testing_promotion(unittest.TestCase):
    id_product=0

        #test_save_promotion
    def  test_1(self):
        obj_E_product = E_product()
        obj_E_product.name = "Family Rental"
        obj_E_product.value = 0
        obj_E_product.description = "include from 3 to 5 Rentals"

        # for the simple products the simple category for the
        # promotions is defined the promotion category
        obj_E_product.category = "promotion"
        obj_E_product.save(obj_E_product)
        max_id = obj_E_product.get_max_id()
        self.id_product = max_id
        obj_E_promotion = E_promotion()
        obj_E_promotion.id_product = max_id
        obj_E_promotion.discount = 30
        obj_E_promotion.item_min = 3
        obj_E_promotion.item_max = 5
        result = obj_E_promotion.save(obj_E_promotion)
        self.assertEqual(True, result, "Test insert promotion OK")

    def test_get_promotion(self):
        obj_E_promotion = E_promotion()
        obj_promotion = obj_E_promotion.get_promotion()
        self.assertIsNotNone(obj_promotion)

    def test_update_promotion(self):
        obj_E_promotion = E_promotion()
        obj_E_promotion.item_min = 4
        obj_E_promotion.item_max = 6
        max_id = obj_E_promotion.get_max_id()
        obj_E_promotion.id_promotion = max_id
        result = obj_E_promotion.update_promotion(obj_E_promotion)
        self.assertEqual(True, result, "Test update promotion OK")

    def test_get_max_id(self):
        obj_E_promotion = E_promotion()
        obj_promotion = obj_E_promotion.get_max_id()
        self.assertIsNotNone(obj_promotion)

    def test_save_detail_promotion(self):
        #import pdb; pdb.set_trace()
        obj_E_product = E_product()
        obj_E_promotion = E_promotion()
        obj_E_dtl_pro= E_detail_promotion()

        id_product = obj_E_product.get_max_id_sp("promotion")
        #import pdb; pdb.set_trace()
        obj_promot = obj_E_promotion.get_promotion_id_product(id_product)
       
        list_product = obj_E_product.get_product_simple()
       
        count =0
        while len(list_product) <= obj_promot.item_min:
                count=1 + count
                obj_product = E_product()
                obj_product.name = "Test promotion " + str(count )
                obj_product.description = "Test description promotion " + str(count )
                obj_product.category = "simple"
                obj_product.value = 50+ (count * 10)
                obj_product.save(obj_product)
                list_product = obj_E_product.get_product_simple()
        
       
        count=0
        if len(list_product) >= obj_promot.item_min:
            for item in list_product:
                count=1+ count
                if count < obj_promot.item_max:
                    #import pdb; pdb.set_trace()
                    obj_dtl_pro=E_detail_promotion()
                    obj_dtl_pro.id_promotion = obj_promot.id_promotion
                    obj_dtl_pro.id_product=item.id_product
                    result = obj_dtl_pro.save(obj_dtl_pro)
                    self.assertEqual(result,result, "Test  OK")


    def test_calc_promotion(self):
        obj_E_promotion = E_promotion()
        #import pdb; pdb.set_trace()
        obj_promotion = obj_E_promotion.get_max_id()
        result = obj_E_promotion.calc_promotion(obj_promotion)
        self.assertIsNotNone(result)





if __name__ == '__main__':
    unittest.main()