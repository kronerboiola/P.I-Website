from routes import db
import bcrypt

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), index=True, unique=True)
	#email = db.Column(db.String(64), index=True, unique=True) #really needed?
	psw_hash = db.Column(db.String(128))

	def check_psw(self, psw):
		return bcrypt.checkpw(self.psw_hash.encode('utf8'), psw)

	def __repr__(self):
		return f'User {self.username}'