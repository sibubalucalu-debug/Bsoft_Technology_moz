from flask import Flask, render_template, url_for,request,jsonify

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import os


respostas = {
    "olá": "Olá! Como posso ajudar você?",
    
    "oy": "Oy! Como posso ajudar você?",
    
    
    "podes me ajudar":"Claro que sim! Como posso te ajudar?",
    "podes me ajudar?":"Claro que sim! Como posso te ajudar?",
    "pode me ajudar":"Claro que sim! Como posso te ajudar?",
    "pode me ajudar?":"Claro que sim! Como posso te ajudar?",
    
    
    "qual seu nome": "Eu sou o assistente da BSoft Tecnology.",
    "como se chama": "ChatBot da BSoft",
    "como se chama?": "ChatBot da BSoft.",
    
    
    "bs": "significa: Buch Software's ,Que é o nome da empresa.",
    
    "oque é bs": "significa: Buch Software's ,Que é o nome da empresa.",
    
    
    
    
    
    "tchao": "Até mais! Obrigado volte sempre",
    "adeus": "Até logo! Obrigado pela visita.",
    
    "obrigado": "De nada! Fico feliz em ajudar.",
    "obrigada": "De nada! Fico feliz em ajudar.",
    "muito obridado": "Optimo! Ficaste Satisfeito! Fico feliz em ajudar.",
    "muito obridada": "Optimo! Ficaste Satisfeito! Fico feliz em ajudar.",
    
    
    "este chat está disponivel 24h por dia?":"Sim, Estou Aqui 24h por dia para te ajudar no que eu poder.",
    
    
    
    "oque pode fazer por me":"Te dar Informacões sobre a BSoft.",
    
    
    
    "quero um site":"Optimo!, fale com Simao Lucas, O contato do whatsapp é +258 869319159.",
    
    
    "quero um blog": "Optimo! Vou te passar o numero do Whatsapp do responsavel: +258 879349159",
    
    
    "quem e dono da Bsoft":"É Simao Lucas Simao, Fundador CEO",
    "quem e dono da BSoft":"É Simao Lucas Simao, Fundador CEO",
    "quem e dono da Bsoft?":"É Simao Lucas Simao, Fundador CEO",
    "ola": "Oy como posso te ajudar?",
    
    
    
    "quem é voce":"Sou uma IA da BSoft, Estou aqui para te ajudar.",
    "quem é vôce?":"Sou uma IA da BSoft, Estou aqui para te ajudar.",
    
    
    
    "quem e voce":"Sou uma IA da BSoft, Estou aqui para te ajudar.",
    
    "quem e voce?":"Sou uma IA da BSoft, Estou aqui para te ajudar.",
    
    "quanto custa um blog": "Depende das paginas e suas funcionalidades, e muito mais, mais o preço pode comessar em torno de 9.000 MTS dependendo do blog.",
    
    "quanto custa um blog?": "Depende das paginas e suas funcionalidades, e muito mais, mais o preço pode comessar em torno de 9.000 MTS dependendo do blog.",
    
    
    "quanto custa um site": "Depende das paginas e suas funcionalidades, e muito mais, mais o preço pode comessar em torno de 14.000 MTS dependendo do site. Mais para um blog pode ser em torno de 9.000 MTS",
    
    
    "quanto custa um site?": "Depende das paginas e suas funcionalidades, e muito mais, mais o preço pode comessar em torno de 14.000 MTS dependendo do site. Mais para um blog pode ser em torno de 9.000 MTS",
    
    
    "quanto custa um app": "Um Aplicativo pode variar dependendo das suas funcionalidades mais comessa em torno de 15.000 MTS um aplicativo Android, se quiser Aplicativo IOS comessa em tormo dos 20.000 MTS",
    
    "quanto custa um app?": "Um Aplicativo pode variar dependendo das suas funcionalidades mais comessa em torno de 15.000 MTS um aplicativo Android, se quiser Aplicativo IOS comessa em tormo dos 20.000 MTS",
    
    "quanto custa um aplicativo": "Um Aplicativo pode variar dependendo das suas funcionalidades mais comessa em torno de 15.000 MTS um aplicativo Android, se quiser Aplicativo IOS comessa em tormo dos 20.000 MTS",
    
    
    "quanto custa um aplicativo?": "Um Aplicativo pode variar dependendo das suas funcionalidades mais comessa em torno de 15.000 MTS um aplicativo Android, se quiser Aplicativo IOS comessa em tormo dos 20.000 MTS",
    
    
    "oque é a bsoft": "BSoft Tecnology é uma empresa de desevolvimento de software, (sites, aplicativos, sistemas de gestao, sistema de instituicões de ensino.)",
    "oque é a bsoft?": "BSoft Tecnology é uma empresa de desevolvimento de software, (sites, aplicativos, sistemas de gestao, sistema de instituicões de ensino.)",
    "oque e a bsoft": "BSoft Tecnology é uma empresa de desevolvimento de software, (sites, aplicativos, sistemas de gestao, sistema de instituicões de ensino.)",
    "oque é bsoft": "BSoft Tecnology é uma empresa de desevolvimento de software, (sites, aplicativos, sistemas de gestao, sistema de instituicões de ensino.)",
    
    "oque é bsoft?": "BSoft Tecnology é uma empresa de desevolvimento de software, (sites, aplicativos, sistemas de gestao, sistema de instituicões de ensino.)",
    
    "oque e bsoft": "BSoft Tecnology é uma empresa de desevolvimento de software, (sites, aplicativos, sistemas de gestao, sistema de instituicões de ensino.)",
    
    
    
    "contato": "whatsapp e tell: +258 879349159",
    "vosso contato": "whatsapp e tell: +258 879349159",
    "contacto": "whatsapp e tell: +258 879349159",
    "vosso contacto": "whatsapp e tell: +258 879349159",
    "como contactar voces": "whatsapp e tell: +258 879349159",
    
    
    
    "oque é blog?": "Nao estou aqui para isso! Estou aqui para dar informacões sobre a BSoft.",
    
    "oque é blog": "Nao estou aqui para isso! Estou aqui para dar informacões sobre a BSoft.",
    
    "oque é site": "Nao estou aqui para isso! Estou aqui para dar informacões sobre a BSoft.",
    
    "oque é um blog": "Nao estou aqui para isso! Estou aqui para dar informacões sobre a BSoft.",
    
    "oque é um blog?": "Nao estou aqui para isso! Estou aqui para dar informacões sobre a BSoft.",
    
    "oque é um site?": "Nao estou aqui para isso! Estou aqui para dar informacões sobre a BSoft.",
    "oque é um site": "Nao estou aqui para isso! Estou aqui para dar informacões sobre a BSoft.",
    
    "va a pagina inicial": "Não consigo fazer isso!",
    "volte a pagina inicial": "Não consigo fazer isso!",
    
    "volte a página inicial": "Não consigo fazer isso!",
    
}


