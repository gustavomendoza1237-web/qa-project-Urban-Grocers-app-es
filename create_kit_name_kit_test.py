import sender_stand_request
import data

create_user_response = sender_stand_request.create_user(data.user_body)
auth_token = create_user_response.json()["authToken"]


def positive_assert_kit(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_kit(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400


def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = {"name": "a"}
    positive_assert_kit(kit_body)


def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = {"name": data.kit_name_511_characters}
    positive_assert_kit(kit_body)


def test_create_kit_0_letter_in_name_get_error_response():
    kit_body = {"name": ""}
    negative_assert_kit(kit_body)


def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = {"name": data.kit_name_512_characters}
    negative_assert_kit(kit_body)


def test_create_kit_has_special_symbol_in_name_get_success_response():
    kit_body = {"name": data.kit_name_special_characters}
    positive_assert_kit(kit_body)


def test_create_kit_has_space_in_name_get_success_response():
    kit_body = {"name": data.kit_name_with_spaces}
    positive_assert_kit(kit_body)


def test_create_kit_has_number_as_text_in_name_get_success_response():
    kit_body = {"name": data.kit_name_numbers_as_text}
    positive_assert_kit(kit_body)


def test_create_kit_no_name_parameter_get_error_response():
    kit_body = {}
    negative_assert_kit(kit_body)


def test_create_kit_number_type_name_get_error_response():
    kit_body = {"name": 123}
    negative_assert_kit(kit_body)