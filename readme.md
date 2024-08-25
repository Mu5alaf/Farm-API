# Farm Management System API

This project is a Farm  API built with Django and Django Rest Framework. It provides a comprehensive solution for managing farms, crops, and animals with user authentication.

## Features

- User Authentication (JWT-based)
- Farm
- Crop
- Animal
- RESTful API endpoints for all operations

## Technologies Used

- Python
- Django
- Django Rest Framework
- djangorestframework-simplejwt

## Project Setup

### Prerequisites

- Python 3.12.5
- pip

### Installation

1. Clone the repository:
2. Create a virtual environment:.env\Scripts\activate
3. Install dependencies: pip install - r requirements.txt

## API Endpoints

- User Authentication:
- Register: `http://127.0.0.1:8000/api/auth/register/`
- Login: `http://127.0.0.1:8000/api/auth/login/`
- Profile: `http://127.0.0.1:8000/api/auth/profile/`
- Edit Profile: `http://127.0.0.1:8000/api/auth/profile/`
- Refresh Token: `http://127.0.0.1:8000/api/auth/refresh/`
- add Farm: `http://127.0.0.1:8000/api/farm/farms/`
- add Crops: `http://127.0.0.1:8000/api/farm/crops/`
- add Animals: `http://127.0.0.1:8000/api/farm/animals/`

## Permissions

- Only authenticated users can access the API endpoints.
- Users can only manage (create, update, delete) their own farms, crops, and  animals.

## Demo
https://github.com/user-attachments/assets/70d08870-7d73-46d1-9bb5-0cc759a34741




