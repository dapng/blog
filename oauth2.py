import JWTtoken
import schemas

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, oauth2

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



# def get_current_user(token: str = Depends(oauth2_scheme)) -> schemas.UserWithId:
#     return JWTtoken.verify_token(token)


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return JWTtoken.verify_token(token, credentials_exception)

# def get_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     return JWTtoken.verify_token(token, credentials_exception)
