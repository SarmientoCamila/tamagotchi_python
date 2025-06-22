from flask import Flask, render_template, request, session
from flask_session import Session
from tamagotchi import Tamagotchi

app = Flask(__name__)

# Configuración de la sesión
app.config['SECRET_KEY'] = 'clave-secreta-segura'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Función para obtener el Tamagotchi desde sesión
def get_tamagotchi(name):
    if 'tamagotchis' not in session:
        session['tamagotchis'] = {}

    tamas = session['tamagotchis']

    if name not in tamas:
        tamas[name] = Tamagotchi(name).__dict__

    session['tamagotchis'] = tamas
    return Tamagotchi(**tamas[name])

# Guardar cambios del Tamagotchi en sesión
def save_tamagotchi(tamagotchi):
    session['tamagotchis'][tamagotchi.name] = tamagotchi.__dict__

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tamagotchi', methods=['POST'])
def create_tamagotchi():
    name = request.form.get('name')
    if not name:
        return render_template('index.html', error="Por favor, ingresa un nombre para tu Tamagotchi.")          

    tamagotchi = get_tamagotchi(name)
    save_tamagotchi(tamagotchi)
    return render_template('tamagotchi.html', tamagotchi=tamagotchi.serialize())

@app.route('/tamagotchi/<name>', methods=['POST'])
def tamagotchi_post(name):
    tamagotchi = get_tamagotchi(name)
    action = request.form.get('action')

    if action == 'feed':
        tamagotchi.hunger += 10
    elif action == 'play':
        tamagotchi.happiness += 10
    elif action == 'sleep':
        tamagotchi.energy += 10
    elif action == 'age':
        tamagotchi.age += 1
    elif action == 'status':
        pass
    else:
        return render_template('tamagotchi.html', error="Acción no válida.", tamagotchi=tamagotchi.serialize())

    save_tamagotchi(tamagotchi)
    return render_template('tamagotchi.html', tamagotchi=tamagotchi.serialize())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
