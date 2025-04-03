from pydantic import BaseModel

class UserBase(BaseModel):
    '''Базовая схема для создания и обновления пользователя.'''
    name: str
    nickname: str
    email: str


class User(UserBase):
    # '''Полная схема пользователя включая идентификатор.'''
    # id: int

    class Config:
        '''Конфигурация для автоматического преобразования ORM-объектов'''
        orm_mode=True