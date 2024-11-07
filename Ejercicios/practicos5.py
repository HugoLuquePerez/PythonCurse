def fibonacci(num):
    a,b = 0,1
    fibonacciLista = []
    for i in range(num):
        if b > num: return num
        else:
            fibonacciLista.append(b)
            a,b = b,a+b
    return fibonacciLista
resultado = fibonacci(20)
print(resultado)