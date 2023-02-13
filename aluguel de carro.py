fiatMobi = 98
hondaCivic = 125
fiatTouro = 240

print("Bem vindo á Gustavinho Locadora de carros \n Esses são nossos preços de Diárias \n ---- [1] Fiat Mobi = R$98,00  ---- \n  -----[2] Honda Civic = R$125,00 ---- \n ----[3] Fiat Touro = R$240,00 ----\n")
carroEscolha = int(input("qual carro mais se adapta à sua necessidade: 1, 2 ou 3 (DIGITE APENAS NUMEROS) "))



if carroEscolha == 1:
  dias =  int(input("Você escolheu o Fiat Mobi ----- Quantos dias você pretende usá-lo? (DIGITE APENAS NUMEROS)"))
  precoFinal = dias * fiatMobi
  print("O preço final que o senhor irá pagar pelo aluguel de {} dias. Será {:.2f}".format(dias, precoFinal))
  print("OBRIGADO POR ESCOLHER A GUSTAVINHO LOCADORA")


    
elif carroEscolha == 2:
  dias =  int(input("Você escolheu o Honda Civic ----- Quantos dias você pretende usá-lo? (DIGITE APENAS NUMEROS)"))
  precoFinal = dias *  hondaCivic
  print("O preço final que o senhor irá pagar pelo aluguel de {} dias. Será {:.2f}".format(dias, precoFinal))
  print("OBRIGADO POR ESCOLHER A GUSTAVINHO LOCADORA")
  


elif carroEscolha == 3:
    dias =  int(input("Você escolheu o Fiat Touro----- Quantos dias você pretende usá-lo? (DIGITE APENAS NUMEROS)"))
    precoFinal = dias *  fiatTouro
    print("O preço final que o senhor irá pagar pelo aluguel de {} dias. Será {:.2f}".format(dias, precoFinal))
    print("OBRIGADO POR ESCOLHER A GUSTAVINHO LOCADORA")


else: 
    print("Digite uma opção compatível ")


    
