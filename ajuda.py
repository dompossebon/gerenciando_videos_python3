pessoa = {}

locate = 0

mulher = 0

homen = 0

ordinal = 0

num_mulher = 0

num_homem = 0

quantity = int(input("quantidade de pessoas a registrar >> "))

for n in range(quantity):
    print("{} ⁰ pessoa".format(ordinal + 1))
    strlocate = str(ordinal + 1)

    variavel_x = "p" + strlocate

    if ordinal == 0:
        pessoa["response"] = {variavel_x: {"Nome": input("nome >> ").title()}}
    else:
        pessoa["response"].update({variavel_x: {"Nome": input("nome >> ")}})


    pessoa["response"][variavel_x].update({"Idade": int(input("idade >> "))})

    print("informe o sexo:\nm (masculino)\nf (feminina)")

    pessoa["response"][variavel_x].update({"Sexo": input("sexo >> ").lower()})

    pessoa["response"][variavel_x].update({"Peso": float(input("peso >> "))})

    print('-__ Verifique as Informações Digitadas __-')
    print(pessoa["response"][variavel_x])
    print('-_-_-')

    locate += 1

    ordinal += 1

    if (pessoa["response"][variavel_x]["Sexo"] == 'f'):
        num_mulher += 1

    elif (pessoa["response"][variavel_x]["Sexo"] == 'm'):
        num_homem += 1

print('Foi informado :', num_mulher, 'mulher')

print('Foi informado :', num_homem, 'Homem')

print('————————————————————————————————————————————————————————————————————————')

print('**- GeRaLzÃo -**')
print(pessoa["response"])
print('*****')
