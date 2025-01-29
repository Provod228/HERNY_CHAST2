import hashlib
import sqlite3
import os
from abc import ABCMeta, abstractmethod


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get(self, cursor_db):
        pass

    @abstractmethod
    def add(self, cursor_db):
        pass

    @abstractmethod
    def delete(self, cursor_db, condition_list):
        pass

    @abstractmethod
    def change(self, cursor_db, condition_list, change_list):
        pass

    @abstractmethod
    def delete_all(self, cursor_db):
        pass


class UserEntity(Entity):
    def __new__(
            cls, username=None, login=None, email=None, password=None, role_id=1,
    ):
        cls.instance = super().__new__(cls)
        cls.instance.username = username
        cls.instance.login = login
        cls.instance.email = email
        cls.instance.password = hash_password(password)
        cls.instance.role_id = role_id
        return cls.instance

    @classmethod
    def get(cls, cursor_db, condition_list=None):
        try:
            if condition_list is None:
                cursor_db.execute(
                    "Select *"
                    "from User"
                )
                return cursor_db.fetchall()
            else:
                cursor_db.execute(
                    f"Select *"
                    f"from User Where {' and '.join(condition_list)}"
                )
                return cursor_db.fetchall()
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def add(cls, cursor_db):
        try:
            cursor_db.execute(
                "INSERT INTO User "
                "(username, login, email, password, role_id)"
                "VALUES (?, ?, ?, ?, ?)",
                (
                    cls.instance.username, cls.instance.login, cls.instance.email,
                    cls.instance.password, cls.instance.role_id,
                )
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete(cls, cursor_db, condition_list):
        try:
            cursor_db.execute(
                f'DELETE FROM User where {' and '.join(condition_list)}'
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, cursor_db, condition_list, change_list):
        for change_list_index in range(len(change_list)):
            if "password" in change_list[change_list_index]:
                list_change = change_list[change_list_index].split('"')
                password = hash_password(list_change[1])
                new_password = list_change[0] + '"' + password + '"'
                change_list.pop(change_list_index)
                change_list.append(new_password)
        try:
            cursor_db.execute(
                f"UPDATE User "
                f"SET {', '.join(change_list)} "
                f"Where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls, cursor_db):
        try:
            cursor_db.execute(
                f"DELETE FROM User"
            )
        except Exception as error:
            print(f"Error: {error}")


class EducationalMaterialEntity(Entity):
    def __new__(
            cls, title=None, summery=None, material_file=None, subject_id=None,
    ):
        cls.instance = super().__new__(cls)
        cls.instance.title = title
        cls.instance.summery = summery
        cls.instance.material_file = material_file
        cls.instance.subject_id = subject_id
        return cls.instance

    @classmethod
    def get(cls, cursor_db, condition_list=None):
        try:
            if condition_list is None:
                cursor_db.execute(
                    "Select *"
                    "from EducationalMaterial"
                )
                return cursor_db.fetchall()
            else:
                cursor_db.execute(
                    f"Select *"
                    f"from EducationalMaterial Where {' and '.join(condition_list)}"
                )
                return cursor_db.fetchall()
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def add(cls, cursor_db):
        try:
            cursor_db.execute(
                "INSERT INTO EducationalMaterial "
                "(title, summery, material_file, subject_id)"
                "VALUES (?, ?, ?, ?)",
                (
                    cls.instance.title, cls.instance.summery,
                    cls.instance.material_file, cls.instance.subject_id,
                )
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete(cls, cursor_db, condition_list):
        try:
            cursor_db.execute(
                f"DELETE FROM EducationalMaterial where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, cursor_db, condition_list, change_list):
        try:
            cursor_db.execute(
                f"UPDATE EducationalMaterial "
                f"SET {', '.join(change_list)} "
                f"Where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls, cursor_db):
        try:
            cursor_db.execute(
                f"DELETE FROM EducationalMaterial"
            )
        except Exception as error:
            print(f"Error: {error}")


class RoleEntity(Entity):
    def __new__(
            cls, title=None,
    ):
        cls.instance = super().__new__(cls)
        cls.instance.title = title
        return cls.instance

    @classmethod
    def get(cls, cursor_db, condition_list=None):
        try:
            if condition_list is None:
                cursor_db.execute(
                    "Select *"
                    "from Role"
                )
                return cursor_db.fetchall()
            else:
                cursor_db.execute(
                    f"Select *"
                    f"from Role "
                    f"Where {' and '.join(condition_list)}"
                )
                return cursor_db.fetchall()
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def add(cls, cursor_db):
        try:
            cursor_db.execute(
                "INSERT INTO Role "
                "(title)"
                "VALUES (?)",
                (
                    cls.instance.title,
                )
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete(cls, cursor_db, condition_list):
        try:
            cursor_db.execute(
                f"DELETE FROM Role where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, cursor_db, condition_list, change_list):
        try:
            cursor_db.execute(
                f"UPDATE Role "
                f"SET {', '.join(change_list)} "
                f"Where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls, cursor_db):
        try:
            cursor_db.execute(
                f"DELETE FROM Role"
            )
        except Exception as error:
            print(f"Error: {error}")


class SubjectEntity(Entity):
    def __new__(
            cls, title=None,
    ):
        cls.instance = super().__new__(cls)
        cls.instance.title = title
        return cls.instance

    @classmethod
    def get(cls, cursor_db, condition_list=None):
        try:
            if condition_list is None:
                cursor_db.execute(
                    "Select *"
                    "from Subject"
                )
                return cursor_db.fetchall()
            else:
                cursor_db.execute(
                    f"Select *"
                    f"from Subject Where {' and '.join(condition_list)}"
                )
                return cursor_db.fetchall()
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def add(cls, cursor_db):
        try:
            cursor_db.execute(
                "INSERT INTO Subject "
                "(title)"
                "VALUES (?)",
                (
                    cls.instance.title,
                )
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete(cls, cursor_db, condition_list):
        try:
            cursor_db.execute(
                f"DELETE FROM Subject where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def change(cls, cursor_db, condition_list, change_list):
        try:
            cursor_db.execute(
                f"UPDATE Subject "
                f"SET {', '.join(change_list)} "
                f"Where {' and '.join(condition_list)}"
            )
        except Exception as error:
            print(f"Error: {error}")

    @classmethod
    def delete_all(cls, cursor_db):
        try:
            cursor_db.execute(
                f"DELETE FROM Subject"
            )
        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    data_base_file = '../school.db'
    if os.path.exists(data_base_file):
        connection = sqlite3.connect(data_base_file)
        cursor = connection.cursor()
        # User.delete_all(cursor)
        # Role(name_role="Пользователь").add(cursor)
        # Role(name_role="Менеджер").add(cursor)
        # Role(name_role="Администратор").add(cursor)
        # Role.delete_all(cursor)
        # Role.change(cursor, ['name_role="Пользователь"'], ['name_role="user"'])
        # Status(name_status="Активный").add(cursor)
        # Status(name_status="Уточнение").add(cursor)
        # Status(name_status="Не активный").add(cursor)
        # Status(name_status="Удалён").add(cursor)
        # Status.delete_all(cursor)
        # Status.change(cursor, ['name_status="активен"'], ['name_status="activ"'])
        # Status.delete_all()
        # User(
        #     name_user="Ignat", login_user="aaa", mail_user="ggg@mail.ru", password_user="123",
        #     time_add_user=datetime.datetime.today(), time_status_change_user=datetime.datetime(2025, 1, 1),
        #     status_user=1, role_user=1,
        # ).add(cursor)
        # User.delete('name_user="Ignat"')
        # User.change(cursor, ['login_user="aaa"'], ['status_user="4"'])
        # print(UserEntity.get(cursor_db=cursor))
        # print(RoleEntity.get(cursor_db=cursor, condition_list=["title='User'"]))
        # print(EducationalMaterialEntity.get(cursor_db=cursor))
        # print(SubjectEntity.get(cursor_db=cursor))
        connection.commit()

        connection.close()
    else:
        print(f"База данных '{data_base_file}' не существует.")

