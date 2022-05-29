import pyotp

secret = pyotp.random_base32()
print("mi secreto:", secret)

totp_object = pyotp.TOTP(secret)
qr_text = totp_object.provisioning_uri(name="mi_usuario", 
issuer_name="App TOTP Python")
print(qr_text)

otp=input("ingresa el otp: ")
valid = totp_object.verify(otp)
print(valid)











