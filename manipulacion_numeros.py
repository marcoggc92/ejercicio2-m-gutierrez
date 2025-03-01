def invertir_numero(n):
    return int(str(n)[::-1])

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def suma_digitos(n):
    return sum(int(digit) for digit in str(n))