def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    if n in fib_seq:
        return fib_seq
    else:
        return None

numero = int(input("Informe um número: "))

sequencia_fibonacci = fibonacci(numero)

if sequencia_fibonacci:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
    print(f"Sequência de Fibonacci gerada: {sequencia_fibonacci}")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")



