# Flask SSO Application

A simple Flask application implementing Single Sign-On (SSO) authentication with protected routes and session management.

## Features

- Single Sign-On (SSO) authentication
- Protected routes requiring authentication
- Server-side session management
- Responsive design
- Token-based authentication
- External token validation

## Project Structure

flask_sso_app/
├── app/
│ ├── init.py
│ ├── auth/
│ │ ├── init.py
│ │ ├── routes.py
│ │ └── sso.py
│ ├── main/
│ │ ├── init.py
│ │ └── routes.py
│ ├── static/
│ │ ├── css/
│ │ │ └── style.css
│ │ └── js/
│ │ └── sso.js
│ └── templates/
│ ├── auth/
│ │ └── login.html
│ ├── base.html
│ └── main/
│ └── index.html
├── config.py
├── requirements.txt
└── run.py

````

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Modern web browser with JavaScript enabled

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd flask-sso-app
````

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Set up environment variables (optional):

```bash
export SECRET_KEY="your-secret-key"
export FLASK_ENV="development"
```

## Configuration

The application can be configured by modifying `config.py`:

```python
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SSO_VALIDATION_URL = 'https://example.com/validate_token'
```

Key configuration options:

- `SECRET_KEY`: Used for session security
- `SSO_VALIDATION_URL`: External endpoint for token validation

## Running the Application

1. Start the development server:

```bash
python run.py
```

2. Access the application at: `http://localhost:5000`

## Authentication Flow

1. User attempts to access protected route
2. If not authenticated, redirected to login page
3. User clicks SSO login button
4. SSO popup window opens
5. After successful external authentication:
   - Token is received via postMessage
   - Token is validated with external service
   - User session is created
   - User is redirected to protected route

## API Endpoints

### Authentication Routes (`/auth`)

- `GET /auth/login`

  - Displays the login page
  - No authentication required

- `POST /auth/validate`

  - Validates SSO token
  - Requires JSON body with token
  - Returns user session data

- `GET /auth/logout`
  - Terminates user session
  - Redirects to login page

### Main Routes (`/`)

- `GET /`
  - Home page
  - Requires authentication
  - Displays user information

## Frontend Components

### JavaScript SSO Class

The `SSO` class in `static/js/sso.js` handles:

- Opening SSO popup window
- Processing postMessage communication
- Token validation
- Redirect after successful authentication

Usage:

```javascript
const sso = new SSO({
  loginUrl: "https://example.com/sso/login",
  validateEndpoint: "/auth/validate",
  redirectUrl: "/",
  width: 600,
  height: 700,
});
```

### Templates

- `base.html`: Base template with navigation and layout
- `login.html`: SSO login interface
- `index.html`: Protected home page showing user data

## Error Handling

The application includes error handling for:

- Invalid tokens
- Failed authentication
- Missing tokens
- Network errors
- Popup blocking

## Troubleshooting

Common issues and solutions:

1. Popup Blocked

   - Enable popups for the application domain
   - Check browser security settings

2. Session Issues

   - Clear browser cookies
   - Verify SECRET_KEY is set
   - Check session configuration

3. Token Validation Fails
   - Verify SSO_VALIDATION_URL is correct
   - Check network connectivity
   - Validate token format
