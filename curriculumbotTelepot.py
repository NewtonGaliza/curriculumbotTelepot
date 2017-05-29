#-*-coding:latin1-*- 

import time
import telepot

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']	
	
	if command == '/contato':
		bot.sendMessage(chat_id, 'Telefone: 83 - 991470725\nE-mail: newtonjgaliza@gmail.com\nTelegram: @NewtonGaliza')
	elif command == '/formacao':
		bot.sendMessage(chat_id, '*Ensino Médio Completo - Colégio e Curso Visão e Marista Pio X\n*Ensino Superior Estácio IDEZ - Análise e Desenvolvimento de Sistemas\n*Brasil Mais TI - Sistemas Operacionais\n*Diálogo TI Intel - Big Data')
	elif command == '/experiencia':
		bot.sendMessage(chat_id, '*Prestador de Serviço - PMJP - Secitec\nCargo: Instrutor de Estação Diigital\nPeríodo: 1(hum) ano e meio\n*Prestador de Serviço - PMJP - Sedes\nCargo: Entrevistador Bolsa Família - Operador do Cadastro Único e SIBEC\nPeríodo: 2(dois) anos e um mês\n*HostDime\nCargo: Atendimento Nível 1\nPeríodo: 1(hum) mês de estágio')

bot = telepot.Bot('Token Here')
bot.message_loop(handle)
print 'listening...'

while 1:
	time.sleep(5)
