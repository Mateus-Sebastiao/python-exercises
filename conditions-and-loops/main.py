#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Título: Exercício sobre Condicionais e Loops (Python)

Descrição: Exercício prático que envolve condicionais (if, elif, else) e loops (for e while).
Criar um programa onde o usuário tem que adivinhar um número secreto entre 1 e 10. Ele terá no máximo 5 tentativas. 
Após cada tentativa, o programa deve informar se o número é maior, menor ou igual ao número secreto.


Autor: Mateus Sebastião
Data: 30/04/2025
"""

def main():
    numero_secreto = 7

    for tentativa in range(1, 6):
        numero = int(input(f"Tentativa {tentativa}: Qual é o número secreto entre 1 a 10? "))

        if numero == numero_secreto:
            print("Parabéns! Você acertou o número secreto!")
        elif numero > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("O número secreto é maior.")

if __name__ == "__main__":
    main()