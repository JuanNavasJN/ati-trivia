from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/login') 
def login():
    return render_template('login/login.html')

@app.route('/register') 
def register():
    return render_template('login/register.html')

@app.route('/forgot-password') 
def forgotPassword():
    return render_template('login/forgot-password.html')
    
@app.route('/admin')
def admin():
    return redirect('/admin/categorias', code=302)

@app.route('/admin/dash')
def dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/categorias') 
def categorias():
    return render_template('admin/categorias.html')

@app.route('/admin/trivias') 
def trivias():
    return render_template('admin/trivias.html')

@app.route('/admin/premios') 
def premios():
    return render_template('admin/premios.html')

@app.route('/admin/sorteos') 
def sorteos():
    return render_template('admin/sorteos.html')

@app.route('/admin/reglas') 
def reglas():
    return render_template('admin/reglas.html')

    

#Rutas para el Usuario home, login, registro, trivias, ranking, ayuda, cuenta

@app.route('/home') 
def reglas():
    return render_template('user/home.html')

@app.route('/trivia') 
def reglas():
    return render_template('user/trivia.html')

@app.route('/ranking') 
def reglas():
    return render_template('user/ranking.html')

@app.route('/ayuda') 
def reglas():
    return render_template('user/ayuda.html')

@app.route('/cuenta') 
def reglas():
    return render_template('user/cuenta.html')


if __name__ == '__main__':
    app.run(debug=True)