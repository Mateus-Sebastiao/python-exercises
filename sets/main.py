#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Título: Exercício sobre Conjuntos (Python)

Descrição:
Este script demonstra operações básicas com conjuntos em Python, 
como acesso, alteração e iteração de elementos.

Autor: Mateus Sebastião
Data: 29/04/2025
"""

def main():
    # Criação de um conjunto
    frutas = {'maçã', 'banana', 'laranja'}
    print(f"Conjunto inicial: {frutas}\n")

    # Acessando um item específico do conjunto
    
    # Mudando o valor de um item específico do conjunto
    
    # Percorrendo o conjunto
    print("Percorrendo o Conjunto:")
    for fruta in frutas:
        print(f"- {fruta}")
    
    # Quebra de linha
    print("")

    # Verificando se um item específico do Conjunto existe
    if "maçã" in frutas:
        print("Sim, 'maçã' está no Conjunto!\n")
    
    # Obtendo o comprimento do conjunto
    print(f"Comprimento do Conjunto: {len(frutas)}\n")

    # Adicionando elementos
    frutas.add('uva')
    print(f"Após adicionar 'uva', o conjunto: {frutas}\n")

    # Adicionando vários items
    frutas.update(["manga", "morango", "cereja"])

    # Removendo elementos
    frutas.remove('cereja')
    print(f"Após remover 'cereja': {frutas}\n")

    # Removendo um item usando o método discard()
    frutas.discard('manga')
    print(f"Após remover 'manga': {frutas}\n")

    # Removendo o último item
    x = frutas.pop() # O item removido
    print(x)
    print(f"O conjunto após remoção do item: {frutas}\n")

    # Esvaziando o conjunto
    frutas.clear()
    print(f"Conjunto após ser esvaziado: {frutas}\n")

    # Removendo o Conjunto
    del frutas
    print(f"Após remover o Conjunto: {frutas}\n") # Vai gerar um erro porque o Conjunto não existe!



if __name__ == "__main__":
    main()
