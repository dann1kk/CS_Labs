# TOTP Authenticator (2FA) and Role Based Access Control (RBAC)

## Theory
______________________
&ensp;&ensp;&ensp; TOTP authenticator - the easiest way to add another security layer and secure your online presence from hackers.

&ensp;&ensp;&ensp; TOTP Authenticator allows you to quickly and conveniently protect your accounts by adding 2-factor authentication (2FA). The app brings together best in class security practices and seamless user experience together.


&ensp;&ensp;&ensp; It generates one-time tokens on your device which are used in combination with your password. This helps to protect your accounts from hackers, making your security bulletproof. Just enable the two-factor authentication in your account settings for your provider, scan the QR code provided and you're good to go!

## Implementation
___________________
## Initial Steps
--------------------------------
&ensp;&ensp;&ensp; Create initial database resources using sqlite, in fact two tables with users, email, role and another one with users and their matching otp code.
```
def create_initial_db_resources():
    cursor.execute(Create_USERS_Table)
    cursor.execute(Create_USER_SECRET_Table)
-----------------------------------------------------------
conn = sqlite3.connect('dbdata.db', check_same_thread=False)
cursor = conn.cursor()
```
&ensp;&ensp;&ensp;Behind each of them are requests to manipulate data
```
Create_USERS_Table = "Create table if not exists Users(email varchar unique, password varchar, role varchar)"

Create_USER_SECRET_Table = "Create table if not exists UsersSecret(email varchar unique, totp text)"
```
## Create endpoints
--------------------------------
&ensp;&ensp;&ensp; __Endpoint for registering:__
```
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
        totp = pyotp.TOTP(secret_string)
        create_secret(email, secret_string)
        return {'Setup key': secret_string}
```
&ensp;&ensp;&ensp; __Request and response:__
```{json}
{
    "email":"dan@gmail.com",
    "psw": "dan"
}
```
```{json}
{
    "Setup key": "THORADTZ3ATLAGLLD66AVU5ZSLBENJS3"
}
```
&ensp;&ensp;&ensp; __Endpoint for login:__
```{json}
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
```
&ensp;&ensp;&ensp; __Request and response:__
```{json}
{
    "email":"dan@gmail.com",
    "otp": "245970"
}
```
```{json}
{
    "Logged in successfully!": 200
}
```
&ensp;&ensp;&ensp; __Endpoints for ciphers(each work same way):__
```{json}
@app.route('/playfair', methods=['POST'])
def playfaircipher():
    try:
        data = request.get_json()
        email = data['email']
        message = data['message']
        role = get_role(email)
        user_role = (', '.join(user_role))
        key = data['key']
        if user_role == 'Admin':
            cipher = playfair.encrypt(message, key)
            decrypted = playfair.decrypt(cipher, key)
            return {'Your encrypted message:': cipher,
                    'Your decrypted message:': decrypted}
```
&ensp;&ensp;&ensp; __Request and response:__
```{json}
{
    "email":"dan@gmail.com",
    "message": "mymessage"
    "key": "secret"
}
```
```{json}
{
    "Your decrypted message:": "MYMESXSAGE",
    "Your encrypted message:": "LZITCVAHBT"
}
```

## TOTP Authentication (2FA)
--------------------------
1. __Generate a Setup key after registering__ 
```
secret_string = pyotp.random_base32()
```
2. __Add to the db the setup key and the matching email of the user__
```
create_secret(email, secret_string)
```
3. __Send request to registering endpoint and add setup key from response in Google Authenticator__
4. __Send request to login endpoint using email with which you registered and OTP code generated in Google Authenticator__
```{json}
{
    "email":"dan@gmail.com",
    "otp": "245970"
}
```
## Authorization (RBAC)
1. __It's given by default at registering to all users the role 'Admin'__
2. __When getting a request to a cipher endpoint, check the user role in database__
```
role = get_role(email)
if user_role == 'Admin':
        
else:
    return {'Not enough access rights:': 401}
```