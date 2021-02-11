"""Test the API with schemathesis."""
from schemathesis.loaders import from_asgi

from app.main import app

schema = from_asgi("/openapi.json", app)


@schema.parametrize()
def test_api(case):
    response = case.call_asgi()
    case.validate_response(response)
