imposto = float(input("Imposto: "))

if imposto < 10.:
    print("baixo")
elif imposto >= 10. and imposto <= 27.:
    print("medio")
else:
    print("imposto invalido")