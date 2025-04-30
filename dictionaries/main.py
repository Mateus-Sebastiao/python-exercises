#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Título: Exercício sobre Dicionários (Python)

Descrição:
Este script demonstra operações básicas com dicionários em Python, 
como acesso, alteração e iteração de elementos.

Autor: Mateus Sebastião
Data: 29/04/2025
"""

def main():
    # Criação de um dicionário
    carro =	{
        "marca": "Ford",
        "modelo": "Mustang",
        "ano": 1964
    }
    print(f"Dicionário inicial: {carro}\n")

    # Acessando os itens
    print(carro["modelo"], "\n")

    # Alterando o valor de um item
    carro["ano"] = 2018
    print(f"Dicionário após a alteração: {carro}\n")

    # Imprimindo os nomes das chaves
    for chave in carro:
        print(f"- {chave}")

    # Quebra de linha
    print("\n")

    # Imprimindo os valores
    for valor in carro:
        print(f"- {carro[valor]}")

    # Quebra de linha
    print("\n")

    # Usando a função values() para imprimir os valores
    for valor in carro.values():
        print(f"- {valor}")

    # Quebra de linha
    print("\n")

    # Imprimindo o par chave:valor usando a função items()
    for chave, valor in carro.items():
        print(f"{chave} : {valor}")

    # Quebra de linha
    print("\n")

    # Verificando se um item específico do dicionário existe
    if "modelo" in carro:
        print("Sim, 'modelo' está no dicionário!\n")

    # Obtendo o comprimento do dicionário
    print(f"Comprimento do dicionário: {len(carro)}\n")

    # Removendo elementos
    carro.pop('modelo')
    print(f"Após remover a chave 'modelo': {carro}\n")

    # Esvaziando o dicionário
    carro.clear()
    print(f"Dicionário após ser esvaziado: {carro}\n")


if __name__ == "__main__":
    main()
