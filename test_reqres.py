
"""
Параметр, показывающий, что все поля обязательные
        required=True,

Параметр, показывающий, что дополнительных полей не должно передаваться
        extra=PREVENT_EXTRA

Параметр, показывающий, что дополнительных полей не должно передаваться
        extra=ALLOW_EXTRA
"""

import requests
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA, Optional
from pytest_voluptuous import S

#Schemas
get_single_user_schema = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            Optional("avatar"): str
        },
        "support": {
            "url": str,
            "text": str
        }
    },
    required=True,
    extra=PREVENT_EXTRA
)

post_create_user_schema = Schema(
        {
            "name": str,
            Optional("job"): str,
            "id": str,
            "createdAt": str
        },
        required=True,
        extra=PREVENT_EXTRA
    )

put_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

post_register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA
)


def test_get_single_user():
    response: Response = requests.get("https://reqres.in/api/users/2")

    assert response.status_code == 200
    assert response.json() == S(get_single_user_schema)
    assert response.json()['data']['id'] == 2
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'
    assert response.json()['data']['first_name'] == 'Janet'
    assert response.json()['data']['last_name'] == 'Weaver'


def test_post_create_user():
    name = 'Gandalf'
    job = 'wizard'

    create = requests.post(
        url="https://reqres.in/api/users",
        json={"name": name, "job": job}
    )

    assert create.status_code == 201
    assert create.json() == S(post_create_user_schema)
    assert create.json()["name"] == name
    assert create.json()["job"] == job
    assert isinstance(create.json()["id"], str)
    assert isinstance(create.json()["createdAt"], str)


def test_put_user():
    name = 'morpheus'
    job = 'zion resident'

    update = requests.put(
        url='https://reqres.in/api/users/2',
        json={"name": name, "job": job}
    )

    assert update.status_code == 200
    assert update.json() == S(put_user_schema)
    assert update.json()['name'] == name
    assert update.json()['job'] == job


def test_delete_user():
    result = requests.delete('https://reqres.in/api/users/2')
    assert result.status_code == 204


def test_post_register_user():
    email = "eve.holt@reqres.in"
    password = "pistol"

    register = requests.post(
        url='https://reqres.in/api/register',
        json={
            "email": email,
            "password": password
        }
    )

    assert register.status_code == 200
    assert register.json() == S(post_register_user_schema)
    assert register.json()["id"] == 4
    assert isinstance(register.json()["id"], int)
    assert register.json()["token"] == "QpwL5tke4Pnpja7X4"
    assert isinstance(register.json()["token"], str)

