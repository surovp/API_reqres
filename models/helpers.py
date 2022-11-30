import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("base_url")


def data_create_user():
    data = {
        'name': 'Gandalf',
        'job': 'wizard'
    }
    return data


def data_edit_user():
    data = {
        'name': 'morpheus',
        'job': 'zion resident'
    }
    return data


def data_register_user():
    data = {
        'email': "eve.holt@reqres.in",
        'password': "pistol"
    }
    return data

