# 🚀 Clever Tasker API

_This application is designed to manage tasks efficiently, allowing users to create, view, edit, delete, and schedule tasks. Users can also view their scheduled tasks on a calendar and mark tasks as completed. The backend API is built using Django and Django REST Framework (DRF), providing a robust and maintainable solution._



## Setup Instructions

### 1. **Prerequisites:**
- Install Python from the [official website](https://www.python.org/).
- Install PostgreSQL from the [official website](https://www.postgresql.org/).
- Ensure you have GIT installed for version control.


### 2. **Clone the Repository:**
Open your terminal or command prompt, navigate to your desired directory, and clone the repository:

```bash
git clone https://github.com/Fawaskp/clever-tasker-api.git
```


### 3. **Virtual Environment:**
Create a virtual environment to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```


### 4. **Install Dependencies:**
Use the `requirements.txt` file to install all necessary packages:

```bash
pip install -r requirements.txt
```


### 5. **Environment Variables:**
Set up a `.env` file using the provided `.env.example` file to configure environment variables.


### 6. **PostgreSQL Configuration:**
- Create a PostgreSQL database for the project.
- Configure the database connection in the `.env` file based on the [`.env.example`](.env.example).
- Ensure the PostGIS extension is enabled to handle geospatial data if needed.


### 7. **Migrations:**
Apply the migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. **Run the Development Server:**
Start the local server to test the application:

```bash
python manage.py runserver
```



### [Frontend Repository](https://github.com/Fawaskp/map-my-crop-task-client)

Explore the Clever Tasker client-side application built for seamless integration with this API.