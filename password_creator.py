#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Author: eduar766
import random
import string

def crear_pass(n):
    allChars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    passphrase = []

    for i in range(n):
        tmp = random.choice(allChars)
        passphrase.append(tmp)
    
    res = "".join(passphrase)
    return res

n = input("Ingresa ancho de Password: ")
test = crear_pass(n)
try:
    print(test)
except:
    print("Debe ingresar el ancho del Password")
