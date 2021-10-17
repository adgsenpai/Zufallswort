#!/usr/bin/env python
# coding: utf8



"""
.. module:: generiere-zufallswort
   :synopsis: Generate random german words. 
.. moduleauthor:: Maximilian Freitag
"""


import random as random












def zufallswort():
    print(random.sample(duden))


def zufallswoerter(n):
    print(random.sample(duden, k=n))


def anfangsbuchstaben(m: str, n: int):
    a = list(filter(lambda x: x.lower().startswith(m), duden)) 
    print(random.sample(a, k=n))  


def endbuchstaben(m: str, n: int):
    h = list(filter(lambda x: x.lower().endswith(m), duden)) 
    print(random.sample(h, k=n))
    
    
def enthaelt_buchstaben(m: str, n: int):
      a = list(filter(lambda x: m in x.lower(), duden)) 
      print(random.sample(a, k=n))    


def anzahl_buchstaben(m: int, n: int):    
    
    a = []  
    
    for i in duden:
        if len(i) == m:
            a.append(i)
     
    print(random.sample(a, k=n))




