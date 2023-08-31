# declaro que uso Framework Flask
# render_template para "llamar" html

from flask import Flask, render_template

# se crea objeto Flask pasando como parametro una variable python que dice que index.py es es modulo principal
app = Flask( __name__ ) 

#define ruta de home
@app.route('/')

# Función           
def home():
    #return "Home Page"
    return render_template("home.html")

#define ruta de una pagina about
@app.route('/about')

def about():
    return render_template("about.html")

if __name__ == '__main__':
    # modo prueba para no tener que reiniciar a cada modificacion de codigo
    app.run(debug=True)