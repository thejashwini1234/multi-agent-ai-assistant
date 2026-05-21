def validate_response(response):

    if len(str(response)) < 5:

        return "Invalid response"

    return "Validated"