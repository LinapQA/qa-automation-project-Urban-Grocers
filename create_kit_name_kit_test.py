import sender_stand_request
import data


# Función de prueba positiva
def positive_assert(kit_response , expected_status_code , expected_name):
    assert kit_response.status_code == expected_status_code
    assert kit_response.json()["name"] == expected_name


# Función de prueba negativa
def negative_assert(kit_response , expected_status_code):
    assert kit_response.status_code == expected_status_code


# Test 1. The allowed number of characters (1):
def test_create_kit_name_1():
    data.kit_body = data.kit_body["one_character"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , data.kit_body["name"])


# Test 2. The allowed number of characters (511):
def test_create_kit_name_2():
    data.kit_body = data.kit_body["maximum_characters"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , data.kit_body["name"])


# Test 3. The number of characters is less than the allowed amount (0):
def test_create_kit_name_3():
    data.kit_body = data.kit_body["empty_field"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    negative_assert(kit_response , 400)


# Test 4. The number of characters is greater than the allowed amount (512):
def test_create_kit_name_4():
    data.kit_body = data.kit_body["number_of_characters_is_higher"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    negative_assert(kit_response , 400)


# Test 5. Special characters are allowed:
def test_create_kit_name_5():
    data.kit_body = data.kit_body["special_characters"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , data.kit_body["name"])


# Test 6. Spaces are allowed:
def test_create_kit_name_6():
    data.kit_body = data.kit_body["spaces"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , data.kit_body["name"])


# Test 7. Numbers are allowed:
def test_create_kit_name_7():
    data.kit_body = data.kit_body["numbers"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    positive_assert(kit_response , 201 , data.kit_body["name"])


# Test 8. The parameter is not passed in the request:
def test_create_kit_name_8():
    data.kit_body = data.kit_body["there_is_no_parameter"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    negative_assert(kit_response , 400)


# Test 9. A different parameter type (number) has been passed:
def test_create_kit_name_9():
    data.kit_body = data.kit_body["different_parameter_(number)"]
    kit_response = sender_stand_request.post_new_client_kit(data.kit_body)
    negative_assert(kit_response , 400)
