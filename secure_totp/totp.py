import pyotp

#secret = pyotp.random_base32()
secret = "QWRSBXXD2CWCHHDKKAXVIO3KFJ5WIHZV"
print("mi secreto:", secret)

totp_object = pyotp.TOTP(secret)
qr_text = totp_object.provisioning_uri(name="mi_usuario", 
issuer_name="Mi App")
print(qr_text)

otp=input("ingresa el otp: ") #imprimo por pantalle el codigo
valid = totp_object.verify(otp)
print(valid)











