def digito(x, i):
    """Retorna el i-ésimo dígito de x, siendo 0 el índice del primer dígito."""
    x_str = str(x)
    if 0 <= i < len(x_str):
        return int(x_str[i])
    else:
        return -1

def largo(x):
    """Retorna el número de dígitos de x."""
    return len(str(x))