from flask import Flask, request, make_response, redirect, render_template # Importamos desde flask, la clase Flask para realizar nuevas instancias

app = Flask(__name__) # Nueva instancia de Flask, donde le tenemos que pasar el nombre de nuestra aplicación, que en este caso seria main.py
app.config['DEBUG'] = True


todos = ['Estudiar','Estudiar estructuras de datos','Desarrollar tesis']


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip',user_ip)

    return response

@app.route('/hello') # route recive como parametro la ruta donde queramos que se corra esta función
def hello_world():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos,
    }

    return render_template('hello.html', **context)


if __name__ == '__main__':
    app.run(debug=True) # Activar debug 