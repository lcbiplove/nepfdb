def checkNumberAndAlpha(value):
    """Check if string contains at least one number
    and an alphabet"""
    is_alpha = False
    is_num = False

    for i in str(value):
        if i.isalpha():
            is_alpha = True

        if i.isdigit():
            is_num = True

    return is_alpha and is_num


def checkAlphaAndSpace(value):
    value = str(value).strip()
    return all(x.isalpha() or x.isspace() for x in value)
