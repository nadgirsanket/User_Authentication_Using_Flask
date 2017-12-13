from Login import db
from models import User

#Create the database
db.create_all()

#Insert user records
db.session.add(User("admin", "admin@xyz.com", "admin1234"))
db.session.add(User("Alice", "alice@xyz.com", "alicepasswd"))
db.session.add(User("Bob", "bob@xyz.com", "bobpasswd"))


#Commit the changes
db.session.commit()