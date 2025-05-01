#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Título: Exercício sobre Funçoes (Python)

Descrição: Exercício prático que envolve funções.
Criar um programa com uma função que calcula o valor final de uma compra com desconto,
de acordo com o valor total.

Autor: Mateus Sebastião
Data: 01/04/2025
"""

def main():
    def calcularDesconto(valor_compra):
        desconto = valor_compra

        if valor_compra <= 5000:
            desconto *= 0.05
        elif valor_compra > 5000 and valor_compra <= 25000:
            desconto *= 0.1
        else:
            desconto *= 0.15

        valorFinal = valor_compra - desconto
        return valorFinal

    while True:
        entrada = input(f"Digite o valor da compra ou 'sair': ")

        if entrada.lower() == 'sair':
            print('Encerrando o programa.')
            break
        elif entrada != 'sair':
            valor_compra = float(entrada)
            valorFinal = calcularDesconto(valor_compra)
            print(f"Valor final com desconto: Kz {valorFinal:.2f}")

if __name__ == "__main__":
    main()