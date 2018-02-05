sanic-sentry-error-handler
==========================
|Travis| |PyPI|

Sentry error handler for Sanic web server

Requirements
------------

- python >= 3.5

Installation
------------

**sanic-sentry-error-handler** should be installed using pip: ::

    pip install sanic-sentry-error-handlert


Usage
-----
**SENTRY_DSN**  - Sentry DSN for your application

To begin we'll set up a Sanic app:

.. code:: python

    >>> from sanic import Sanic
    >>> from sanic_sentry import SanicSentryErrorHandler
    >>> app = Sanic(__name__)
    >>> app.error_handler = SanicSentryErrorHandler('http://public:secret@example.com/1')

If your application uses the `Sanic exception handling views`_ you might consider using decorator for intercepting the exceptions.

.. code:: python

    >>> from sanic import response, Sanic
    >>> from sanic_sentry import SanicSentryErrorHandler
    >>>
    >>> sentry_client = SanicSentryErrorHandler('http://public:secret@example.com/1')
    >>> app = Sanic(__name__)
    >>>
    >>>
    >>> @app.exception([Exception, ])
    >>> @sentry_client.intercept_exception
    >>> def handle_exception_500(request, exception):
    >>>     return response.json({"description": "Internal Server Error"}, status=500)


.. |Travis| image:: https://travis-ci.org/ekampf/sanic-sentry-error-handler.svg?branch=master
.. |PyPI| image:: https://badge.fury.io/py/sanic-sentry-error-handler.svg
    :target: https://badge.fury.io/py/sanic-sentry-error-handler
.. _Sanic exception handling views: https://sanic.readthedocs.io/en/latest/sanic/exceptions.html#handling-exceptions

