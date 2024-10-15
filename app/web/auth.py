"""
Auth Module
"""
from typing import Annotated

import jwt
from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from jwt import PyJWKClient

from app.config import AuthConfig as auth
from app.models.user import LoggedInUser

oauth_2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl = f"{auth.url}/protocol/openid-connect/token",
    authorizationUrl = f"{auth.url}/protocol/openid-connect/auth",
    refreshUrl = f"{auth.url}/protocol/openid-connect/token",
)

async def valid_access_token(access_token: Annotated[str, Depends(oauth_2_scheme)]):
    """
    Method to validated access token
    """
    url = f"{auth.url}/protocol/openid-connect/certs"
    optional_custom_headers = {"User-agent": "custom-user-agent"}
    jwks_client = PyJWKClient(url, headers=optional_custom_headers)

    try:
        signing_key = jwks_client.get_signing_key_from_jwt(access_token)
        data = jwt.decode(
            access_token,
            signing_key.key,
            algorithms = ["RS256"],
            audience = "account",
            options = {"verify_exp": True},
        )
        return data
    except jwt.exceptions.InvalidTokenError as ex:
        print(ex)
        raise HTTPException(status_code=401, detail="Not authenticated")

async def get_user_info(payload: dict = Depends(valid_access_token)) -> LoggedInUser:
    """
    Method to get loggedIn user info
    """
    try:
        return LoggedInUser(
            id=payload.get("sub"),
            username=payload.get("preferred_username"),
            email=payload.get("email"),
            first_name=payload.get("given_name"),
            last_name=payload.get("family_name"),
            realm_roles=payload.get("realm_access", {}).get("roles", []),
            client_roles=payload.get("realm_access", {}).get("roles", [])
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e), # "Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
