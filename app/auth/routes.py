from flask import render_template, request, session, redirect, url_for, jsonify, current_app
import requests
from app.auth import bp

@bp.route('/login')
def login():
    return render_template('auth/login.html')

@bp.route('/validate', methods=['POST'])
def validate_token():
    data = request.get_json()
    
    if not data or 'token' not in data:
        return jsonify({'error': 'Brak tokenu'}), 400
    
    token = data['token']
    
    # Walidacja tokenu przez zewnętrzny serwis
    response = requests.get(
        current_app.config['SSO_VALIDATION_URL'],
        headers={'Authorization': f'Bearer {token}'}
    )
    
    if response.status_code != 200:
        return jsonify({'error': 'Nieprawidłowy token'}), 401
    
    user_data = response.json()
    
    # Zapisanie danych użytkownika w sesji
    session['user'] = user_data
    
    return jsonify({'success': True})

@bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('auth.login')) 