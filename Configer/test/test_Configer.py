import unittest
import os

class TestConfiger(unittest.TestCase):
     def test_configer(self):
         from pyconfiger.Configer import Configer
         default_ps_fname = 'sample_settings.ini'


         my_ps1 = Configer(default_ps_fname=default_ps_fname)
         self.assertEqual(my_ps1.status, None)

         my_ps2 = Configer(default_ps_fname=default_ps_fname, status=False)
         self.assertEqual(my_ps2.status, False)

         my_ps3 = Configer(default_ps_fname=default_ps_fname, **{'status': True})
         self.assertEqual(my_ps3.status, True)

         my_ps4 = Configer(default_ps_fname=default_ps_fname, status=False,**{'somethings': [1.0, 2.0]})
         self.assertEqual(my_ps4.status, False)

         my_ps5 = my_ps4 + my_ps3
         self.assertEqual(my_ps5.status,True)
         self.assertEqual(my_ps5.somethings, [1.0, 2.0])

         my_ps6 = my_ps4.overload(my_ps3)
         self.assertEqual(my_ps6.status,False)

if __name__ == '__main__':
    unittest.main()