def enviarMSG(nome,numero,email,dsjo):
	
	allMSG = "Nome: "+ nome+"\n<br>Tell: "+ numero+"\n<br>Email: "+email+"\n<br>"+dsjo+"\n<br>Mensagem do site"
	
	msg = MIMEMultipart()
	
	
	msg["Subject"] = "Mensagem de: "+nome
	msg["From"] = "mozlimoz0rc@gmail.com"
	msg["To"] = "scaybuch@gmail.com"
	password = "vqcmikhtvwmvooab"
	
	#enviando a mensagem!
	msg.attach(MIMEText(allMSG,"html"))
	
	#credenciais
	
	s = smtplib.SMTP("smtp.gmail.com: 587")
	s.ehlo()
	s.starttls()
	s.login(msg["From"],password)
	s.sendmail(msg["From"],[msg["To"]],msg.as_string())
	s.quit()
	
	
	
	return nome




app = Flask(__name__)


@app.route("/")
def princi():
	return render_template("index.html")

@app.route("/contatos",methods=["GET","POST"])
def contato():
	
	nome = ""
	numero = ""
	email = ""
	dsjo = ""
	respo = None
	if request.method == "POST":
		nome = request.form["nome_"]
		numero = request.form["num_"]
		email = request.form["email_"]
		dsjo = request.form["dsejo_"]
	
	if nome != "":
		
		try:
			respo = enviarMSG(nome,numero,email,dsjo)
			
			return render_template("contato.html",alert = f"Mensagem de {respo} enviada com sucesso! ")
		except:
			return render_template("contato.html",alert = f"{nome} Mensagem nao enviada! ")
		
		
	else:
		return render_template("contato.html")
	
	
@app.route("/bschatbot",methods=["GET","POST"])
def chat():
	
	if request.content_type != "application/json":
		return render_template("chat.html")
		#return jsonify({"resposta": "Tipo de Conteudo Ivalido!"})
	msg = request.json.get('mensagem','').lower()
	resposta = respostas.get(msg,"Desculpe, não entendi, ainda estou em treinamento. whatsapp: +258 879349159 da Empresa")
	return jsonify({"resposta": resposta})
	
	
	#return render_template("chat.html")




@app.route("/projectos-bsoft")
def projetos():
	
	
	return render_template("vendas_bsoft_site.html")

@app.route("/free-apps")
def apps_free():
	
	
	return render_template("free_appsbs.html")
	
	


if __name__ == "__main__":
    app.run(debug="False")