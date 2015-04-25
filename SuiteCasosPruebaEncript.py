# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Patricia Valencia
         Aldrix Marfil
'''
import unittest
from mdlaccesscontrol import clsAccessControl

class TestEncript(unittest.TestCase):

    #Casos Fronteras
    
    #Caso 1: Clave que cumple con los requisitos y de longitud 8.
    def testClaveValidalong8(self):
        object = clsAccessControl()
        string = "Hola123*"
        result = object.encript(string) 
        self.assertTrue(result,"Clave Invalida")
    
    #Caso 2: Clave que cumple con los requisitos y de longitud 16.
    def testclaveValidalong16(self):
        object = clsAccessControl()
        string = "Estoes1prueb@.Xy"
        result = object.encript(string) 
        self.assertTrue(result,"Clave Invalida")   
        
    #Caso 3: Clave que cumple con los requisitos y de longitud 7.
    #       (Frontera externa del dominio de la funcion)
    def testClaveInvalidalong7(self):
        object = clsAccessControl()
        string = "clav1#7"
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")

    #Caso 4: Clave que cumple con los requisitos y de longitud 17.
    #        (Frontera externa del dominio de la funcion)         
    def testClaveInvalidalong17(self):
        object = clsAccessControl()
        string = "Clavede#17digitos"
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")
        
    
    # Casos Esquina
    
    #Caso 5: Clave de longitud 8 con ausencia de mayusculas.
    def testClaveFaltaMayuscula(self):
        object = clsAccessControl()
        string = "hola156#"
        result = object.encript(string)
        self.assertFalse(result,"Clave válida") 
        
    #Caso 6: Clave de longitud 8 con asusencia de letras.
    def testClaveFaltanLetras(self):
        object = clsAccessControl()
        string = "1234#567."
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")
        
    #Caso 7: Clave de longitud 8 con ausencia de numeros.
    def testClaveFaltanNumeros(self):
        object = clsAccessControl()
        string = ".abCD$ef"
        result = object.encript(string)
        self.assertFalse(result,"Clave válida") 
        
    #Caso 8: Clave de longitud 8 con ausencia de caracteres especiales.
    def testClaveFaltanCaracteresEspeciales(self):
        object = clsAccessControl()
        string = "4ald56Z"
        result = object.encript(string) 
        self.assertFalse(result,"Clave válida")
        
        
    #Casos Normales
    
    #Caso 9: Clave que cumple con los requisitos y de longitud 10.
    def testClaveValidaLargo10(self):
        objeto = clsAccessControl()
        cadena = "h*l4Any$91"
        resultado = objeto.encript(cadena)
        self.assertTrue(resultado,"La clave no es valida.")
       
    #Caso 10: Clave que no contiene letras minusculas y cumple con los requisitos.
    def testClaveValidaSinMinusculas(self):
        object = clsAccessControl()
        string = "1XZABC@W"
        result = object.encript(string) 
        self.assertTrue(result, "Clave Invalida")
        
    #Caso 11: Clave de longitud 11 que cumple con los requisitos.
    def testClaveValidaSoloCaracteresEspecialesUnaMayusculaUnNumero(self):
        object = clsAccessControl()
        string = "@*+.1$+#.L%"
        result = object.encript(string) 
        self.assertTrue(result, "Clave válida")
 
    #Caso 12: Clave de longitud 12 que cumple con los requisitos.
    def testclaveSoloNumerosUnaMayusculaUnCaracterEspecial(self):
        object = clsAccessControl()
        string = "123$4568965P"
        result = object.encript(string) 
        self.assertTrue(result, "Clave Invalida")
        
        
    #Casos Maliciosos
    
    #Caso 13: Clave sin caracteres de ningun tipo.
    def testClaveVacia(self):
        object = clsAccessControl()
        string = ""
        result = object.encript(string)
        self.assertFalse(result,"Clave Valida")
        
    #Caso 14: Clave con solo 8 espacios.
    def testClaveLargo8ConSoloEspacios(self):
        objeto = clsAccessControl()
        cadena = "        "
        resultado = objeto.encript(cadena)
        self.assertFalse(resultado,"Clave Valida")
        
    #Caso 15: Clave de longitud 9 que tiene un espacio entre dos palabras.
    def testClaveLargo8ConCaracterEspacio(self):
        objeto = clsAccessControl()
        cadena = "Alifo 13#"
        resultado = objeto.encript(cadena)
        self.assertFalse(resultado,"Clave Valida")
        
    #Caso 16: Clave de longitud 8 que contiene un caracter \t no imprimible
    def testClaveLargo8ConCaracterNoImprimible(self):
        objeto = clsAccessControl()
        cadena = "Alif13m\t"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Caso 17: Clave de longitud 8 que contiene solo numeros.       
    def testClaveLargo8ConSoloNumeros(self):
        objeto = clsAccessControl()
        cadena = "56789142"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Caso 18: Clave de longitud 8 que contiene solo letras minusculas.        
    def testClaveLargo8ConSoloLetras(self):
        objeto = clsAccessControl()
        cadena = "abcdefgh"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
        
    #Caso 19: Clave de longitud 8 que contiene solo letras mayusculas.        
    def testClaveLargo8ConSoloLetrasMayusculas(self):
        objeto = clsAccessControl()
        cadena = "ABCDEFGH"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")

    #Caso 20: Clave de longitud 8 que contiene solo caracteres especiales.
    def testClaveLargo8ConSoloCaracteres(self):
        objeto = clsAccessControl()
        cadena = "#$.*+@++"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
        
    #Caso 21: Clave inválida con caracteres diferentes a los solicitados 
    def testClaveInvalidaCaractereSIncorrectos(self):
        objeto = clsAccessControl()
        cadena = "Gft%u!i56*"
        resultado = objeto.encript(cadena)
        self.assertEqual(resultado,"")
    