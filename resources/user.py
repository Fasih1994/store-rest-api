from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash

from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help='Username field can not be blanked.')
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help='password field can not be blanked.')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": f"User with {data['username']} already exist."}, 400

        try:
            user = UserModel(data['username'], generate_password_hash(data['password']))
            user.save_to_db()
        except:
            return {"message": "an error occurred while creating the user."}, 500

        return {'message': "User Created Successfully!"}, 201
