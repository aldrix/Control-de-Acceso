# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Patricia Valencia
         Aldrix Marfil
'''

import unittest
from mdlaccesscontrol import clsAccessControl

class Testlength_password(unittest.TestCase):

    #Caso Frontera 
    
    #Caso 1: String de longitud 8
    def testLongitud8Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.R"
        result = object.length_password(string) 
        self.assertEqual(result,8,"Longitud Inv�lida")
        
    #Caso 2: String de longitud 16
    def testLongitud16Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.RF23pwQsx"
        result = object.length_password(string) 
        self.assertEqual(result,16,"Longitud Inv�lida")

    #Caso 3: String vacío
    def testLongitudStringVacio(self):
        object = clsAccessControl()
        string = ""
        result = object.length_password(string) 
        self.assertEqual(result,0,"Longitud Inv�lida")
        
    #Caso 4: String muy grande, longitud (2^31)-1
    def testLongitudMasGrande(self):
        object = clsAccessControl()
        string = ((2**31)-1)*"p"
        result = object.length_password(string) 
        self.assertEqual(result,(2**31)-1,"Longitud Inv�lida")
        
        
    #Caso Esquina
    
    #Caso 5: String de longitud 7
    def testLongitud7Caracteres(self):
        object = clsAccessControl()
        string = "acD34@."
        result = object.length_password(string) 
        self.assertEqual(result,7,"Longitud Inv�lida")
        
    #Caso 6: String de longitud 17
    def testLongitud17Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.1235ufjD.u"
        result = object.length_password(string) 
        self.assertEqual(result,17,"Longitud Inv�lida")
        
    #Caso Normal
    
    #Caso 7: String de longitud 9
    def testLongitud9Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.12"
        result = object.length_password(string) 
        self.assertEqual(result,9,"Longitud Inv�lida")
        
    #Caso 8: String de longitud 15
    def testLongitud15Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.12e87@sh"
        result = object.length_password(string) 
        self.assertEqual(result,15,"Longitud Inv�lida")
        

        