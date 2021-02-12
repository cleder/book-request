"""Test the API with schemathesis."""
from hypothesis import strategies as st
from schemathesis.loaders import from_asgi
from email_validator import validate_email, EmailNotValidError

from app.main import app
from app.persistors import books

schema = from_asgi("/openapi.json", app)


@schema.parametrize()
def test_api(case):
    response = case.call_asgi()
    case.validate_response(response)

@schema.parametrize(endpoint="/request/", method="POST")
@schema.given(data=st.data())
def test_request_add_valid(data, case):
    """Always return a 201 response when the book is in db and a valid email."""
    case.body["email"] = data.draw(st.emails())
    case.body["title"] = data.draw(st.sampled_from(list(books.values())))
    response = case.call_asgi(app=app)
    try:
        validate_email(case.body['email'], check_deliverability=False)
        assert response.status_code == 201
    except EmailNotValidError:
        # not all emails generated by hypothesis pass pydantic validation.
        assert response.status_code == 422
