from flask import render_template, session, redirect, url_for
from app.main import bp
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@login_required
def index():
    user = session.get('user')
    return render_template('main/index.html', user=user) 