from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse
import uvicorn

from submissions.fastapi_oidc_auth.auth import OpenIDConnect

host = "https://auth.cuahsi.io"
realm = "HydroShare"
client_id = "local_iguide_api"
client_secret = "AyPQBiRP1FAJ7bU8rIUopgtFExc6ySkR"
app_uri = "https://localhost/api/"
redirect_uri = "https://localhost/api/"

#host = "http://keycloak:8080/auth"
#realm = "master"
#client_id = "test-client"
#client_secret = "jC8NwfW8KHMv0ww0WEFvpYSv9R5ddjAD"
#app_uri = "https://localhost/api/"
#redirect_uri = "https://localhost/api"


oidc = OpenIDConnect(host, realm, app_uri, client_id, client_secret, redirect_uri)
router = APIRouter()


@router.get("/")
async def homepage(request: Request) -> dict[str, str]:
    return {"message": "Not a secret"}


@router.get("/secret")
@oidc.require_login
async def secret(request: Request) -> dict[str, str]:
    return {"message": "Secret"}


@router.get("/login")
@oidc.require_login
async def login(request: Request) -> dict[str, str]:
    return {"message": "success"}


@router.get("/logout")
async def logout(request: Request) -> RedirectResponse:
    return oidc.logout(request=request)