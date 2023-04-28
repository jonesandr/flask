
from flask import Flask, request

app = Flask(__name__)
palabras = {}

@app.route('/')
def home():
    return 'bienvenido(a)!'

@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        palabra = request.form['palabra']
        significado = request.form['significado']
        palabras[palabra] = significado
        return 'palabra ingresada: {} - {}'.format(palabra, significado)
    else:
        return '''
            <form method="post">
                <label>palabra:</label>
                <input type="text" name="palabra"><br>
                <label>significado:</label>
                <input type="text" name="significado"><br>
                <input type="submit" value="ingresar">
            </form>
        '''

@app.route('/buscar')
def buscar():
    palabra = request.args.get('palabra')
    if palabra in palabras:
        return 'significado: {}'.format(palabras[palabra])
    else:
        return 'no encontrada '

@app.route('/eliminar')
def eliminar():
    palabra = request.args.get('palabra')
    if palabra in palabras:
        del palabra[palabra]
        return 'palabra eliminada'
    else:
        return 'no encontrada'

@app.route('/editar', methods=['GET', 'POST'])
def editar():
    if request.method == 'POST':
        palabra = request.form['palabra']
        significado = request.form['significado']
        if palabra in palabras:
            palabras[palabra] = significado
            return 'listo'
        else:
            return 'no existe '
    else:
        return '''
            <form method="post">
                <label>palabra:</label>
                <input type="text" name="palabra"><br>
                <label>nuevo significado:</label>
                <input type="text" name="significado"><br>
                <input type="submit" value="actualizar">
            </form>
        '''

@app.route('/salir')
def salir():
    return 'Goodbye!'

if __name__ == '__main__':
    app.run()