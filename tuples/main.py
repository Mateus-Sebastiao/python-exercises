#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Título: Exercício sobre Tuplas (Python)

Descrição:
Este script demonstra operações básicas com tuplas em Python, 
como acesso, alteração e iteração de elementos.

Autor: Mateus Sebastião
Data: 29/04/2025
"""

def main():
    # Criação de uma tupla
    frutas = ('maçã', 'banana', 'laranja')
    print(f"Tupla inicial: {frutas}\n")

    # Acessando um item específico da tupla
    print(f"Este é o segundo item da tupla: {frutas[1]}\n")

    # Mudando o valor de um item específico da tupla
    frutasTemporarias = list(frutas)
    frutasTemporarias[1] = "cereja"
    frutas = tuple(frutasTemporarias)
    print(f"Tupla após a alteração: {frutas}\n")

    # Percorrendo a tupla
    print("Percorrendo a tupla:")
    for fruta in frutas:
        print(f"- {fruta}")
        if fruta == frutas[-1]: # Adiciona uma quebra de linha se fruta for o último item da lista
            print("")

    # Verificando se um item específico da tupla existe
    if "maçã" in frutas:
        print("Sim, 'maçã' está na tupla!\n")
    
    # Obtendo o comprimento de uma lista
    print(f"Comprimento da tupla: {len(frutas)}\n")

    # Removendo a tupla
    del frutas
    print(f"Após remover a tupla: {frutas}\n") # Vai gerar um erro porque a tupla não existe!



if __name__ == "__main__":
    main()
