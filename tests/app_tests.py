from nose.tools import *
from bin.app import app
from tests.tools import assert_response


def test_index():
    # chequea que se obtiene 404 en la URL /
    resp = app.request("/")
    assert_response(resp, status="404")

    # testea nuestra primera peticion GET a /hello
    resp = app.request("/hello")
    assert_response(resp)

    # asegurarse de que los valores por defecto funcionan para el formulario
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nadie")

    # testear que obtenemos los valores esperados
    data = {'name': 'Jose', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Jose")
