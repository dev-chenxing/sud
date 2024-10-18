import regex


def is_chinese(string: str):
    if not string:
        return False
    return not not regex.findall(r'^\p{Han}+$', string)
