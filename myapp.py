"""
This script runs the BinaryDecimal application using a development server.
"""

from os import environ
from BinaryDecimal import app

application = app
if __name__ == '__main__':
    app.run()
    
