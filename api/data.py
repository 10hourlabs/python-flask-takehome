
from app import db, Company, User

db.create_all()

user1 = User(name='John Doe', email_address="john.doe@companyxyz.com",
             availability_status='available', company=Company(name='Company XYZ'))
user2 = User(name='Cindy Smith', email_address="cindy.smith@companyabc.com",
             availability_status='available', company=Company(name='Company ABC'))
user3 = User(name='Harry Potter', email_address="harry.potter@companyxyz.com",
             availability_status='available', company=Company(name='Company AMZ'))


db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

db.session.commit()
