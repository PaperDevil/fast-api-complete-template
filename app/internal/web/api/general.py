from fastapi import APIRouter

from app.external.entities.exception_response import ExceptionResponse
from app.internal.web.api.user import user_router

general_router = APIRouter(prefix='/v1', responses={400: {'model': ExceptionResponse},
                                                    500: {'model': ExceptionResponse}})

general_router.include_router(user_router)
