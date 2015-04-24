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
    def testLongitud8Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.R"
        result = object.length_password(string) 
        self.assertEqual(result,8,"Longitud Inválida")
        
    #Caso Frontera 
    def testLongitud16Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.RF23pwQsx"
        result = object.length_password(string) 
        self.assertEqual(result,16,"Longitud Inválida")

    #Caso Frontera
    def testLongitudStringVacio(self):
        object = clsAccessControl()
        string = ""
        result = object.length_password(string) 
        self.assertEqual(result,0,"Longitud Inválida")
        
        
    #Caso Esquina
    def testLongitud7Caracteres(self):
        object = clsAccessControl()
        string = "acD34@."
        result = object.length_password(string) 
        self.assertEqual(result,7,"Longitud Inválida")
        
    #Caso Esquina
    def testLongitud17Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.1235ufjD.u"
        result = object.length_password(string) 
        self.assertEqual(result,17,"Longitud Inválida")
        
    #Caso Normal
    def testLongitud9Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.12"
        result = object.length_password(string) 
        self.assertEqual(result,9,"Longitud Inválida")
        
    #Caso Normal
    def testLongitud15Caracteres(self):
        object = clsAccessControl()
        string = "acD34@.12e87@sh"
        result = object.length_password(string) 
        self.assertEqual(result,15,"Longitud Inválida")
        
    def testLongitudMasGrande(self):
        object = clsAccessControl()
        string = ((2**31)-1)*"p"
        result = object.length_password(string) 
        self.assertEqual(result,(2**31)-1,"Longitud Inválida")
        