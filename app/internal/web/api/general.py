from fastapi import APIRouter

from app.external.entities.exception_response import ExceptionResponse
from app.internal.web.api.organisation import organisation_router
from app.internal.web.api.pretension import pretension_router
from app.internal.web.api.ticket import ticket_router
from app.internal.web.api.user import user_router

general_router = APIRouter(prefix='/v1', responses={400: {'model': ExceptionResponse},
                                                    500: {'model': ExceptionResponse}})


general_router.include_router(user_router)
general_router.include_router(pretension_router)
general_router.include_router(ticket_router)
general_router.include_router(organisation_router)
