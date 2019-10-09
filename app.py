from flask import Flask, render_template, redirect, request, jsonify,request, session, abort , flash , redirect, url_for
from controllers.main import *
import pymongo
import os
import json
from bson import BSON
from bson import json_util

# DB -----------------------------------

URI = "mongodb://admin:DY4B2kiERHj9Vl4I@cluster0-shard-00-00-55sxd.mongodb.net:27017,cluster0-shard-00-01-55sxd.mongodb.net:27017,cluster0-shard-00-02-55sxd.mongodb.net:27017/admin?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"

# URI = "mongodb://localhost:27017"

client = pymongo.MongoClient(URI)

db = client['atrivia'] # Se selecciona la base de datos

#-----------------------------------

app = Flask(__name__)

@app.route('/') 
def index():
    categories = list(db.category.find({}))
    return render_template('user/home.html', categories=categories)

@app.route('/login') 
def login():
    if session.get('logged_in'):
        return redirect(url_for('home'))
    return render_template('login/login.html')

@app.route('/loginAuth' , methods=['GET', 'POST'])
def loginAuth():
    user = db.user.find_one({"email": request.form.get('inputEmail','')})

    if user == None:
        flash("Correo o contraseña invalido")
        return redirect(url_for('login'))
    else:
        user = json.dumps(user, sort_keys=True, indent=4, default=json_util.default)
        user = json.loads(user)
        if not user['password'] == request.form.get('inputPassword',''):
            return redirect(url_for('login'))
        else:
            session['logged_in'] = True
            if user['admin'] == True:
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/register') 
def register():
    return render_template('login/register.html')

@app.route('/registerAuth' , methods=['GET', 'POST'])
def registerAuth():
    user = db.user.find_one({"email": request.form.get('inputEmail', '')})
    if user == None:
      dic = {
          "email": request.form.get('inputEmail', ''),
          "password": request.form.get('inputPassword', ''),
          "admin": False,
          "nombre": request.form.get('inputFirstName', ''),
          "apellido": request.form.get('inputLastName', ''),
          "ranking": 0,
          "scoare": 0,
          "imagen": ""
      }
      db.user.insert_one(dic)
      return redirect(url_for('login'))
    else:
        return render_template('login/register.html')

@app.route('/forgot-password') 
def forgotPassword():
    return render_template('login/forgot-password.html')
    
@app.route('/admin')
def admin():
    return redirect('/admin/categorias', code=302)

@app.route('/admin/dash')
def admindashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/categorias') 
def admincategorias():
    categories = list(db.category.find({}))
    return render_template('admin/categorias.html', categories=categories)

@app.route('/admin/trivias') 
def admintrivias():
    categories = list(db.category.find({}))
    trivias = list(db.trivias.find({}))
    return render_template('admin/trivias.html', categories=categories, trivias=trivias)

@app.route('/admin/premios') 
def adminpremios():
    premios = list(db.premios.find({}))
    return render_template('admin/premios.html', premios=premios)

@app.route('/admin/sorteos') 
def adminsorteos():
    sorteos = list(db.sorteos.find({}))
    premios = list(db.premios.find({}))
    trivias = list(db.trivias.find({}))
    return render_template('admin/sorteos.html', sorteos=sorteos, premios=premios, trivias=trivias)

@app.route('/admin/reglas') 
def adminReglas():
    return render_template('admin/reglas.html')
   
#Rutas para el Usuario 

@app.route('/home') 
def home():
    categories = list(db.category.find({}))
    return render_template('user/home.html', categories=categories)

@app.route('/trivia') 
def trivia():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('user/trivia.html')

@app.route('/ranking') 
def ranking():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('user/ranking.html')

@app.route('/help') 
def ayuda():
    return render_template('user/ayuda.html')

@app.route('/cuenta') 
def cuenta():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('user/cuenta.html')




# ----------------------------- API ------------------------------

# Categories
@app.route('/api/categories', methods = ['GET']) 
def api_categories():
    return getAllCategories()

@app.route('/api/category/<id>', methods = ['GET']) 
def api_category(id):
    return getOneCategory(id)

@app.route('/api/category', methods = ['POST']) 
def api_new_category():
    return createCategory(request.get_json(force=True))

@app.route('/api/category/<id>', methods = ['DELETE']) 
def api_delete_category(id):
    return deleteCategory(id)

# Trivias
@app.route('/api/trivias', methods = ['GET']) 
def api_trivias():
    return getAllTrivias()

@app.route('/api/trivia/<id>', methods = ['GET']) 
def api_trivia(id):
    return getOneTrivia(id)

@app.route('/api/trivia', methods = ['POST']) 
def api_new_trivia():
    return createTrivia(request.get_json(force=True))

@app.route('/api/trivia/<id>', methods = ['DELETE']) 
def api_delete_trivia(id):
    return deleteTrivia(id)

# Premios
@app.route('/api/premios', methods = ['GET'])
def api_premios():
    return getAllPremios()

@app.route('/api/premios/nuevo', methods = ['POST'])
def api_new_premio():
    return createPremio(request.get_json(force=True))

@app.route('/api/premios/borrar', methods = ['POST'])
def api_delete_premio():
    return deletePremio(request.get_json(force=True))

@app.route('/api/premios/editar', methods = ['POST'])
def api_edit_premio():
    return editPremio(request.get_json(force=True))


# Sorteos
@app.route('/api/sorteos', methods = ['GET'])
def api_sorteos():
    return getAllSorteos()

@app.route('/api/sorteos/nuevo', methods = ['POST'])
def api_new_sorteo():
    return createSorteo(request.get_json(force=True))

@app.route('/api/sorteos/borrar', methods = ['POST'])
def api_delete_sorteo():
    return deleteSorteo(request.get_json(force=True))

@app.route('/api/sorteos/editar', methods = ['POST'])
def api_edit_sorteo():
    return editSorteo(request.get_json(force=True))

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0')