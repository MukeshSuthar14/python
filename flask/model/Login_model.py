from index import db

class Login_model(db.Model):
    
    __table__ = "login_master"
    i_id = db.Column(db.Integer, primary_key = True)
    v_name = db.Column(db.String)
    v_email = db.Column(db.String)
    v_password = db.Column(db.String)
    v_mobile = db.Column(db.String)
    v_role = db.Column(db.String)
    t_is_active = db.Column(db.Integer, default = 1)
    t_is_deleted = db.Column(db.Integer, default = 0)
    i_created_id = db.Column(db.Integer)
    dt_created_at = db.Column(db.DateTime)
    i_updated_id = db.Column(db.Integer, nullable=True)
    dt_updated_at = db.Column(db.DateTime, nullable=True)
    i_deleted_id = db.Column(db.Integer, nullable=True)
    dt_deleted_at = db.Column(db.DateTime, nullable=True)
    v_ip = db.Column(db.String)

    def __init__(self):
        pass
    
    def getRecordDetails(self):
        pass