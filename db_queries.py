Create_USERS_Table = "Create table if not exists Users(email varchar unique, password varchar, role varchar)"

Create_USER_SECRET_Table = "Create table if not exists UsersSecret(email varchar unique, totp text)"

Insert_User = "Insert into Users(email, password, role) values(:email, :password, :role)"

Insert_User_Secret = "Insert into UsersSecret(email, totp) values(:email, :totp)"

Fetch_User_Secret = "Select email, totp from UsersSecret where email=:email"

Fetch_User_Role = "Select role from Users where email=:email"

Fetch_User = "Select email from Users where email=:email"
