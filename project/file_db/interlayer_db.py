from .editing_db import UserEntity, EducationalMaterialEntity, SubjectEntity, RoleEntity
from abc import ABCMeta, abstractmethod
import sqlite3


class AbstractManipulation(metaclass=ABCMeta):
    @abstractmethod
    def get(self, cursor_db):
        pass

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
    def get(
            cursor_db, id=None, username=None, login=None, email=None, password=None, role_id=1, *args, **kwargs
    ) -> list:
        role_data = []
        search_list = []
        search_dict = {
            'id': id,
            'username': username,
            'login': login,
            'email': email,
            'password': password,
            'role_id': role_id,
        }
        if any([id, username, login, email, password, role_id]):
            for k, v in search_dict.items():
                if v is not None:
                    search_list.append(f'{k} = "{v}"')
            index = 0
            for item in UserEntity.get(cursor_db, search_list):
                role_data.append({
                    'id': item[0],
                    'username': item[1],
                    'login': item[2],
                    'email': item[3],
                    'password': item[4],
                    'role_id': item[5],
                })
                index += 1
            return role_data
        else:
            index = 0
            for item in UserEntity.get(cursor_db):
                role_data.append({
                    'id': item[0],
                    'username': item[1],
                    'login': item[2],
                    'email': item[3],
                    'password': item[4],
                    'role_id': item[5],
                })
                index += 1
            return role_data

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
                del_list.append(f'{k} = "{v}"')
        UserEntity.delete(cursor_db=cursor_db, condition_list=del_list)

    @staticmethod
    def change(
            cursor_db, is_login=None, is_email=None, username=None,
            login=None, email=None, password=None, role_id=None, *args, **kwargs
    ):
        old_data_dict = {
            'login': is_login,
            'email': is_email,
        }
        new_data_dict = {
            'login': login,
            'email': email,
            'password': password,
            'role_id': role_id,
        }
        old_data_list = []
        new_data_list = []
        for k, v in old_data_dict.items():
            if v is not None:
                old_data_list.append(f'{k} = "{v}"')
        for k, v in new_data_dict.items():
            if v is not None:
                new_data_list.append(f'{k} = "{v}"')
        UserEntity.change(cursor_db, old_data_list, new_data_list)

    @staticmethod
    def delete_all(cursor_db, *args, **kwargs):
        UserEntity.delete_all(cursor_db)


class Role(AbstractManipulation):
    @staticmethod
    def get(cursor_db, id=None, title=None, *args, **kwargs) -> list:
        role_data = []
        search_list = []
        search_dict = {
            'id': id,
            'title': title,
        }
        if any([id, title]):
            for k, v in search_dict.items():
                if v is not None:
                    search_list.append(f'{k} = "{v}"')
            index = 0
            for item in RoleEntity.get(cursor_db, search_list):
                role_data.append({'id': item[0], 'title': item[1]})
                index += 1
            return role_data
        else:
            index = 0
            for item in RoleEntity.get(cursor_db):
                role_data.append({'id': item[0], 'title': item[1]})
                index += 1
            return role_data

    @staticmethod
    def add(cursor_db, title=None, *args, **kwargs) -> None:
        if None not in (title, ):
            RoleEntity(title=title).add(cursor_db)
        else:
            print("Ошибка ввода")

    @staticmethod
    def delete(cursor_db, is_title=None, *args, **kwargs) -> None:
        del_dict = {
            'title': is_title,
        }
        del_list = []
        for k, v in del_dict.items():
            if v is not None:
                del_list.append(f'{k} = "{v}"')
        RoleEntity.delete(cursor_db=cursor_db, condition_list=del_list)

    @staticmethod
    def change(
            cursor_db, is_title=None, title=None, *args, **kwargs
    ):
        old_data_dict = {
            'title': is_title,
        }
        new_data_dict = {
            'title': title,
        }
        old_data_list = []
        new_data_list = []
        for k, v in old_data_dict.items():
            if v is not None:
                old_data_list.append(f'{k} = "{v}"')
        for k, v in new_data_dict.items():
            if v is not None:
                new_data_list.append(f'{k} = "{v}"')
        RoleEntity.change(cursor_db, old_data_list, new_data_list)

    @staticmethod
    def delete_all(cursor_db, *args, **kwargs):
        RoleEntity.delete_all(cursor_db)


