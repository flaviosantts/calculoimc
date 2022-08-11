# CRIANDO UM SISTEMA DE CALCULO DO ÍNCICI DE MASSA CORPRAL:

# IMPORTANDO O MODULO OS:
import os                                                                                     # IMPORTANDO O MODULO
BOAS_VINDAS = "OLÁ CARO USUÁRIO, SEJA BEM -VINDO AO SISTEMA DE CALCULO DE ÍNDICE CORPORAL" 
print(BOAS_VINDAS)  
nome = input("Digite o seu nome para começar:  ")                                             # VARIÁVEL INPUT NOME, SERÁ INSERIDO O SEU NOME
altura =  float(input("Nos informe a sua altura em metros:  "))                               # VARIÁVEL INPUT ALTURA, SERÁ INSERIDO A SUA ALTURA
peso = float(input("Informe o seu peso em Kg:  "))                                            # VARIÁVEL INPUT PESO, SERÁ INSERIDO O SEU PESO
imc = peso / altura ** 2                                                                      # Variavél IMC: Calculando o seu IMC(PESO / ALTURA ** A 2)
print(nome, 'SEU IMC É DE:%.4f' % imc)                                                        # Camando na tela as variavéis, nome e IMC
if imc < 16:                                                                                  # Condição: IF (se) o IMC for < 16 ("Magreza grave")
  print("ALERTA PARA O SEU IMC, MAGREZA GRAVE: ")                                               
elif imc < 17:                                                                                # Condição: ELIF (caso-contário) o IMC for < 17 ("Magreza moderada")
  print("MAGREZA MODERADA")
elif imc < 18.5:                                                                              # Condição: ELIF (caso-contário) o IMC for < 18.5 (""Magreza leve")
  print("MAGREZA LEVE, REAVALI A SUA ALIMENTAÇÃO: ")
elif imc < 25:                                                                                # Condição: ELIF (caso-contário) o IMC for < 25 ("Saudável")       
 print("O SEU ESTADO DE SAÚDE É SAUDÁVEL: ")
elif imc < 30:                                                                                # Condição: ELIF (caso-contário) o IMC for < 30 ("Sobrepeso")  
  print("ATENÇÃO, SOBREPESO:  ")
elif imc < 35:                                                                                # Condição: ELIF (caso-contário) o IMC for < 35 ("Obesidade Grau I")
  print("CUIDADO, OBSIDADE DE I GRAU: ")    
elif imc < 40:                                                                                # Condição: ELIF (caso-contário) o IMC for < 40 ("Obesidade Grau II (severa)")
  print("ALERTA, OBSIDADE DE II GRAU:(SEVERA) ")
else:                                                                                         # Condição: ELSE(caso-contário) o IMC for < 40 ("Obesidade Grau III (mórbida)")                                                                                                                                                                                  
  print("ALERTA MÁXIMO, OBSIDADE DE III  (MORBIDA)")

os.system                                                                                     # Dá pausa