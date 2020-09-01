# Flask CRUD with JWT Auth

[![Build Status](https://travis-ci.org/adnaanbheda/flask-crud.svg?branch=master)](https://travis-ci.org/adnaanbheda/flask-crud)

Basic Customers REST API created using Flask, SQLAlchemy, Marshmallow

[Postman Collection](https://www.getpostman.com/collections/3b00550bc8398e67ec62)



## TODO

- [x] DB Setup
- [x] Variable Configuration Files
- [x] Customer Routes
- [x] Login/Signup Setup
- [x] JWT Auth
- [X] Travis CI
- [ ] Tests
- [ ] Create Docker Compose File

## Documentation

To run this application, you'll require `pipenv`

1) `pip install pipenv`
2) Clone this repository, `cd flask-crud`
3) `pipenv install`
4) Run the application
    * Development Mode 
    
      - `export FLASK_ENV=development && flask run`
     
    * Production Mode  
    
      - `flask run`
  
  
## API

### Customers Schema
| Field | Type | Description | 
| --- | --- | --- | 
| `name` | `string`| Name | 
| `dob` | `datetime.date` | Date of Birth | 
| `updated_at` | `datetime`| Last Updated Date | 

### Endpoints

| Route | Method | Description | Authentication Required | Body | 
| --- | --- | --- | --- | --- | 
| /login | `POST` | Login endpoint to receive the token | No | `username`, `password`|
| /signup | `POST` | Signup endpoint to receive the token | No | `userame`, `password`|
| /customer | `GET` |  Lists all customers | Yes | - | - |
| /customer | `POST` |  Lists all customers | Yes | `name`, `dob`|
| /customer/\<id\> | `PUT` |  Add a customer | Yes | `name`, `dob` |
| /customer/\<id\> | `GET` |  Fetch a customer | Yes | - |
| /customer/\<id\> | `DELETE` |  Delete a customer | Yes | - |
| /customer/list/\<n\>| `GET`| List all customers sorted by `dob`| Yes | - |
