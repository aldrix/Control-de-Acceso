# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Patricia Valencia
         Aldrix Marfil
'''

import unittest
from mdlaccesscontrol import clsAccessControl

class Testcheck_password(unittest.TestCase):
 
    #Caso Normal
    def testHashValidoCorrespodeAClaveCorrecta(self):
        object = clsAccessControl()
        password = "1XZABC@W"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")

    #Caso Esquina
    def testHashyClaveDiferentePorUnaLetra(self):
        object = clsAccessControl()
        password = "1ZA3BC@Ws"
        passwordInvalid = "1ZA3C@Ws" 
        encriptar = object.encript(passwordInvalid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
     
    #Caso Esquina
    def testHashValidoClaveInvalida(self):
        object = clsAccessControl()
        password = "abcd@123" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    def testHashValidoClaveLong7(self):
        object = clsAccessControl()
        password = "xYz2#15" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
     