from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/vehiculo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import(
    Marca, 
    Tipo, 
    Vehiculo
    )

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/productos')
def mostrar_productos():
    return render_template('productos.html')

@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        # aca obtiene los datos ddel formulario
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = float(request.form['precio'])
        # creo el nuevo producto
        nuevo_producto = {"nombre": nombre, "categoria": categoria, "precio": precio}
        # y aca lo agrego


        return redirect(url_for('mostrar_productos'))   
    
    return render_template('agregar_producto.html') 

if __name__ == '__main__':
    app.run(debug=True)
