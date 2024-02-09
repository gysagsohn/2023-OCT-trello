from init import db, ma 

class User(db.Model):
    __tablename__="users"

    id = db.Colum(db.Integer, primary_key=True)
    name = db.Colum(db.String)
    email = db.Colum(db.String, nullable=False, unique=True)
    password = db.Colum(db.String, nullable=False)
    is_admin = db.Colum(db.Boolean, default=False)

class UserSchema(ma.Schema):
        class Meta:
              fields = ('id', 'name', 'email', 'password', 'is_admin')

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])
