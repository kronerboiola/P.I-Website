from flask import *
from flask_mail import Mail, Message
from forms import *
from random import choice
from models import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'guess-it'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = '101airbornekiller@gmail.com'
app.config['MAIL_PASSWORD'] = 'polka0789'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
mail = Mail(app)
error_messages = ['Prepare for unforeseen consequences', 'And another page bites the dust...',
 'Away with you, vile error!', 'Mayday, Mayday!!!',
  'O problema é na mangueira!', 'Houston, nós temos um problema']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', title='Home')#, 404

@app.route('/about')
def about():
	return render_template('about.html', title='About Us')

@app.route('/subscription', methods=['GET', 'POST'])
def sign():
	form = CustomForm('Quero a newsletter!')
	if form.validate_on_submit():
		session['username'] = form.user.data
		session['email'] = form.email.data
		session['password'] = form.password.data
		msg = Message(f'{session["username"]}, obrigado por inscrever-se na newsletter!',
		 sender='101airbornekiller@gmail.com', recipients=[session['email']])
		msg.html = render_template('email-body.html')
		try:
			mail.send(msg)
		except: # smtplib.SMTPRecipientsRefused:
			flash("There's an error with the typed e-mail!", 'error')
			return redirect('/subscription')

		user = User(username=session['username'],
		 psw_hash=bcrypt.hashpw(session['password'].encode('utf8'),
		  bcrypt.gensalt()))
		try:
			db.session.add(user)
			db.session.commit()
			flash('User %s registered!' % session['username'], 'info')
		except:
			flash('An error happened while trying to signup.')
			return redirect('/subscription')
			#return flash('An error happened while trying to signup.') #needs to be valid HTTP response!!!
		session['logged'] = True
		return redirect('/home')
	return render_template('signup.html', title='Sign Up',
	 form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = CustomForm('Login')
	if form.validate_on_submit():
		session['username'] = form.user.data
		session['password'] = form.password.data
		user = User.query.filter_by(username=session['username']).first()
		if user is None or not user.check_psw(session['password']):
			flash('Wrong username or password!')
			session['logged'] = False
			return redirect('/login')
		session['logged'] = True
		flash('Successfull login!')
		return redirect('/home')
	return render_template('login.html', title='Login', form=form)

'''@app.route('/login', methods=['GET', 'POST'])
def login():
	form = CustomForm('Login')
	if form.validate_on_submit():
		session['username'] = form.user.data
		session['password'] = form.passw.data
		user = User.query.filter_by(username=session['username']).first()
		if user is None:
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	return render_template('contact.html', title='Contato',
	 msg_types=['Reclamação', 'Dúvida', 'Sugestão'])

@app.route('/turma')
def turma():
	return render_template('turminha.html', title='Nossa Turma')

@app.route('/logout')
def logout():
	try:
		session.pop('username')
	except KeyError:
		return redirect('/home')
	session['logged'] = False
	return render_template('logout.html')

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html', msg=choice(error_messages)), 404

if __name__ == '__main__':
	#db.create_all()
	app.run(debug=True, host='0.0.0.0')