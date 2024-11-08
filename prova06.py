UsuarioCerto = 'admin'
SenhaCerta = "senha"
MaxTentativa = 3


for tentativa in range(1, MaxTentativa +1):
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    if usuario == UsuarioCerto and senha == SenhaCerta:
        print('Login bem-sucedido!')
        break
    else:
        tentativarestante = MaxTentativa - tentativa
        if tentativarestante > 0:
            print(f'usuario ou senha incorretos, você tem {tentativarestante} tentativa(s) restante(s).')
        else:
            print('Usuario ou senha incorretos, você não tem mais tentativas.')

if usuario != UsuarioCerto or senha != SenhaCerta:
    for i in range(1, 4):
     print('acesso bloqueado')