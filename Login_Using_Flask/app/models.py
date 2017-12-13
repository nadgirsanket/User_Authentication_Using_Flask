from Login import db, bcrypt

#create class
class User(db.Model):

	__tablename__ = "users" #table name

	id=db.Column(db.Integer, primary_key=True) # columns of the table
	name=db.Column(db.String, nullable=False)
	email=db.Column(db.String, nullable=False)
	password=db.Column(db.String, nullable=False)

	def __init__(self,name,email,password):
		self.name = name
		self.email = email
		self.password = bcrypt.generate_password_hash(password)

	def __repr__(self):
		return '<name {}'.format(self.name)


