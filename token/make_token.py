from jose import jwt,JWTError
from datetime import datetime,timedelta 
import secrets

SECREATE_KEY = secrets.token_hex(64) 
ALGORITHM = "HS256" 

payload ={
    "name":"sujal",
    "role":"admin"
}

expire = datetime.utcnow()+ timedelta(minutes=10) 
payload["exp"] = expire 

# print(payload)

token = jwt.encode(payload,SECREATE_KEY,algorithm=ALGORITHM) 
print("Jwt token : ",token)

print() 

try: 
    token_decode = jwt.decode(token,SECREATE_KEY,algorithms=[ALGORITHM]) 
    print("Decoded token : ",token_decode) 
except JWTError: 
    print("Failed to decode.")
