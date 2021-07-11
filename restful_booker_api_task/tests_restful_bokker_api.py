import requests

from restful_booker_api_task import urls, headers


def test_restful_booker_crud(username_password_data, booking_data):
    create_token_response = requests.post(url=urls.CREATE_TOKEN_URL,
                                          headers=headers.HEADER_JSON,
                                          json=username_password_data)
    assert create_token_response.status_code == 200
    TOKEN = create_token_response.json()
    print(TOKEN)

    get_booking_ids = requests.get(url=urls.BOOKING_URL)
    assert get_booking_ids.status_code == 200
    assert type(get_booking_ids.json()) is list
    id = get_booking_ids.json()[0]['bookingid']

    updatebooking_response = requests.put(url=urls.BOOKING_URL + f"/{id}",
                                          headers=headers.NEWHEADERvsACCEPT |
                                                  {'Cookie': f'token={TOKEN["token"]}'},
                                          json=booking_data)
    assert updatebooking_response.status_code == 200

    get_booking_id_vs_parameters_response = requests.get(url=urls.BOOKING_URL,
                                                         params={"firstname": booking_data['firstname']})
    assert get_booking_id_vs_parameters_response.status_code == 200
    assert get_booking_id_vs_parameters_response.json()[0]['bookingid'] == id

    get_booking_response = requests.get(url=urls.BOOKING_URL + f"/{id}",
                                        headers=headers.NEWHEADERvsACCEPT)
    assert get_booking_response.status_code == 200
    assert get_booking_response.json()['firstname'] == "Osachi"
    assert get_booking_response.status_code == 200
    assert get_booking_response.json()['lastname'] == "Roman"

    booking_response = requests.post(url=urls.BOOKING_URL, json=booking_data, headers=headers.HEADER_JSON)
    assert booking_response.status_code == 200
    new_booking_id = booking_response.json()['bookingid']
    print(f'new id  - {new_booking_id}')

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

    delete_booking_response = requests.delete(url=urls.BOOKING_URL+f"/{new_booking_id}",
                                              headers=headers.NEWHEADERvsACCEPT |
                                                             {'Cookie': f'token={TOKEN["token"]}'})
    assert delete_booking_response.status_code == 201
    get_booking_response = requests.get(url=urls.BOOKING_URL + f"/{new_booking_id}",
                                        headers=headers.NEWHEADERvsACCEPT)
    assert get_booking_response.status_code == 404
