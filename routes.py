from flask import *
from flask_mail import Mail, Message
from forms import *
'''from models import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate'''

app = Flask(__name__)
app.secret_key = 'guess-it'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '101airbornekiller@gmail.com'
app.config['MAIL_PASSWORD'] = open(r"C:\Users\RAFAEL\Videos\Site_PI\app\highway.txt", 'r').read()
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
'''app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate=Migrate(app, db)'''

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', title='Home')#, 404

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/subscription', methods=['GET', 'POST'])
def sign():
	form = CustomForm()
	if form.validate_on_submit():
		flash('User %s registered!' % form.user.data, 'info')
		session['username'] = form.user.data
		session['email'] = form.email.data
		#session['password'] = form.passw.data
		session['logged'] = True
		msg = Message(f'<h1>{session["username"]}, obrigado por increver-se na newsletter!</h1>', sender='101airbornekiller@gmail.com',
		 recipients=[session['email']])#, body=''.join(open(r'C:\Users\RAFAEL\Videos\Site_PI\app\email-body.html', 'r').readlines()))
		msg.html = render_template('email-body.html')
		mail.send(msg)
		'''
		user = User(username=session['username'], psw_hash=bcrypt.hashpw(session['password'].encode('utf8'), bcrypt.gensalt()))
		db.session.add(user)
		db.session.commit()'''
		return redirect('/home')
	return render_template('signup.html', title='Sign Up', form=form)

'''def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d'''

'''@app.route('/login', methods=['GET', 'POST'])
def login():
	import sqlite3
	con = sqlite3.connect('users.sqlite3')
	con.row_factory = dict_factory
	cursor = con.cursor()#dictionary=True, buffered=True)
	form = CustomForm('Login')
	if form.validate_on_submit():
		session['username'] = form.user.data
		session['password'] = form.passw.data
		cursor.execute(f"SELECT * FROM user WHERE username = {session['username']}")
		if cursor is not None:
			data = cursor.fetchone()
			try:
				password = data['psw_hash']
			except:
				return 
			if bcrypt.checkpw(session['password'].encode('utf8'), password):
				session['logged'] = True
				flash('Successfull login!')
				cursor.close()
				return
			return render_template('login.html')
		return
	return render_template('login.html', title='Login', form=form)'''

@app.route('/contact')
def contact():
	return render_template('contact.html', title='Contact')

@app.route('/turma')
def turma():
	return render_template('turminha.html', title='Turma')

@app.route('/logout')
def logout():
	try:
		session.pop('username')
	except KeyError:
		return redirect('/home')
	session['logged'] = False
	#logged = False
	return render_template('logout.html')

if __name__ == '__main__':
	#db.create_all()
	app.run(debug=True)