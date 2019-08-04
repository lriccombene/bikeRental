import unittest
import queue
from E_product import E_product

'''
In this class the singleton pattern is amplified, which makes it easy 
for us to always have the same object and in particular we need a 
list of the type queue that Basic FIFO implements with the put and 
get methods that are used in the TEST class

'''
#tipo_usuario =""
class Singleton(object):
     _instance = None
     list_rents = queue.Queue()

     def __new__(self):
       
        #import pdb; pdb.set_trace()
        if not self._instance:
            self._instance = super(Singleton, self).__new__(self)
            self.list_rents = queue.Queue()
        return self._instance

class user_rents(unittest.TestCase):
    list_rents = ""


    def test_1(self):
        #import pdb; pdb.set_trace()
        obj_E_prod = E_product()
        list_product = obj_E_prod.get_product_simple()
        singleton =Singleton()
        
        for item in list_product:
           print ("" + item.name)
           singleton.list_rents.put(item)

        #import pdb; pdb.set_trace()
        while not singleton.list_rents.empty():
           obj_prod =singleton.list_rents.get()
           print (obj_prod.name)
	    
        result=True
        self.assertEqual(True, result, "Test singleton promotion OK")





if __name__ == '__main__':
    unittest.main()

