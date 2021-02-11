# -*- coding: utf-8 -*-
"""
Created on Mon May 11 06:57:17 2020

@author: Mr ABBAS-TURKI
"""

from PKI_utile import generate_private_key, generate_public_key

private_key = generate_private_key("ca-cle-privee.pem", "password")

generate_public_key(private_key, "ca-cle-publique.pem", country="FR", state="france", locality="Paris", org="SR73 SA.", hostname="Moi meme")