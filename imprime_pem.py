# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:21:37 2020

@author: Mr ABBAS-TURKI
"""

import pem

certs = pem.parse_file("ca-cle-publique.pem")
print(certs)
print(str(certs[0]))

certs = pem.parse_file("serveur-cle-publique.pem")
print(certs)
print(str(certs[0]))