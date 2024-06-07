# Social Media Platform using Django

## Features

- User registration and authentication
- User profiles with profile pictures and bio
- Post creation
- Like Posts
- Follow a User
- Unfollow a User
- User search functionality

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- Django (version 3.2 or higher)
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ayushsav/social-media.git
   ```

2. Navigate to the project directory:

   ```bash
   cd social-media
   ```

3. Create a virtual environment (recommended):

   ```bash
   virtualenv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```bash
   pip install pillow
   ```

6. Perform database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account for administrative access:

   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:

   ```bash
   python manage.py runserver
   ```

9. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

- Register a new account or log in with an existing account.
- Customize your profile by adding a profile picture and bio.
- Search for other users.
- Create your own posts.
- Like on posts from friends.
- Follow to a user & see its post on home feed
- Unfollow to a user
- Explore the news feed to see posts from friends.
- Log out when you're done using the platform.
