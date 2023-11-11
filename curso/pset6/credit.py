# Importar a função get_string do módulo CS50
from cs50 import get_string

# Solicitar ao usuário um número de cartão de crédito
cc_number = get_string ( "Number: " )

# Verificar se o cartão é válido usando a fórmula do Luhn
total = 0
parity = len ( cc_number ) % 2
for digit in cc_number :
    if digit.isdigit () :
        if parity == 0 :
            digit = int ( digit ) * 2
            if digit > 9 :
                digit = digit - 9
        else :
            digit = int(digit)
        total += digit
        parity = 1 - parity

# Verificar se o cartão é de alguma das marcas conhecidas
if total % 10 == 0 :
    # Obter os primeiros 2 dígitos (que indicam a marca)
    first_two_digits = int(cc_number[:2])

    # Verificar se é um cartão American Express
    if 34 <= first_two_digits <= 37 :
        print("AMEX")
    # Verificar se é um cartão MasterCard
    elif 51 <= first_two_digits <= 55 :
        print("MASTERCARD")
    # Verificar se é um cartão Visa
    elif 40 <= first_two_digits <= 49 :
        print("VISA")
else :
    print("INVALID")
