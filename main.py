from models.data import users
from utis.crud import read

if __name__ == '__main__':
    print(f'Witaj {users[0]["name"]}')


    read(users)

