sanic-sentry-error-handler
==========================
.. image:: https://travis-ci.org/ekampf/sanic-sentry-error-handler.svg?branch=master


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
