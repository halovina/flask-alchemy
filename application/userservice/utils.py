from ..models import User
from .. import db
from passlib.hash import sha256_crypt

async def example_async_without_await():
    password = sha256_crypt.hash('1234567')

    user = User()
    user.email = "ratna@example.com"
    user.first_name = "ratna"
    user.last_name = "xyz"
    user.password = password
    user.username = "ratna@example.com"
    user.authenticated = True

    db.session.add(user)
    db.session.commit()