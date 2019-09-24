
def add(x, y):
    """Add function"""
    return x + y


def substract(x, y):
    """Substract function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('You can`t divide by zero...')
    return x / y
