# Flask_applcation
This is a Flask application that provides a REST API for performing CRUD operations on a User resource. The User data is stored in a MongoDB database.

## Requirements

- Python 3.x
- Flask
- PyMongo

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Binita72/Flask_applcation.git
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask application:

   ```bash
   python app.py
   ```

   The application will run at `http://localhost:90`.

## API Endpoints

The following REST API endpoints are available:

- `GET /users`: Returns a list of all users.
- `GET /users/<id>`: Returns the user with the specified ID.
- `POST /users`: Creates a new user.
- `PUT /users/<id>`: Updates the user with the specified ID.
- `DELETE /users/<id>`: Deletes the user with the specified ID.

## Usage

You can use an HTTP client like cURL or Postman to interact with the API endpoints. For example:

- Retrieve all users:

  ```bash
  curl http://localhost:90/users
  ```

- Retrieve a specific user:

  ```bash
  curl http://localhost:90/users/<id>
  ```

- Create a new user:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "password": "secret"}' http://localhost:90/users
  ```

- Update a user:

  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated Name", "email": "updated@example.com", "password": "newpassword"}' http://localhost:90/users/<id>
  ```

- Delete a user:

  ```bash
  curl -X DELETE http://localhost:90/users/<id>
  ```

Make sure to replace `<id>` with the actual ID of the user you want to interact with.



Feel free to modify and adapt this project to suit your needs.

---
