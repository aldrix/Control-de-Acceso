# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Patricia Valencia
         Aldrix Marfil
'''

import unittest
from mdlaccesscontrol import clsAccessControl

class Testcheck_password(unittest.TestCase):
 
    #Casos Fronteras
    
    def testHashValidoCorrespodeAClaveCorrectaLong8(self):
        object = clsAccessControl()
        password = "1XZABC@W"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")
        
     #Caso Frontera
    def testHashValidoCorrespodeAClaveCorrectaLong16(self):
        object = clsAccessControl()
        password = "1abcdXZABC@W123@"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")
        
    #Caso Frontera
    def testHashValidoClaveInvalida(self):
        object = clsAccessControl()
        password = "abcd@123" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Caso Normal
    def testHashValidoCorrespondeAClaveCorrectaLong10(self):
        object = clsAccessControl()
        password = "fggA#123.s"
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
    def testHashValidoClaveLong7(self):
        object = clsAccessControl()
        password = "xYz2#15" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
     
     #Caso Esquina
    def testHashValidoClaveLong17(self):
        object = clsAccessControl()
        password = "xYz2#15gsgshshsah" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Caso Malicioso
    def testHashValidoClaveVacia(self):
        object = clsAccessControl()
        password = "" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Caso Malicioso
    def testHashValidoClaveConSoloEspacios(self):
        object = clsAccessControl()
        password = "        " 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
            
    
