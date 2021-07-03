import requests

from restful_booker_api_task import urls, headers


def test_creation_token_crud(username_password_data):
    create_token_response = requests.post(url=urls.CREATE_TOKEN_URL,
                                          headers=headers.HEADER_JSON,
                                          json=username_password_data)
    assert create_token_response.status_code == 200
    global TOKEN
    TOKEN = create_token_response.json()
    print(TOKEN)


def test_getbookingids():
    get_booking_ids = requests.get(url=urls.BOOKING_URL)
    assert get_booking_ids.status_code == 200
    assert type(get_booking_ids.json()) is list
    global id
    id = get_booking_ids.json()[0]['bookingid']


def test_updatebooking_crud(booking_data):
    updatebooking_response = requests.put(url=urls.BOOKING_URL + f"/{id}",
                                          headers=headers.NEWHEADERvsACCEPT |
                                                  {'Cookie': f'token={TOKEN["token"]}'},
                                          json=booking_data)

    assert updatebooking_response.status_code == 200
    print(updatebooking_response.json())


def test_get_booking_id_vs_parametrs(booking_data):
    get_booking_id_vs_parameters_response = requests.get(url=urls.BOOKING_URL,
                                                         params={"firstname": booking_data['firstname']})
    assert get_booking_id_vs_parameters_response.status_code == 200
    assert get_booking_id_vs_parameters_response.json()[0]['bookingid'] == id
    print(get_booking_id_vs_parameters_response.json())


def test_get_booking():
    get_booking_response = requests.get(url=urls.BOOKING_URL + f"/{id}",
                                        headers=headers.NEWHEADERvsACCEPT)
    assert get_booking_response.status_code == 200
    assert get_booking_response.json()['firstname'] == "Osachi"

    assert get_booking_response.status_code == 200
    assert get_booking_response.json()['lastname'] == "Roman"


def test_createbooking_crud(booking_data):
    booking_response = requests.post(url=urls.BOOKING_URL, json=booking_data, headers=headers.HEADER_JSON)
    assert booking_response.status_code == 200
    print(booking_response.json())
    global new_booking_id
    new_booking_id = booking_response.json()['bookingid']
    print(new_booking_id)


def test_partialupdatebooking():
    partial_update_booking_response = requests.patch(url=urls.BOOKING_URL + f"/{new_booking_id}",
                                                     headers=headers.NEWHEADERvsACCEPT |
                                                             {'Cookie': f'token={TOKEN["token"]}'},
                                                     json={
                                                         'firstname': 'Roman',
                                                         'lastname': 'Osachi',
                                                         'additionalneeds': 'sluts'
                                                     }
                                                     )
    assert partial_update_booking_response.status_code == 200
    assert partial_update_booking_response.json()['firstname'] == "Roman"
    assert partial_update_booking_response.json()['lastname'] == 'Osachi'
    print(partial_update_booking_response.json())

def test_delete_booking():
    delete_booking_response = requests.delete(url=urls.BOOKING_URL+f"/{new_booking_id}",
                                              headers=headers.NEWHEADERvsACCEPT |
                                                             {'Cookie': f'token={TOKEN["token"]}'})
    assert delete_booking_response.status_code == 201
    get_booking_response = requests.get(url=urls.BOOKING_URL + f"/{new_booking_id}",
                                        headers=headers.NEWHEADERvsACCEPT)
    assert get_booking_response.status_code == 404
