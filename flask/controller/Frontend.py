from flask import render_template
from config.constants import *
from controller.Guest import Guest

class Frontend(Guest):
    def __init__(self):
        super().__init__();
    
    def home(self):
        data = {}
        data['pageTitle'] = "Home"
        return render_template("home.html", **data)