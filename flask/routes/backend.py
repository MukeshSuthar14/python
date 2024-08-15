from index import app
from controller.Login import Login
from controller.Frontend import Frontend
from middleware.CheckLogin import checkLogin

# @app.before_request
def check():
    return checkLogin()

@app.get('/')
def homeRoute():
    return Frontend().home()

@app.get('/login')
def loginIndexRoute():
    return Login().index()

@app.post('/login/check-login')
def checkLoginRoute():
    return Login().checkLogin()

@app.get('/login/verifyData/<jsonData>')
def verifyDataRoute(jsonData):
    return Login().verifyData(jsonData)