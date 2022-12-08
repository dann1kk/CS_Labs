from Ciphers import stream
from Ciphers import vigenere
from Ciphers import caesar_substitution
from Ciphers import caesar_permutation
from Ciphers import playfair
from Ciphers import block
from Ciphers import rsa
from Ciphers import sha256
import struct, codecs, hashlib
import pyotp
from flask import Flask, request
from flask import render_template
db = []

from db import create_initial_db_resources, create_user, create_secret, get_secret, get_role

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET"


@app.route('/caesar', methods=['POST'])
def caesar():
    try:
        data = request.get_json()
        email = data['email']
        role = get_role(email)
        user_role = role[0]
        user_role = (', '.join(user_role))
        print(user_role)
        message = data['message']
        message_lower = message.lower()
        if user_role == 'Admin':
            cipher = caesar_substitution.encrypt(message_lower, caesar_substitution.shift,
                                             caesar_substitution.letter_to_index,
                                             caesar_substitution.index_to_letter)
            decrypted = caesar_substitution.decrypt(cipher, caesar_substitution.shift, caesar_substitution.letter_to_index,
                                                caesar_substitution.index_to_letter)
            return {'Your encrypted message:': cipher,
                    'Your decrypted message:': decrypted}
        else:
            return {'Not enough access rights:': 401}
    except Exception as e:
        print(str(e))
        return {'status_code': 404}


@app.route('/caesarpermutation', methods=['POST'])
def caesarpermutation():
    try:
        data = request.get_json()
        email = data['email']
        message = data['message']
        role = get_role(email)
        user_role = role[0]
        user_role = (', '.join(user_role))
        message_lower = message.lower()
        if user_role == 'Admin':
            cipher = caesar_permutation.encrypt(message_lower, caesar_permutation.shift, caesar_permutation.letter_to_index,
                                            caesar_permutation.index_to_letter)
            decrypted = caesar_permutation.decrypt(cipher, caesar_permutation.shift, caesar_permutation.letter_to_index,
                                               caesar_permutation.index_to_letter)
            return {'Your encrypted message:': cipher,
                    'Your decrypted message:': decrypted}
        else:
            return {'Not enough access rights:': 401}
    except Exception as e:
        print(str(e))
        return {'status_code': 404}


@app.route('/vigenere', methods=['POST'])
def vigenerecipher():
    try:
        data = request.get_json()
        email = data['email']
        message = data['message']
        role = get_role(email)
        user_role = role[0]
        user_role = (', '.join(user_role))
        key = data['key']
        message_lower = message.lower()
        if user_role == 'Admin':
            cipher = vigenere.encrypt(message_lower, key, vigenere.alphabet, vigenere.letter_to_index,
                                  vigenere.index_to_letter)
            decrypted = vigenere.decrypt(cipher, key, vigenere.alphabet, vigenere.letter_to_index, vigenere.index_to_letter)
            return {'Your encrypted message:': cipher,
                    'Your decrypted message:': decrypted}
        else:
            return {'Not enough access rights:': 401}
    except Exception as e:
        print(str(e))
        return {'status_code': 404}


@app.route('/playfair', methods=['POST'])
def playfaircipher():
    try:
        data = request.get_json()
        email = data['email']
        message = data['message']
        role = get_role(email)
        user_role = role[0]
        user_role = (', '.join(user_role))
        key = data['key']
        if user_role == 'Admin':
            cipher = playfair.encrypt(message, key)
            decrypted = playfair.decrypt(cipher, key)
            return {'Your encrypted message:': cipher,
                    'Your decrypted message:': decrypted}
        else:
            return {'Not enough access rights:': 401}
    except Exception as e:
        print(str(e))
        return {'status_code': 404}


