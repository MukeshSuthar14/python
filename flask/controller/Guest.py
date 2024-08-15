from flask import render_template

class Guest:
    def __init__(self):
        pass

    def loadLoginView(self, pageName, pageData):
        return render_template(pageName, **pageData)