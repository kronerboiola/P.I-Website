from routes import db
import bcrypt

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True) #id is a built-in!!!
	username = db.Column(db.String(32), index=True, unique=True)
	#email = db.Column(db.String(64), index=True, unique=True) #really needed?
	psw_hash = db.Column(db.String(128))

	def __repr__(self):
		return f'User {self.username}'