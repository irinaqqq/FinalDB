# Project Setup and Installation Guide

## Prerequisites

Before starting, make sure you have the following installed on your system:

- Python (version 3.7 or higher)
- pip (Python package manager)
- MongoDB (version 4.0 or higher)
- Git

## Step 1: Clone the Repository

Clone the project from GitHub using the following command:

```bash
git clone https://github.com/irinaqqq/FinalDB.git
```

Once cloned, navigate to the project directory:

```bash
cd FinalDB-main
```

## Step 2: Set Up a Virtual Environment

It’s recommended to create a virtual environment to keep the dependencies isolated. Run the following commands:

```bash
python -m venv venv
.\venv\Scripts\activate
```

## Step 3: Install the Required Packages

Use the `requirements.txt` file to install all necessary packages:

```bash
pip install -r requirements.txt
```

This will install Django, Djongo (for MongoDB integration), and any other dependencies listed in the file.

## Step 4: Configure MongoDB

1. Make sure MongoDB is running on your system. You can start it with:
   ```bash
   mongod
   ```
   
2. Open the Django project’s settings file (typically `settings.py`) and configure the MongoDB database settings if they aren't set yet. The configuration should look like this:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'djongo',
           'NAME': '<database_name>',
           'HOST': 'localhost',
           'PORT': 27017,
       }
   }
   ```

   Replace `<database_name>` with the name of the MongoDB database you want to use.

## Step 5: Apply Migrations

Since you’re using MongoDB with Djongo, Django migrations might be handled differently depending on your project setup. Generally, you can try running:

```bash
python manage.py migrate
```

This will apply any pending migrations to the database.

## Step 6: Run the Django Development Server

Finally, to start the Django development server, use:

```bash
python manage.py runserver
```

This will start the server at `http://127.0.0.1:8000/`. You can now access your project in a web browser by visiting that address.
