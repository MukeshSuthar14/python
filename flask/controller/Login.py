from flask import render_template, request, redirect
from config.constants import *
from controller.Guest import Guest
from helper.helper import *
# from model.Login_model import Login_model

class Login(Guest):
    def __init__(self):
        super().__init__();
        self.folderName = ADMIN_VIEW_FOLDER + 'login/'

    def index(self):
        data = {}
        data['pageTitle'] = "Login"
        return self.loadLoginView(self.folderName + "login.html", data)

    def checkLogin(self):
        if request.form:

            return "success"
        return redirect(request.referrer)
        

    def verifyData(self, jsonData):
        return jsonData