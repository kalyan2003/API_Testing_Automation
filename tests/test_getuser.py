import pytest
from oauthlib.oauth2 import OAuth2Token

from utils.apis import APIS
from data.contact_data import *


@pytest.fixture(scope='module')
def apis():
    return APIS()


@pytest.fixture(scope='module')
def register_user(apis):
    user_data = generate_random_user()
    response = apis.register(user_data)
    print(response.status_code, response.json())

    data = response.json()
    authToken = data.get("token")
    email = user_data.get("email")
    id = data.get("user", {}).get("_id")

    print(f"authToken: {authToken}")
    print(f"email: {email}")
    print(f"Id : {id}")

    assert response.status_code == 201

    return {
        "token": authToken,
        "email": email,
        "id": id
    }



def test_register_user(register_user):
    assert register_user is not None


def test_get_user(apis,register_user):
    authToken = register_user["token"]
    response = apis.get("users/me",authToken)
    print(f"authtoken is:{register_user}")
    print(response.status_code,response.json())
    assert response.status_code == 200

def test_patch_user(apis,register_user):
    authToken = register_user["token"]
    user_data = partial_update_data()
    response = apis.patch("users/me",authToken,user_data)
    print(response.status_code,response.json())
    assert response.status_code == 200


# def test_log_out_user(apis,register_user):
#     authToken = register_user["token"]
#     response = apis.log_out_user("users/logout",authToken)
#     print(response.status_code)
#     assert response.status_code == 200
#
# def test_log_in_user(apis,register_user):
#     log_in_data = {
#         "email": register_user["email"],
#         "password": "myPassword"
#     }
#     response = apis.log_in_user("users/login",log_in_data)
#     print(response.status_code, response.json())
#     assert response.status_code == 200


# def test_delete_users(apis, register_user):
#     authToken = register_user["token"]
#     response = apis.delete_user("users/me", authToken)
#     print(response.status_code)
#     assert response.status_code == 200
#

@pytest.fixture(scope='module')
def add_contact(apis, register_user):
    contact_data = {
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }
    authToken = register_user["token"]
    response = apis.add_contact("contacts", authToken, contact_data)
    assert response.status_code == 201
    contact_id = response.json().get("_id")
    return contact_id

def test_add_contact(add_contact):
    assert add_contact is not None


def test_get_contact(register_user,apis):
    authToken = register_user["token"]
    response = apis.get_contact("contacts/",authToken)
    assert response.status_code == 200

