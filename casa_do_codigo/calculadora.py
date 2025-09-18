#MANIPULACÕES BASICAS EM PYTHON
    #operadores de comparação
        # • < – menor que;
        # • <= – menor ou igual que;
        # • > – maior que;
        # • >= – maior ou igual;
        # • == – igual;
        # • != – não igual.

salario = int(input("Salario: "))
imposto = input("Imposto em % ? (exemplo 27.5 ou deixe em branco para calcular):")
if not imposto:
     if salario > 4664.68:
         imposto = 27.5
     elif salario > 3751.06:
        imposto = 22.5
     elif salario > 2826.66:
        imposto = 15.0
     elif salario > 2428.81:
        imposto = 7.5
     else:
         imposto = 0.0
else:
    imposto = float(imposto)


print ("valor liquido: {0}".format(salario - (salario * (imposto * 0.01))))


