"""
This script runs the BinaryDecimal application using a development server.
"""

from os import environ
from BinaryDecimal import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        #Run in Cpanel
        app.run()
    app.run(HOST, PORT)
