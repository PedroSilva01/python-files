kmPorLitroAlcohol = float(input('quantos km o seu automovel faz por litro de alcoll: ').replace('r', '0'))
kmPorLitroGasoline = float(input('quantos km o seu automovel faz por litro de gasolina: '))
PricePerAlcoholLiter = float(input('quanto custa o litro de alcol: '))
PricePerGasolineLiter = float(input('quanto custa o litro de gasosa: '))
if kmPorLitroAlcohol and kmPorLitroGasoline > 0 :
    if PricePerAlcoholLiter and PricePerGasolineLiter > 0:
        result = float(PricePerAlcoholLiter/PricePerGasolineLiter)
        if result >= 0.7:
            print('A gasolina está com maior custo beneficio')
        else:
            print('o Alcoll está com um melhor custo beneficio')
    else:
        print('error')
else:
    print('error')
