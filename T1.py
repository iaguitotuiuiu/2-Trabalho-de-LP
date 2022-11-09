#LISTAS
Lnome = []
Lemail = []
Lsenha = []
Lcpf = []
Lnum= []

#VARIAVÉIS
dados = 0
nome = 'vazio'
fm = 1
z = ''
x = 0

#MENU
z = input("Pressione Enter para iniciar:")

while z != 't01':
	print('-'*60)
	print("MENU".center(60))
	print('-'*60)
	print("1-Cadastrar \n2-Ler \n3-Deletar \n4-Atualizar \n5-Sair")
	v = int(input('\nEscolha a opção: '))
	x = v
	z = 't01'
	
	#SAIR DO PROGRAMA
	while x == 5:
		print('-'*60)
		print('Deseja sair do Programa?\n 1-Sim\n 2-Não')
		fm = int(input())
		if fm == 2:
			z = ''
			x = 0
		elif fm == 1:
			v = 5
			x = 3
		else:
			print('Opção inválida!')
			
	#OPÇOES
	while v != 5:
		
		#OPÇÃO INVÁLIDA
		if v > 5 or v == 0:
			print('-'*60)
			print("NÃO EXISTE ESSA OPÇÃO!".center(60))
			print('-'*60)
			z = input('Pressione Enter pra voltar ao menu: ')
			v=5
			
		#CADASTRAR
		elif v == 1:
			print('='*25,'CADASTRO','='*25)
			if len(Lnome) == 0:
				reg = int(input('Quantos registros de cadastro: '))
			else:
				reg = int(input('Quantos novos registros de cadastro: '))
			print('-'*60)
			r = 0
			
			while r < reg:
				print('CADASTRO ',r+1)
				Lnome.append(input('Cadastre seu nome: '))
				Lemail.append(input("Cadastre seu email: "))
				Lsenha.append(input("Cadastre sua senha: "))
				Lcpf.append(int(input("Cadastre seu cpf: ")))
				Lnum.append(int(input("Cadastre seu número de telefone: ")))
				print('-'*60)
				print('Confirmar dados?\n 1-Sim\n 2-Não')
				cfm = int(input())
				if cfm == 1:
					r+=1
				else:
					Lnome.pop(r)
					Lemail.pop(r)
					Lsenha.pop(r)
					Lcpf.pop(r)
					Lnum.pop(r)
					
			print('='*60)
			print('DADOS')
			print('='*60)
			while dados < len(Lnome):
				print('REGISTRO ',dados + 1)
				print('\nNome: ',Lnome[dados])
				print('Email: ',Lemail[dados])
				print('Senha: ',Lsenha[dados])
				print('Cpf: ',Lcpf[dados])
				print('N° de Telefone: ',Lnum[dados])
				print('- '*30)
				dados += 1
			z = input('Pressione Enter pra voltar ao menu: ')
			v = 5
			
		#LER
		elif v == 2:
			if len(Lnome) == 0:
				print('SEM REGISTROS ! ! !')
				v = 5
				z = ''
			else:
				print('='*25, 'REGISTROS', '='*24)
				for element in range(len(Lnome)):
					print('Registro ',element+1,':')
					print('-'*60)
					print(' Nome: ',Lnome[element],'\n Email: ',Lemail[element],'\n Senha: ',Lsenha[element],'\n Cpf: ',Lcpf[element],'\n N° de telefone: ',Lnum[element])
					print('-'*60)
				z = input('Pressione Enter pra voltar ao menu: ')
				v = 5
				
		#DELETAR
		elif v == 3:
			if len(Lnome) == 0:
				print('SEM REGISTROS ! ! !')
				v = 5
				z = ''
			else:
				print('='*25, 'DELETAR', '='*26)
				print('Registro - [Opção]')
				print('-'*60)
				for element in range(len(Lnome)):
					print('Registro - ',element+1,':')
					print('- '*30)
					print(' Nome: ',Lnome[element],'\n Email: ',Lemail[element],'\n Senha: ',Lsenha[element],'\n Cpf: ',Lcpf[element],'\n N° de telefone: ',Lnum[element])
					print('-'*60)
				print('--> Digite 0 para apagar todos os registros! \n')
				ap = int(input('Qual registro deseja deletar? '))
				if ap == 0:
					Lnome = []
					Lemail = []
					Lsenha = []
					Lcpf = []
					Lnum= []
					print('DELETADO TODOS OS REGISTROS !')
				else:
					Lnome.pop(ap-1)
					Lemail.pop(ap-1)
					Lsenha.pop(ap-1)
					Lcpf.pop(ap-1)
					Lnum.pop(ap-1)
					print('\nDELETADO !')
				v = 5
				z = ''
				
		#ATUALIZAR
		elif v == 4:
			if len(Lnome) == 0:
				print('SEM REGISTROS ! ! !')
				v = 5
				z = ''
			else:
				print('='*24, 'ATUALIZAR', '='*25)
				print('Registro - [Opção]')
				print('-'*60)
				for element in range(len(Lnome)):
					print('Registro - ',element+1,':')
					print('- '*30)
					print(' Nome: ',Lnome[element],'\n Email: ',Lemail[element],'\n Senha: ',Lsenha[element],'\n Cpf: ',Lcpf[element],'\n N° de telefone: ',Lnum[element])
					print('-'*60)
				print('--> Digite 0 para atualizar todos os registros! \n')
				at = int(input('Qual registro deseja atualizar? '))
				print('-'*60)
				if at == 0:
					Ln = Lnome
					Le = Lemail
					Ls = Lsenha
					Lc = Lcpf
					Lnu = Lnum
					
					Lnome = []
					Lemail = []
					Lsenha = []
					Lcpf = []
					Lnum= []
					
					for h in range(len(Ln)):
						print('-'*60)
						print('CADASTRO ',h+1)
						Lnome.append(input('Novo nome: '))
						Lemail.append(input("Novo email: "))
						Lsenha.append(input("Nova senha: "))
						Lcpf.append(int(input("Novo cpf: ")))
						Lnum.append(int(input("Novo número de telefone: ")))
						print('-'*60)
				else:
						a = Lnome[at-1]
						b = Lemail[at-1]
						c = Lsenha[at-1]
						d = Lcpf[at-1]
						e = Lnum[at-1]
						
						print('Atualizar registro ',at,':')
						print('-'*60)
						Lnome[at-1] = input('Novo nome: ')
						Lemail[at-1] = input('Novo email: ')
						Lsenha[at-1] = input('Nova senha: ')
						Lcpf[at-1] = int(input('Novo cpf: '))
						Lnum[at-1] = int(input('Novo N° de telefone: '))
				print('-'*60)
				atual = int(input('Atualizar dados? 1 - Sim  2 - Não '))
				if atual == 1:
					print('ATUALIZADO !')
				elif atual == 2 and at == 0:
					Lnome = Ln
					Lemail = Le
					Lsenha = Ls
					Lcpf = Lc
					Lnum = Lnu
					print('NÃO ATUALIZADO !')
				elif atual == 2 and at != 0:
					Lnome[at-1] = a
					Lemail[at-1] = b
					Lsenha[at-1] = c					
					Lcpf[at-1] = d
					Lnum[at-1] = e
					print('NÃO ATUALIZADO !')	
			v = 5
			z = ''
				