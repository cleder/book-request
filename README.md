# book-request

A small app to evaluate FastApi

I chose FastAPI over Flask because I wanted to try FastApi and testing with schemathesis.

## Installation
Create a virtualenvironment with python 3.8 or 3.9.
Install the reequirements with `pip install -r requirements.txt`.
Run the application with `uvicorn app:app` and goto `http://localhost:8000/docs`

## Add Request Endpoint
This allows a user to request a particular book, and returns the request object along with an id
by which it can be referred to. Ensure email is of a valid format, and that title exists in our
list of titles in the database. This is currently a fixed dictionary.

`/request [POST]`

- email {string} the email address of the requesting user
- title {string} the title of the requested book

Returns a JSON response with the following:
- email {string} the email address of the requesting user
- title {string} the title of the requested book
- id {string} an id which the newly created user can be referred to by
- timestamp {string} a timestamp set to the date and time that the user made the initial request.

## Retrieve Request(s) Endpoint
This allows a user to retrieve an existing request by using an id, or a list of all existing requests
if id is omitted.

`/request/{id} [GET]`

Returns a JSON response with values depending on whether id was provided. If it was, there
should only be one value, and it should match return value of the POST endpoint above. If there
is no id given, it should be a list of all requests, each being in the same format as a single one
would be.

## Delete Request Endpoint
This allows a user to remove an existing request.

`/request/{id} [DELETE]`

Returns no body.
