#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Manoel Vitor
#
# Created:     28/01/2019
# Copyright:   (c) Manoel Vitor 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from ctypes import*

dll = cdll.LoadLibrary("math2.dll")

x = input(">> Digite o valor de x:")
y = input(">> Digite o valor de y:")

resultado = dll.soma(x, y)

print(resultado)
