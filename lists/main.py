#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Título: Exercício sobre Listas (Python)

Descrição:
Este script demonstra operações básicas com listas em Python, 
como adição, remoção e iteração de elementos.

Autor: Mateus Sebastião
Data: 29/04/2025
"""

def main():
    # Criação de uma lista
    frutas = ['maçã', 'banana', 'laranja']
    print(f"Lista inicial: {frutas}\n")

    # Acessando um item específico da lista
    print(f"Este é o segundo item da lista: {frutas[1]}\n")

    # Mudando o valor de um item específico da lista
    frutas[1] = "cereja"
    print(f"Lista após a alteração: {frutas}\n")

    # Percorrendo a lista
    print("Percorrendo a lista:")
    for fruta in frutas:
        print(f"- {fruta}")
        if fruta == frutas[-1]: # Adiciona uma quebra de linha se fruta for o último item da lista
            print("")

    # Verificando se um item específico da lista existe
    if "maçã" in frutas:
        print("Sim, 'maçã' está na lista!\n")
    
    # Obtendo o comprimento de uma lista
    print(f"Comprimento da lista: {len(frutas)}\n")

    # Adicionando elementos
    frutas.append('uva')
    print(f"Após adicionar 'uva', a lista: {frutas}\n")

    # Adicionando elementos numa posição específica
    frutas.insert(1, "manga")
    print(f"Lista após adicionar manga na segunda posição: {frutas}\n")

    # Removendo elementos
    frutas.remove('cereja')
    print(f"Após remover 'cereja': {frutas}\n")

    # Removendo o último item
    frutas.pop()
    print(f"Apó remover o último item: {frutas}\n")

    # Removendo um item num índice especificado
    del frutas[0]
    print(f"Após remover o primeiro item: {frutas}\n")


    # Usando o construtor list() para passar uma lista para uma nova
    frutasNovas = list(frutas)
    print(f"Nova lista: {frutasNovas}\n")

    # Esvaziando a lista
    frutas.clear()
    print(f"Lista após ser esvaziada: {frutas}\n")

if __name__ == "__main__":
    main()
