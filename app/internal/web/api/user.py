from fastapi import APIRouter, Depends

from app.internal.logic.deserializers.user import UserDeserializer
from app.internal.logic.entities.db.user import User
from app.internal.logic.entities.request.user.add import UserAddRequest
from app.internal.logic.entities.request.user.update import UserUpdateRequest
from app.internal.logic.entities.response.just_bool import JustBoolResponse
from app.internal.logic.entities.response.token import TokensResponse
from app.internal.logic.entities.response.user.detail import UserDetailResponse
from app.internal.logic.services.user import UserService
from app.internal.web.depends.auth import MyOAuth2PasswordRequestForm
from app.internal.web.depends.user import get_current_user_from_refresh_token, get_current_user

user_router = APIRouter(prefix='/users', tags=['Users API'])


@user_router.post('/register', response_model=JustBoolResponse)
async def register(user_add_request: UserAddRequest):
    await UserService.register(user_add_request.to_user())
    return JustBoolResponse(result=True)


@user_router.post('/auth/base', response_model=TokensResponse)
async def auth_base(form_data: MyOAuth2PasswordRequestForm = Depends()):
    user: User = UserDeserializer.get_from_form_data(form_data)
    user = await UserService.auth_user_base(user)
    return user.to_tokens()

@user_router.get('/refresh_token', response_model=TokensResponse)
def refresh_token(user: User = Depends(get_current_user_from_refresh_token)):
    user.create_auth_token()
    return user.to_tokens()


@user_router.get('/me', response_model=UserDetailResponse)
def get_my_simple(user: User = Depends(get_current_user)):
    return user.to_user_detail_response()


@user_router.patch('/me', response_model=UserDetailResponse)
async def update_my_data(user_update_request: UserUpdateRequest,
                         user: User = Depends(get_current_user)):
    user = await UserService.update(user.id, user_update_request.to_user())
    return user.to_user_detail_response()
