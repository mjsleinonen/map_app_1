import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from application import create_app

import webbrowser as wb

app = create_app()

if __name__ == '__main__':
    local_url = "http://127.0.0.1:5000"
    wb.open(local_url)
    app.run(debug=True)
