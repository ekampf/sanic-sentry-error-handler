# pylint:disable=too-few-public-methods,import-error

import sys
import raven
from sanic.handlers import ErrorHandler

class SanicSentryErrorHandler(ErrorHandler):

    def __init__(self, dsn):
        super(SanicSentryErrorHandler, self).__init__()
        self.sentry_client = raven.Client(dsn)

    def default(self, request, exception):
        exc_info = sys.exc_info()
        self.sentry_client.captureException(
            exc_info,
            extra=dict(
                url=request.url,
                method=request.method,
                headers=request.headers,
                body=request.body,
                query_string=request.query_string
            )
        )

        return super(SanicSentryErrorHandler, self).default(request, exception)
