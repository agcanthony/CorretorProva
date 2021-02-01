import os
import sys


def limpaTela():
	if sys.platform() == "linux2":
		os.system("clear")
	else:
		os.system("cls")


def lerGabarito(nome_arq):
	gab = open(nome_arq, 'rw')
	lendo_txt = gab.readlines()
	ler = []
	for l in lendo_txt:
		ler.append(l.rstrip())
	gab.close()
	return ler


def lerProva(nome_arq):
	prova = open(nome_arq, 'r')
	lendo_prova = prova.readlines()
	ler2 = []
	for l in lendo_prova:
		ler2.append(l.rstrip())
	prova.close()
	return ler2


def corrigirProva (sGab,sProva):
	tam = len(sProva)
	tam2 = len(sGab)
	laco = range(0,tam)
	prova = lerProva("prova.txt")
	gab = lerGabarito("gab.txt")
	resp = []
	for cont in laco:
		resp.append(input("Informe as resposta das questoes: "))
		tam2 = resp.writes()

	acerto = []
	pos_acerto = []
	erro = []
	pos_erro = []

	for r in resp:
		for p in prova:
			if resp[resp.index(p)] == prova[prova.index(p)]:
				acerto.append(r.rstrip())
				pos_acerto.append(resp.index(r))
				print("acertou:", resp.index(p))
				break
			else:
				erro.append(r.rstrip())
				pos_erro.append(gab.index(r))
				break

	print("Resposta: ", gab)
	print("prova: ", prova)


	#implementar
	#recebe as entradas do gabarito e prova
	#retorna uma string de saída
	#corrija a prova
	#string de saída deve conter em cada linha o número da questão e "correto" se estiver correto ou  "incorreto" caso contrário


def imprimeResultados(sGab, sProva, corrigirProva):
	nota = 0
	erro = 0
	resp = []
	prova = lerProva("prova.txt")
	gab = lerGabarito("gab.txt")

	for i in range(len(gab)):  # Soma a nota comparando com o gabarito
		if gab[i] == prova[i]:
			nota += 1
		else:
			erro += 1
	resp.append(gab)
	print("acertos: ",nota)
	print("erros: ", erro)
	#implementar
	#recebe a string de correção
	#imprime em tela quantas respostas estão corretas e quantas estão erradas


def escreverRelatorio(sRelatorio):
	pass
	#implementar
	#recebe a string de correção
	#escreva a string no arquivo "correcao.txt"




