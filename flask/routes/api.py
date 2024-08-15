from index import app

@app.route('/index')
def apiRoutes():
    return 'api routes'

@app.route('/api')
def ppa():
    return "api "