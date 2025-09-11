#MANIPULACÕES BASICAS EM PYTHON
    #operadores de comparação
        # • < – menor que;
        # • <= – menor ou igual que;
        # • > – maior que;
        # • >= – maior ou igual;
        # • == – igual;
        # • != – não igual.

imposto = float(input("Imposto: "))
salario = float(input("Salario: "))
print ("valor liquido: {0}".format(salario - (salario * (imposto * 0.01))))