class Subject(AbstractManipulation):
    @staticmethod
    def get(cursor_db, id=None, title=None, *args, **kwargs) -> list:
        role_data = []
        search_list = []
        search_dict = {
            'id': id,
            'title': title,
        }
        if any([id, title]):
            for k, v in search_dict.items():
                if v is not None:
                    search_list.append(f'{k} = "{v}"')
            index = 0
            for item in SubjectEntity.get(cursor_db, search_list):
                role_data.append({'id': item[0], 'title': item[1]})
                index += 1
            return role_data
        else:
            index = 0
            for item in SubjectEntity.get(cursor_db):
                role_data.append({'id': item[0], 'title': item[1]})
                index += 1
            return role_data

    @staticmethod
    def add(cursor_db, title=None, *args, **kwargs) -> None:
        if None not in (title, ):
            SubjectEntity(title=title).add(cursor_db)
        else:
            print("Ошибка ввода")

    @staticmethod
    def delete(cursor_db, is_title=None, *args, **kwargs) -> None:
        del_dict = {
            'title': is_title,
        }
        del_list = []
        for k, v in del_dict.items():
            if v is not None:
                del_list.append(f'{k} = "{v}"')
        SubjectEntity.delete(cursor_db=cursor_db, condition_list=del_list)

    @staticmethod
    def change(
            cursor_db, is_title=None, title=None, *args, **kwargs
    ):
        old_data_dict = {
            'title': is_title,
        }
        new_data_dict = {
            'title': title,
        }
        old_data_list = []
        new_data_list = []
        for k, v in old_data_dict.items():
            if v is not None:
                old_data_list.append(f'{k} = "{v}"')
        for k, v in new_data_dict.items():
            if v is not None:
                new_data_list.append(f'{k} = "{v}"')
        SubjectEntity.change(cursor_db, old_data_list, new_data_list)

    @staticmethod
    def delete_all(cursor_db, *args, **kwargs):
        SubjectEntity.delete_all(cursor_db)


class EducationalMaterial(AbstractManipulation):
    @staticmethod
    def get(
            cursor_db, id=None, title=None, summery=None, material_file=None, subject_id=None, *args, **kwargs
    ) -> list:
        role_data = []
        search_list = []
        search_dict = {
            'id': id,
            'title': title,
            'summery': summery,
            'material_file': material_file,
            'subject_id': subject_id,
        }
        if any([id, title, summery, material_file, subject_id]):
            for k, v in search_dict.items():
                if v is not None:
                    search_list.append(f'{k} = "{v}"')
            index = 0
            for item in EducationalMaterialEntity.get(cursor_db, search_list):
                role_data.append({
                    'id': item[0],
                    'title': item[1],
                    'summery': item[2],
                    'material_file': item[3],
                    'subject_id': item[4],
                })
                index += 1
            return role_data
        else:
            index = 0
            for item in EducationalMaterialEntity.get(cursor_db):
                role_data.append({
                    'id': item[0],
                    'title': item[1],
                    'summery': item[2],
                    'material_file': item[3],
                    'subject_id': item[4],
                })
                index += 1
            return role_data

    @staticmethod
    def add(cursor_db, title=None, summery=None, material_file=None, subject_id=None, *args, **kwargs) -> None:
        if None not in (title, summery, material_file, subject_id):
            EducationalMaterialEntity(
                title=title, summery=summery, material_file=material_file, subject_id=subject_id
            ).add(cursor_db)
        else:
            print("Ошибка ввода")

    @staticmethod
    def delete(cursor_db, is_title=None, *args, **kwargs) -> None:
        del_dict = {
            'title': is_title,
        }
        del_list = []
        for k, v in del_dict.items():
            if v is not None:
                del_list.append(f'{k} = "{v}"')
        EducationalMaterialEntity.delete(cursor_db=cursor_db, condition_list=del_list)

    @staticmethod
    def change(
            cursor_db, is_title=None, title=None, summery=None, material_file=None, subject_id=None, *args, **kwargs
    ):
        old_data_dict = {
            'title': is_title,
        }
        new_data_dict = {
            'title': title,
            'summery': summery,
            'material_file': material_file,
            'subject_id': subject_id,
        }
        old_data_list = []
        new_data_list = []
        for k, v in old_data_dict.items():
            if v is not None:
                old_data_list.append(f'{k} = "{v}"')
        for k, v in new_data_dict.items():
            if v is not None:
                new_data_list.append(f'{k} = "{v}"')
        EducationalMaterialEntity.change(cursor_db, old_data_list, new_data_list)

    @staticmethod
    def delete_all(cursor_db, *args, **kwargs):
        EducationalMaterialEntity.delete_all(cursor_db)


if __name__ == "__main__":
    connection = sqlite3.connect('../school.db')
    cursor = connection.cursor()
#
    # User.add(cursor_db=cursor, username="LOL", login="aba", email="lol@bk.ru", password="3123fas")
#     User.delete(cursor_db=cursor, is_login='aba', is_email='lol@bk.ru')
#     User.change(cursor_db=cursor, is_email="lol@bk.ru", email="ffff@ff.ff")
#     User.delete_all(cursor)
#     Role.add(cursor_db=cursor, title="LOL")
#     Role.change(cursor_db=cursor, is_title="LOL", title="lol")
#     Role.delete(cursor_db=cursor, is_title="lol")
#     EducationalMaterial.add(
#         cursor_db=cursor, title="SOLID", summery="Что такое солид", material_file="README.md", subject_id=1
#     )
#     EducationalMaterial.change(
#         cursor_db=cursor, is_title="SOLID", title="NAAA", summery=None, material_file=None, subject_id=None,
#     )
#     EducationalMaterial.delete(cursor_db=cursor, is_title="SOLID")
    print(Role.get(cursor_db=cursor, title='Admin'))
    print(Role.get(cursor_db=cursor))
    print(Subject.get(cursor_db=cursor, title='SOLID'))
    print(Subject.get(cursor_db=cursor))
    print(User.get(cursor_db=cursor))
    print(User.get(cursor_db=cursor, username='LOL'))
    print(EducationalMaterial.get(cursor_db=cursor))
    print(EducationalMaterial.get(cursor_db=cursor, title='NAAA'))
    connection.commit()

    connection.close()
