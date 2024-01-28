from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64decode, b64encode

class DecryptionError(Exception):
    pass

class EncryptionError(Exception):
    pass

def AK_encrypt(secret_key,text):
    try:
        secret_key = secret_key.encode('utf-8')
        iv = secret_key[:16]
        text = str(text)
        cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv), backend=default_backend())
        block_size = algorithms.AES.block_size // 8
        padder = lambda data: data + (block_size - len(data) % block_size) * bytes([block_size - len(data) % block_size])
        padded_data = padder(text.encode())

        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        ciphertext = b64encode(ciphertext)
        return ciphertext.decode('utf-8')
    except Exception as e:
        raise EncryptionError(e) 

def AK_decrypt(secret_key,ciphertext):
    try:
        secret_key=secret_key.encode('utf-8')
        iv = secret_key[:16]
        cipher = Cipher(algorithms.AES(secret_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        # Make sure the ciphertext is of type bytes
        if isinstance(ciphertext, str):
            ciphertext = b64decode(ciphertext)

        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        # Remove padding
        unpadder = padding.PKCS7(128).unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

        decoded = unpadded_data.decode()

        return decoded
        
    except Exception as e:
        raise DecryptionError(e)
    



