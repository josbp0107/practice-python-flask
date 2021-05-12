# Importamos para realizar testing con flask
from flask_testing import TestCase
from flask import current_app, url_for
# Import del archivo main, que en este caso es app.py
from app import app

class MainTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True # Flask va a saber que esta en el ambiente de testing
        app.config['WTF_CSRF_ENABLED'] = False # Desactivar CSRF
        
        return app
    
    # Prueba si nuestra app de flask existe
    def test_app_exist(self):
        self.assertIsNotNone(current_app) # importa la current app del momento

    # Prueba si la app esta en modo testing
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING']) # Verifica si la configuracion es True
    
    # Prueba si la app redirige a hello
    def test_index_redirect(self):
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
    
    # Prueba si que hello nos regresa un status code 200 cuando se realiza un GET
    def test_hello_get(self):
        response  = self.client.get(url_for('hello'))
        self.assert200(response)
    
    # Prueba si el envio del form o POST fue existosamente y se hizo un redirect a index
    def test_hello_post(self):
        fake_form = {
            'username':'fake',
            'password':'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form )
        self.assertRedirects(response, url_for('index'))