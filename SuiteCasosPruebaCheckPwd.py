# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Patricia Valencia
         Aldrix Marfil
'''

import unittest
from mdlaccesscontrol import clsAccessControl

class Testcheck_password(unittest.TestCase):
 
    #Caso Frontera
    
    #Caso 1: Clave válida de longitud 8, con su hash correspondiente
    def testHashValidoCorrespodeAClaveCorrectaLong8(self):
        object = clsAccessControl()
        password = "1XZABC@W"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")
        
    #Caso 2:Clave válida de longitud 16, con su hash correspondiente
    def testHashValidoCorrespodeAClaveCorrectaLong16(self):
        object = clsAccessControl()
        password = "1abcdXZABC@W123@"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")
        
    #Caso 3: Clave Inválida (falta de letra mayúscula), con un hash 
    #generado de una clave válida
    def testHashValidoClaveInvalida(self):
        object = clsAccessControl()
        password = "abcd@123" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Caso Normal
    
    #Caso 4: Clave válida de longitud 10, con su hash correspondiente
    def testHashValidoCorrespondeAClaveCorrectaLong10(self):
        object = clsAccessControl()
        password = "fggA#123.s"
        encriptar = object.encript(password)
        result = object.check_password(encriptar,password)
        self.assertTrue(result,"Clave Invalida")

    #Caso Esquina
    
    #Caso 5: Clave de longitud 9, con un hash de una clave diferente a la anterior 
    #por solo una letra
    def testHashyClaveDiferentePorUnaLetra(self):
        object = clsAccessControl()
        password = "1ZA3BC@Ws"
        passwordInvalid = "1ZA3C@Ws" 
        encriptar = object.encript(passwordInvalid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Caso 6: Clave de longitud 7 con su hash correspondiente
    def testHashValidoClaveLong7(self):
        object = clsAccessControl()
        password = "xYz2#15" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
     
     #Caso 7: Clave de longitud 17 con su hash correspondiente
    def testHashValidoClaveLong17(self):
        object = clsAccessControl()
        password = "xYz2#15gsgshshsah" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Caso Malicioso
    
    #Caso 8: Clave sin caracteres de ningún tipo, con hash de una clave válida
    def testHashValidoClaveVacia(self):
        object = clsAccessControl()
        password = "" 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
        
    #Caso 9: Clave de string vacio, con hash de una clave válida
    def testHashValidoClaveConSoloEspacios(self):
        object = clsAccessControl()
        password = "        " 
        passwordValid = "ABCD@123"
        encriptar = object.encript(passwordValid)
        result = object.check_password(encriptar,password)
        self.assertFalse(result,"Clave Valida")
            
    
