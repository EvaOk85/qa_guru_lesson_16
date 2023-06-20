import requests
from jsonschema.validators import validate

from helper import load_json_schema, CustomSession, reqres_session


def test_requested_page_number():
    page = 2

    response = reqres_session.get('/api/users', params={'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == page

def test_requested_page_number_schema_validation():
    page = 2
    schema = load_json_schema('get_requested_page_number.json')

    response = reqres_session.get('/api/users', params={'page': page})

    validate(instance=response.json(), schema=schema)


def test_users_list_default_length():
    default_users_count = 6

    response = reqres_session.get('/api/users')

    assert len(response.json()['data']) == default_users_count


def test_users_list_default_length_schema_validation():
    schema = load_json_schema('get_users_list_default_length.json')

    response = reqres_session.get('/api/users')

    validate(instance=response.json(), schema=schema)


def test_single_user_not_found():
    response = reqres_session.get('/api/users/23')

    assert response.status_code == 404
    assert response.text == '{}'

def test_single_user_not_found_schema_validation():
    schema = load_json_schema('get_single_user_not_found.json')

    response = reqres_session.get('/api/users/23')

    validate(instance=response.json(), schema=schema)


def test_create_user():
    name = "jane"
    job = "job"

    response = reqres_session.post(
        url='/api/users',
        json={
            "name": name,
            "job": job}
    )

    assert response.status_code == 201
    assert response.json()['name'] == name

def test_create_user_schema_validation():
    name = "jane"
    job = "job"
    schema = load_json_schema('post_create_user.json')

    response = reqres_session.post(
        url='/api/users',
        json={
            "name": name,
            "job": job}
    )

    validate(instance=response.json(), schema=schema)


def test_update_user():
    name = "Fill"
    job = "leader"

    response = reqres_session.put("/api/users/23", json={"name": name, "job": job})

    assert response.status_code == 200
    assert response.json()["name"] == name



def test_put_update_user_schema_validation():
    name = "Fill"
    job = "leader"

    schema = load_json_schema("put_update_user_schema.json")

    response = reqres_session.put("/api/users/23", json={"name": name, "job": job})

    validate(instance=response.json(), schema=schema)



def test_requested_total_number():
    total = 12

    response = reqres_session.get('/api/users', params={'total': total})

    assert response.status_code == 200
    assert response.json()['total'] == total

def test_requested_total_number_schema_validation():
    total = 12

    schema = load_json_schema("get_requested_total_number.json")

    response = reqres_session.get('/api/users', params={'total': total})

    validate(instance=response.json(), schema=schema)


def test_register_user_error():
    response = reqres_session.post(
        url='/api/register',
        json={
            "email": "sydney@fife"
        }
    )
    print(response.text)
    assert response.status_code == 400
    assert response.text == '{"error":"Missing password"}'

def test_register_user_error_schema_validation():

    schema = load_json_schema("post_register_user_error.json")

    response = reqres_session.post(
        url='/api/register',
        json={
            "email": "sydney@fife"
        }
    )

    validate(instance=response.json(), schema=schema)


def test_registration_successful():
    token = 'QpwL5tke4Pnpja7X4'

    response = reqres_session.post(
        url='/api/register',
        json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
    )

    assert response.status_code == 200
    assert response.json()['token'] == token

def test_registration_successful_schema_validation():

    schema = load_json_schema("post_registration_successful.json")

    response = reqres_session.post(
        url='/api/register',
        json={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
    )

    validate(instance=response.json(), schema=schema)

def test_authorization_successful_():

    response = reqres_session.post(
        url='/api/login',
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    assert response.status_code == 200
    assert response.text == '{"token":"QpwL5tke4Pnpja7X4"}'

def test_authorization_successful_schema_validation():

    schema = load_json_schema("post_authorization_successful.json")

    response = reqres_session.post(
        url='/api/login',
        json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
    )

    validate(instance=response.json(), schema=schema)

def test_users_list_count_length():
    default_users_count = 7

    response = reqres_session.get('/api/users')

    assert len(response.json()['data']) != default_users_count

def test_users_list_count_length_schema_validation():


    schema = load_json_schema("get_users_list_count_length.json")

    response = reqres_session.get('/api/users')

    validate(instance=response.json(), schema=schema)
