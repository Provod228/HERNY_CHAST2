from editing import UserEntity, SubjectEntity, EducationalMaterialEntity, RoleEntity
from abc import ABCMeta, abstractmethod
import sqlite3


class AbstractManipulation(metaclass=ABCMeta):
    @abstractmethod
    def add(self, cursor_db):
        pass

    @abstractmethod
    def delete(self, cursor_db):
        pass

    @abstractmethod
    def change(self, cursor_db):
        pass

    @abstractmethod
    def delete_all(self, cursor_db):
        pass


class User(AbstractManipulation):
    @staticmethod
    def add(cursor_db, username=None, login=None, email=None, password=None, role_id=1, *args, **kwargs) -> None:
        if None not in (username, login, email, password):
            UserEntity(username=username, login=login, email=email, password=password, role_id=role_id).add(cursor_db)
        else:
            print("Ошибка ввода")

    @staticmethod
    def delete(cursor_db, is_login=None, is_email=None, *args, **kwargs) -> None:
        del_dict = {
            'login': is_login,
            'email': is_email,
        }
        del_list = []
        for k, v in del_dict.items():
            if v is not None:
                del_list.append(f'{k}="{v}"')
        print(del_list)


    @staticmethod
    def change(cursor_db, *args, **kwargs):
        pass

    @staticmethod
    def delete_all(cursor_db, *args, **kwargs):
        pass


connection = sqlite3.connect('school.db')
cursor = connection.cursor()

User.delete(cursor_db=None, is_login='aba', is_email='lol@bk.ru')

connection.commit()

connection.close()
