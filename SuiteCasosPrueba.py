# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Patricia Valencia
         Aldrix Marfil
'''

import unittest
from mdlaccesscontrol import clsAccessControl

class TestEncript(unittest.TestCase):

    #Caso Frontera
    def testClaveValidalong8(self):
        object = clsAccessControl()
        string = "Hola123*"
        result = object.encript(string) 
        self.assertTrue(result,"Clave Invalida")
    
    #Caso Frontera    
    def testclaveValidalong16(self):
        object = clsAccessControl()
        string = "Estoes1prueb@.Xy"
        result = object.encript(string) 
        self.assertTrue(result,"Clave Invalida")   
        
    #Caso Frontera
    def testClaveInvalidalong7(self):
        object = clsAccessControl()
        string = "clave#7"
        result = object.encript(string) 
        self.assertFalse(result,"Clave inválida")

    #Caso Frontera        
    def testClaveInvalidalong17(self):
        object = clsAccessControl()
        string = "Clavede#17digitos"
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")

     #Caso Normal
    def testClaveValidaSinMinusculas(self):
        object = clsAccessControl()
        string = "1XZABC@W"
        result = object.encript(string) 
        self.assertTrue(result, "Clave Invalida")
        
    #Caso Esquina
    def testClaveFaltaMayuscula(self):
        object = clsAccessControl()
        string = "hola156#"
        result = object.encript(string)
        self.assertFalse(result,"Clave válida") 
        
    #Caso Esquina
    def testclaveSoloNumerosUnaMayusculaUnCaracter(self):
        object = clsAccessControl()
        string = "123$4568965P"
        result = object.encript(string) 
        self.assertTrue(result, "Clave Invalida")
        
    #Caso Esquina
    def testClaveFaltanLetras(self):
        object = clsAccessControl()
        string = "1234#567."
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")
        
    #Caso Esquina
    def testClaveFaltanNumeros(self):
        object = clsAccessControl()
        string = ".abCD$ef"
        result = object.encript(string)
        self.assertFalse(result,"Clave válida") 
        
    #Caso Esquina
    def testClaveFaltanCaracteresEspeciales(self):
        object = clsAccessControl()
        string = "4ald56Z"
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")
        
    #Caso Malicioso
    def testClaveVacia(self):
        object = clsAccessControl()
        string = ""
        result = object.encript(string)
        self.assertEqual(result,"")
        
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
    def testClaveLargo8ConSoloLetras(self):
        objeto = clsAccessControl()
        cadena = "abcdefgh"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Caso Malicioso
    def testClaveLargo8ConSoloCaracteres(self):
        objeto = clsAccessControl()
        cadena = "#$.*+@++"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
        
############################################################################################################
        
#     Caso Esquina
#     def testclaveSoloCaracteresEspecialesUnaMayusculaUnNumero(self):
#         object = clsAccessControl()
#         string = "@*+.$+-%&9L"
#         result = object.encript(string) 
#         self.assertFalse(result, "Clave Invalida")




   