from basicauth import encode

username, password = 'username','password'
auth = encode(username, password)
print(auth)