@app.route('/stream', methods=['POST'])
def streamcipher():
    try:
        data = request.get_json()
        email = data['email']
        message = data['message']
        role = get_role(email)
        user_role = role[0]
        user_role = (', '.join(user_role))
        newKey = stream.randomKey()
        if user_role == 'Admin':
            for i in range(2):
                encryption = stream.encrypt(message, newKey)
                res = stream.encrypt(encryption, newKey)

            for i in range(2):
                decryption = stream.decrypt(res, newKey)
                res2 = stream.decrypt(decryption, newKey)
            return {'Your encrypted message:': res,
                    'Your decrypted message:': res2}
        else:
            return {'Not enough access rights:': 401}
    except Exception as e:
        print(str(e))
        return {'status_code': 404}


@app.route('/block', methods=['POST'])
def blockcipher():
    try:
        data = request.get_json()
        email = data['email']
        message = data['message']
        key = data['key']
        b_ciph = block.blowfish(key)
        role = get_role(email)
        user_role = role[0]
        user_role = (', '.join(user_role))
        if user_role == 'Admin':
            encrypted = b_ciph.encrypt(message)
            decrypted_bytes = b_ciph.decrypt(encrypted)
            decrypted = decrypted_bytes.decode()
            return {'Your encrypted message:': encrypted,
                    'Your decrypted message:': decrypted}
        else:
            return {'Not enough access rights:': 401}
    except Exception as e:
        print(str(e))
        return {'status_code': 404}


@app.route('/rsa', methods=['POST'])
def rsacipher():
    try:
        data = request.get_json()
        email = data['email']
        message = data['message']
        role = get_role(email)
        user_role = role[0]
        user_role = (', '.join(user_role))
        public, private = rsa.generate_key_pair(rsa.p, rsa.q)
        if user_role == 'Admin':
            encrypted = rsa.encrypt(public, message)
            decrypted = rsa.decrypt(private, encrypted)
            encrypted_m =  ''.join(map(lambda x: str(x) + " ", encrypted))
            return {'Your encrypted message:': encrypted_m,
                    'Your decrypted message:': decrypted}
        else:
            return {'Not enough access rights:': 401}
    except Exception as e:
        print(str(e))
        return {'status_code': 404}


@app.route('/sha256', methods=['POST'])
def hashing():
    try:
        data = request.get_json()
        email = data['email']
        message = data['message']
        role = get_role(email)
        user_role = role[0]
        user_role = (', '.join(user_role))
        public, private = rsa.generate_key_pair(rsa.p, rsa.q)
        byte_message = bytes(message, 'UTF-8')
        digest = codecs.encode(sha256.sha256_sum(byte_message), 'hex').decode()
        db.append(digest)
        if user_role == 'Admin':
            encrypted = rsa.encrypt(public, digest)
            db.append(encrypted)
            encrypted_db = db[1]
            decrypted = rsa.decrypt(private, encrypted_db)
            digest_db = db[0]
            mess = ''
            print("Decrypted message:", decrypted)
            if (decrypted == digest_db):
                mess = "Digital signature check successfully performed!"
            else:
                print("Error!")
            return {'Your encrypted message:': encrypted,
                    'Your decrypted message:': decrypted,
                    '': mess}
        else:
            return {'Not enough access rights:': 401}
    except Exception as e:
        print(str(e))
        return {'status_code': 404}


@app.route('/')
def create_account():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data['email']
        password = data['psw']
        print("Creating user")
        # give default role for all users 'Admin'
        role = "Admin"
        create_user(email, password, role)
        secret_string = pyotp.random_base32()
        print(secret_string)
        totp = pyotp.TOTP(secret_string)
        create_secret(email, secret_string)
        print(totp.now())
        return {'Setup key': secret_string}
    except Exception as e:
        print(str(e))
        return {'Access forbidden': 403}


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data['email']
        otp = data['otp']
        user = get_secret(email)
        print(user)
        totp = user[0][1]
        totp = pyotp.TOTP(totp)
        print(otp)
        print(totp.now())
        if totp.now() != otp:
            return {'Access forbidden': 403}
        return {'Logged in successfully!': 200}
    except Exception as e:
        print(str(e))
        return {'Access forbidden': 403}


if __name__ == "__main__":
    create_initial_db_resources()
    app.run(debug=True)


def start_app():
    return app
