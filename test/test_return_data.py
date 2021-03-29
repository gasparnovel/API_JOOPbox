from flask import Request, jsonify
import pytest
from resources.data import Data
import json


@pytest.mark.return_data
def test_return_data(client):
    rv = client.get('/')
    assert Data.datos == rv.get_json()