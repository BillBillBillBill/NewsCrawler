
err_code_message = {
    '10000': 'Unknown Error',
    '10001': 'Bad Request',
    '10005': 'Internal Error(Json Dumps Error)',
    '99999': 'Jsonschema Check Fail',
}


def get_message(err_code):
    return err_code_message.get(str(err_code), "Undefined Error Code")
