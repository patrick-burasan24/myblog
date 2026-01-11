from django.db import models
from .utils import encrypt_data, decrypt_data

class EncryptedField(models.TextField):
    """
    A custom Django model field for encrypting and decrypting data using AES.
    """

    def from_db_value(self, value, expression, connection):
        """
        Decrypt the value when reading from the database.
        """
        if value is None:
            return value
        return decrypt_data(value)

    def get_prep_value(self, value):
        """
        Encrypt the value before saving it to the database.
        """
        if value is None:
            return value
        return encrypt_data(value)