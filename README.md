Automotive Maintenance API Backend
This is the backend for the Automotive Maintenance application built with Django. It provides an API for managing user authentication, starting and viewing conversations, and other related features.

Features
User Registration (/api/v1/signup/)
User Sign In (/api/v1/signin/)
Start a Conversation (/api/v1/conversation/)
View Conversations (/api/v1/conversations/)
View Specific Conversation (/api/v1/conversations/{id}/)
Requirements
Python 3.13.2
Django 5.2.3
djangorestframework
djangorestframework-simplejwt
Setup Instructions
1. Clone the repository
git clone https://github.com/yourusername/automotive_maintenance.git
cd automotive_maintenance

2. Create a virtual environment (optional but recommended)
python -m venv venv
3. Activate the virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Apply migrations
python manage.py migrate
6. Start the development server
python manage.py runserver

You can now access the API at http://127.0.0.1:8000/
.

API Endpoints
POST /api/v1/signup/

Registers a new user with a username and password.

Request Body:

{
  "username": "john_doe",
  "password": "password123"
}

Response:

{
  "username": "john_doe"
}
POST /api/v1/signin/

Signs in an existing user and returns an access token and refresh token.

Request Body:

{
  "username": "john_doe",
  "password": "password123"
}

Response:

{
  "access": "your-access-token-here",
  "refresh": "your-refresh-token-here"
}
POST /api/v1/conversation/

Starts a new conversation.

Request Body:

{
  "user": "john_doe",
  "message": "Hello, I need some maintenance help."
}

Response:

{
  "id": 1,
  "user": "john_doe",
  "message": "Hello, I need some maintenance help.",
  "created_at": "2026-03-05T12:34:56Z"
}
GET /api/v1/conversations/

Retrieves a list of all conversations.

Response:

[
  {
    "id": 1,
    "user": "john_doe",
    "message": "Hello, I need some maintenance help.",
    "created_at": "2026-03-05T12:34:56Z"
  }
]
GET /api/v1/conversations/{id}/

Retrieves details of a specific conversation by id.

Response:

{
  "id": 1,
  "user": "john_doe",
  "message": "Hello, I need some maintenance help.",
  "created_at": "2026-03-05T12:34:56Z"
}
Development
Running Tests

If you want to run the tests for this project, you can do so with the following command:

python manage.py test
Static Files

To serve static files in development, ensure you have the following setting in your settings.py:

STATIC_URL = '/static/'

You can collect static files for production with:

python manage.py collectstatic
License

This project is licensed under the MIT License - see the LICENSE
 file for details.


---

### Explanation of the Sections

- **Project Description**: Explains the project and its features.
- **Requirements**: Lists the requirements (like Python, Django, etc.).
- **Setup Instructions**: Provides a step-by-step guide for setting up and running the project locally.
- **API Endpoints**: A description of the main API endpoints with sample requests and responses.
- **Development**: Explains how to run tests and manage static files for production.
- **License**: Mentions the project license (you can choose one like MIT, GPL, etc.).

---

Feel free to customize the README based on your actual project structure. Let me know if you need any more details or changes!
