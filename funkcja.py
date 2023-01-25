"""Klasa przechowujaca funkcje"""

import math

class Funkcja:
  
    def __init__(self):
        """Konstruktor klasy Funkcja"""
        pass
    
    def wartosc(self, x):
        """Metoda obliczajaca wartosc funkcji w punkcie x"""
        wart = 4*math.sin(81*x+ 6)+math.sqrt(6+x*x) #wpisac tu swoja funckje
        return wart
    
    
