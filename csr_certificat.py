# -*- coding: utf-8 -*-
"""
Created on Mon May 11 07:06:46 2020

@author: Mr ABBAS-TURKI
"""


from PKI_utile import generate_csr, generate_private_key

cle_privee_serveur = generate_private_key("cle-privee-serveur.pem", "server_password")

generate_csr(cle_privee_serveur, "serveur-csr.pem", country="FR", state="france", locality="Paris", org="SR73 SA.", hostname="Moi meme")