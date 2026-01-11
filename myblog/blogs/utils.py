from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import os

# Replace this with a securely generated key
SECRET_KEY = b'\x88\x07Za\xe6\xb0\xe4\xd5\x87\xd3\xf9\xf3jI/\x1c\xad\xb4\xc79\x8f\x06\xbf\x7fFa\xb1A\xef\xdd\x87\xe6'


def encrypt_data(plain_text):
    """
    Encrypt the plain text using AES encryption.
    """
    if not plain_text:
        return None
    iv = os.urandom(16)  # AES block size is 16 bytes
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(plain_text.encode()) + encryptor.finalize()
    return base64.urlsafe_b64encode(iv + encrypted_data).decode()


def decrypt_data(encrypted_text):
    """
    Decrypt the encrypted text using AES encryption.
    """
    if not encrypted_text:
        return None
    encrypted_text_bytes = base64.urlsafe_b64decode(encrypted_text)
    iv = encrypted_text_bytes[:16]
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_text_bytes[16:]) + decryptor.finalize()
    return decrypted_data.decode()