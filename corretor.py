from moduloCorr import *

continua = True
gab = False
prov = False

while (continua):
	print ("Entre com a opção desejada:")
	print ("1 - Carregar gabarito")
	print ("2 - Carregar prova")
	print ("3 - Gerar correção")
	print ("4 - Sair")
	resp = input("Opção: ")
	resp = int(resp)
	if (resp < 1 or resp > 4):
		print("Entrada Inválida:")
		limpaTela()
		continue
	else:
		if (resp == 1):
			if (not gab):
				sGab = lerGabarito("gab.txt")
				print ("Gabarito lido com sucesso")
				gab = True

				continue
			else:
				input("Gabarito já foi lido")
				limpaTela()
				continue
			
		elif (resp == 2):
			if(not prov):
				sProva = lerProva("prova.txt")
				print("Prova lida com sucesso")
				prov = True

				continue
			else:
				input("Prova já foi lida")
				limpaTela()
				continue
			
		elif (resp == 3):
			corrigirProva(sGab, sProva)
			imprimeResultados(sGab, sProva, corrigirProva)

			continue
		else:
			#sair do programa
			s = input("Deseja mesmo sair? [S/N]")
			sair = s.upper()
			if sair == "S":
				continua = False
			else:
				continue

