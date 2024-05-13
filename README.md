# ChatFlask

This is a simple chat application built with Flask, SQLAlchemy, and SQLite.

## Project Structure

The project structure is organized into separate files for better modularity and readability:

- `app.py`: Initializes the Flask app and sets up the database.
- `models.py`: Defines the database models (Chat and Message).
- `routes.py`: Contains the route definitions and handlers.
- `chat_app.db`: SQLite database file (generated after running the app).

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Pikuz1/chat-flask.git 
   cd chat-flask
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the application:
   Open your web browser and go to `http://localhost:5000`

## API Endpoints

- `GET /chats`: Get all chats.
- `GET /chats/<chat_id>/messages`: Get all messages of a specific chat or send a new message.
- `POST /chats`: Create new chats.
- `POST /chats/<chat_id>/messages`: Send messages to specific id.

## Usage

- Use Postman or any API testing tool to interact with the API endpoints.
- Create chats using `POST /chats` and send messages using `POST /chats/<chat_id>/messages`.
- Retrieve chats and messages using `GET` requests to the respective endpoints.

## Database

The application uses SQLite as the database. The database file (`chat_app.db`) is created automatically when the application is run.

## Dependencies

- Flask
- Flask-SQLAlchemy
