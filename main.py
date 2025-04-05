def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Cerem primul număr o singură dată, înainte de buclă
nr_1 = float(input("Primul număr: "))

# Începem bucla
while True:
    operation = input("Operatorul (+, -, *, /): ")
    nr_2 = float(input("Al doilea număr: "))

    result = operations[operation](nr_1, nr_2)
    print(f"Rezultatul este: {result}")

    continuare = input('Vrei să continui cu rezultatul? Scrie "Y" pentru da, "N" pentru nu: ').upper()

    if continuare == "Y":
        nr_1 = result
    else:
        nr_1 = float(input("Introdu un nou prim număr: "))
