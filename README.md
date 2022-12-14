# Contact List Backend

Python,Django backend webapi

Tested with Python 3, Django 4 , Django REST framework 3

Runs on : http://localhost:5076/

Can be used with Angular frontend [demo](https://github.com/georgedimac/contacts_webapi_frontend/tree/ver2/)


## API Reference
| **API**                           | **Description**                 
|-----------------------------------|---------------------------------|
| GET /contact/        | Get all contacts            
| GET, POST, PUT, DELETE /contact/{id}           | Get, Add, Update, Delete Contact               | 

| Parameter | Type     | 
| :-------- | :------- | 
| `name` | `string` | 
| `email` | `string` | 
| `phone` | `string` | 

## Installation


```bash
# Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

pip3 install -r requirements.txt
python3 manage.py runserver
```

## Usage

Runs on http://localhost:5076/

<img width="782" alt="Screenshot 2022-09-18 at 13 29 43" src="https://user-images.githubusercontent.com/112869370/190897655-8c3a872c-40a8-48d1-b768-d4bbc5f82343.png">
<img width="788" alt="Screenshot 2022-09-18 at 13 30 01" src="https://user-images.githubusercontent.com/112869370/190897658-d45db9f6-2970-499d-8434-9f0665d78ef1.png">

