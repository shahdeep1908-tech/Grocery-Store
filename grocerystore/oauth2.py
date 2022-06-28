from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from grocerystore import token

# Following file checks which path requires token Bearer to be generated and throws error code
# for eah not authenticated User.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    """
    This function provides email-id to function who has access to routes after successful Login.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid ACCESS TOKEN. Please Check and come back!!!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    email_token = token.verify_token(data, credentials_exception)
    return email_token


def get_current_user_access_token(data: str = Depends(oauth2_scheme)):
    """
    This function provides email-id to function who has access to routes after successful Login.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid ACCESS TOKEN. Please Check and come back!!!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    email_token = token.verify_refresh_token(data, credentials_exception)
    return email_token
