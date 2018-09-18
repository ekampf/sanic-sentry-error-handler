# pylint:disable=too-few-public-methods,import-error,line-too-long

import sys
from functools import wraps

import raven
from raven_aiohttp import AioHttpTransport
from sanic.handlers import ErrorHandler
from sanic import exceptions as sanic_exceptions


class SanicSentryErrorHandler(ErrorHandler):
    DEFAULT_EXCEPTIONS_TO_IGNORE = (sanic_exceptions.NotFound,)

    def __init__(self, dsn, exceptions_to_ignore=None, **sentry_kwargs):
        super(SanicSentryErrorHandler, self).__init__()
        self.exceptions_to_ignore = tuple(exceptions_to_ignore) if exceptions_to_ignore is not None else self.DEFAULT_EXCEPTIONS_TO_IGNORE
        # For sentry_kwargs see
        # https://docs.sentry.io/clients/python/advanced/#client-arguments
        self.sentry_client = raven.Client(dsn, transport=AioHttpTransport, **sentry_kwargs)

    def default(self, request, exception):
        if not isinstance(exception, self.exceptions_to_ignore):
            exc_info = (type(exception), exception, exception.__traceback__)

            extra = dict()
            if request is not None:
                extra = dict(
                    url=request.url,
                    method=request.method,
                    headers=request.headers,
                    body=request.body,
                    query_string=request.query_string
                )

            self.sentry_client.captureException(exc_info, extra=extra)

        return super(SanicSentryErrorHandler, self).default(request, exception)

    def intercept_exception(self, function):
        """
        Decorator for Sanic exception views.
        You should use this decorator only if your exception handler returns its own response.
        If you're handler returns `None` the default exception handler will be called which
        means Sentry will be called twice.

        Example:
            >> @app.exception([Exception, ])
            >> @sentry_client.intercept_exception
            >> def handle_exception(request, exception):
            >>     pass
        """

        @wraps(function)
        def wrapped_view_function(request, exception):
            self.default(request, exception)
            return function(request, exception)

        return wrapped_view_function
