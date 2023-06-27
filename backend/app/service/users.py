
from sqlalchemy.future import select
from app.model import User, Person
from app.config import db

class UserService:
    
    @staticmethod
    async def get_user_profile(username: str):
        query = select(User.username, 
                       User.email, 
                       Person.name, 
                       Person.birth,
                       Person.sex,
                       Person.phone_number).join_from(User, Person).where(User.username == username)
        return(await db.execute(query)).mappings().one()
    
    @staticmethod
    async def delete_all_users():
        await db.execute(User.__table__.delete())
        await db.execute(Person.__table__.delete())