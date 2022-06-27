from dominio import Usuario, Lance, Leilao

yuri = Usuario('Yuri')
gui = Usuario('Gui')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular')

leilao.propoe(lance_do_yuri)
leilao.propoe(lance_do_gui)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')
print(f"O menor lance foi de {leilao.menor_lance} e o maior lance foi de {leilao.maior_lance}")
