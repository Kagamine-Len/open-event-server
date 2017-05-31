from flask.ext.scrypt import check_password_hash
from app.models.user import User


def jwt_authenticate(email, password):
    """
    helper function to authenticate user if credentials are correct
    :param email:
    :param password:
    :return:
    """
    user = User.query.filter_by(email=email).first()
    if user is None:
        return None
    auth_ok = check_password_hash(
        password.encode('utf-8'),
        user.password.encode('utf-8'),
        user.salt
    )
    if auth_ok:
        return user
    else:
        return None


def jwt_identity(payload):
    """
    Jwt helper function
    :param payload:
    :return:
    """
    return User.query.get(payload['identity'])


