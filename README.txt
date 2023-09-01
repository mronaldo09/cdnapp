CDN Application with Kong
This application is an example of a Content Delivery Network (CDN) application that uses Kong as an API gateway to manage API requests and responses.

Prerequisites
Docker: Make sure you have Docker installed on your system.
Flask: Ensure you have Flask installed on your system. You can install it by running pip install Flask.
mysql-connector-python: Make sure you have MySQL Connector Python installed on your system. You can install it by running pip install mysql-connector-python.
Running the Application
1. Setting Up the Database
Create a MySQL database and import the database schema available in the database folder.

2. Running the Flask Application
- Open a terminal or command prompt.

- Navigate to your Flask application directory.

- Build a Docker image for the Flask application by running the following command:
docker build -t flask-app .

- After successfully building the image, run a Docker container for the Flask application with the following command:
docker run -d --name flask-container -p 5000:5000 flask-app
Your Flask application will run at http://127.0.0.1:5000/.

3. Running Kong
Ensure that Kong is installed on your system.

Create a Kong configuration file (e.g., kong.yml) with the appropriate configuration for your application.

Run Kong with the following command, replacing /path/to/your/kong.yml with the absolute path to your Kong configuration file:
kong start -c /path/to/your/kong.yml

Verify if Kong is running smoothly by running the command:
kong health

4. Accessing the Application through Kong
Your CDN application can be accessed through Kong using the URL configured according to your settings. For example:

CDN API Endpoint: http://localhost:8000/items_data
Ensure that you have configured your frontend to send requests to Kong with the correct URL.

5. Running the Flask Application Manually (Optional)
If you want to run the Flask application manually without using Docker, follow these steps:

Navigate to your Flask application directory.

Run the Flask application with the following command:
python app.py
The Flask application will run at http://127.0.0.1:5000/.

License
This application was created by Ronaldo for assessment purposes at Asians Group LLC.