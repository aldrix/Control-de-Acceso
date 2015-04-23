# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Patricia Valencia
         Aldrix Marfil
'''

import unittest 
from mdlaccesscontrol import clsAccessControl

class TestEncript(unittest.TestCase):
    
    #Caso Malicioso
    def testClaveVacia(self):
        object = clsAccessControl()
        string = ""
        result = object.encript(string)
        self.assertEqual(result,"")
        
    #Caso Malicioso
    def testClaveInvalidalong7(self):
        object = clsAccessControl()
        string = "clave#7"
        result = object.encript(string) 
        self.assertFalse(result,"Clave inválida")

    #Caso Malicioso        
    def testClaveInvalidalong17(self):
        object = clsAccessControl()
        string = "Clavede#17digitos"
        result = object.encript(string) 
        self.assertFalse(result,"Clave inválida")

    #Caso Frontera
    def testClaveValidalong8(self):
        object = clsAccessControl()
        string = "Hola123*"
        result = object.encript(string) 
        self.assertTrue(result,"Clave Invalida")
    
    #Caso Frontera    
    def testclavevalidalong16(self):
        object = clsAccessControl()
        string = "Estoes1prueb@.Xy"
        result = object.encript(string) 
        self.assertTrue(result,"Clave Invalida")
        
        