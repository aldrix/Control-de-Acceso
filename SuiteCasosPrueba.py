# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Patricia Valencia
         Aldrix Marfil
'''

import unittest
from mdlaccesscontrol import clsAccessControl

class TestEncript(unittest.TestCase):

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
       

        

        
    