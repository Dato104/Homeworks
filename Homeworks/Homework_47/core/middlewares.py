from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, Response
import uuid



class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next)-> Response:

        correlation_id = str(uuid.uuid4())

        request.state["X-Correlation-ID"] = correlation_id

        response = await call_next(request)

        response.headers["X-Correlation-ID"] = correlation_id

        return response


