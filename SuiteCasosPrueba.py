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
        
    #Caso Normal 
    def testClaveValidaLargo10(self):
        objeto = clsAccessControl()
        cadena = "h*l4Any$91"
        resultado = objeto.encript(cadena)
        self.assertTrue(resultado,"La clave no es valida.")
    
    #Caso Malicioso
    def testClaveLargo8ConSoloEspacios(self):
        objeto = clsAccessControl()
        cadena = "        "
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
        
    #Caso Malicioso
    def testClaveLargo8ConCaracterEspacio(self):
        objeto = clsAccessControl()
        cadena = "Alifo 13#"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
        
    #Caso Malicioso
    def testClaveLargo8ConCaracterNoImprimible(self):
        objeto = clsAccessControl()
        cadena = "Alif13m\t"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Caso Malicioso        
    def testClaveLargo8ConSoloNumeros(self):
        objeto = clsAccessControl()
        cadena = "56789142"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Caso Malicioso        
    def testClaveLargo9ConSoloLetras(self):
        objeto = clsAccessControl()
        cadena = "#$.*+@4+*#"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Caso Malicioso
    def testClaveLargo10ConSoloCaracteres(self):
        objeto = clsAccessControl()
        cadena = "#$.*+@4+*#"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

