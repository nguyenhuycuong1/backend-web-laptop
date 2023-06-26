import base64
from datetime import datetime
from uuid import uuid4
from fastapi import HTTPException

from passlib.context import CryptContext
from app.schema.schema import RegisterSchema
from app.model import Person, User, UsersRole, Role, Cart
from app.repository.role import RoleRepository
from app.repository.users import UsersRepository
from app.repository.person import PersonRepository
from app.repository.user_role import UsersRoleRepository
from app.repository.cart import CartRepository
from app.schema.schema import LoginSchema, ForgotPasswordSchema
from app.repository.auth_repo import JWTRepo


# Encrypt password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    async def register_service(register: RegisterSchema):
        # Create uuid
        _person_id = str(uuid4())
        _users_id = str(uuid4())
        _cart_id = str(_users_id)

        # mapping request data to class entity table
        _person = Person(
            id=_person_id,
            name=register.name,
            birth=register.birth,
            sex=register.sex,
            phone_number=register.phone_number,
        )

        _users = User(
            id=_users_id,
            username=register.username,
            email=register.email,
            password=pwd_context.hash(register.password),
            person_id=_person_id,
        )

        _cart = Cart(cart_id=_cart_id, user_id=_users_id)

        # Everyone who registers through our registration page makes the default as a user
        _role = await RoleRepository.find_by_role_name("user")
        _users_role = UsersRole(users_id=_users_id, role_id=_role.id)

        # Cheking the same username
        _username = await UsersRepository.find_by_username(register.username)
        if _username:
            raise HTTPException(status_code=400, detail="Username already exists!")

        # Cheking the same email
        _email = await UsersRepository.find_by_email(register.email)
        if _email:
            raise HTTPException(status_code=400, detail="Email already exists!")

        else:
            #  insert to tables
            await PersonRepository.create(**_person.dict())
            await UsersRepository.create(**_users.dict())
            await UsersRoleRepository.create(**_users_role.dict())
            await CartRepository.create(**_cart.dict())

    @staticmethod
    async def logins_service(login: LoginSchema):
        _username = await UsersRepository.find_by_username(login.username)

        if _username is not None:
            if not pwd_context.verify(login.password, _username.password):
                raise HTTPException(status_code=400, detail="Invalid Password !")
            return JWTRepo(data={"username": _username.username}).generate_token()
        raise HTTPException(status_code=404, detail="Username not found !")

    @staticmethod
    async def forgot_password_service(forgot_password: ForgotPasswordSchema):
        _email = await UsersRepository.find_by_email(forgot_password.email)
        if _email is None:
            raise HTTPException(status_code=404, detail="Email not found !")
        await UsersRepository.update_password(
            forgot_password.email, pwd_context.hash(forgot_password.new_password)
        )

    @staticmethod
    async def get_user_by_credentials(username: str, password: str) -> User:
        user = await UsersRepository.find_by_username(username)
        if user is not None:
            if pwd_context.verify(password, user.password):
                return user
        raise HTTPException(status_code=401, detail="Invalid credentials")


# Generate roles manually
async def generate_role():
    _role = await RoleRepository.find_by_list_role_name(["admin", "user"])
    if not _role:
        await RoleRepository.create_list(
            [
                Role(id=str(uuid4()), role_name="admin"),
                Role(id=str(uuid4()), role_name="user"),
            ]
        )
