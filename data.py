import random
import string


def generate_email():
    return ''.join(random.choices(string.ascii_lowercase, k=6)) + "@mail.com"


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


def generate_name():
    return ''.join(random.choices(string.ascii_lowercase, k=6))


INGREDIENT = ["61c0c5a71d1f82001bdaaa6d"]

INVALID_INGREDIENT = ["invalid_hash"]