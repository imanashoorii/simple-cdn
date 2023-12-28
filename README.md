# Django File Manager and CDN Minifier

## Overview

This Django app serves as a versatile file manager with an additional capability to function as a CDN minifier. Users can manage files and, if needed, choose to minify JavaScript (js), HTML, or CSS files by sending a POST request with the "minify" parameter set to "true" or "false."

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/imanashoorii/simple-cdn.git
   cd simple-cdn
   ```
2. Install dependencies using pip and the provided requirements.txt:
    ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
## Usage
### Running the Development Server
Start the development server:
   ```bash
   python manage.py runserver
   ```
Visit http://127.0.0.1:8000/ in your web browser to access the app.

### User Registration and Login
Before using the file manager and CDN minifier features, users need to register and log in with their email and password. Use the provided registration and login forms to create an account or sign in.

### CDN Minifier
To minify files, send a POST request with the "minify" parameter set to "true" or "false" and the file type specified as either "js," "html," or "css."

Example using `curl`:

   ```bash
      curl -X POST -H "Content-Type: application/json" -d '{"file": FILE,"minify": true}' http://127.0.0.1:8000/minify/
   ```
### API Endpoints
* `/file/manager/upload`: Minify files using a POST request as described above.

### Contributing
Feel free to contribute to the project by creating issues or submitting pull requests. Please follow the contribution guidelines.

### Contact
For any inquiries, please contact me at [imanashoorii.77@gmail.com](imanashoorii.77@gmail.com) .

