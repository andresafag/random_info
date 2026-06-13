import json
import pytest
from application import application


@pytest.fixture
def client():
    application.config["TESTING"] = True
    with application.test_client() as c:
        yield c


def test_index(client):
    r = client.get("/")
    assert r.status_code == 200


def test_valid_selection(client):
    r = client.get("/allow/name")
    assert r.status_code == 200


def test_invalid_selection(client):
    r = client.get("/allow/invalid")
    assert r.status_code == 200
    assert b"Wrong selection" in r.data


def test_results(client):
    r = client.get("/allow/name/3/en_US")
    assert r.status_code == 200


def test_results_between(client):
    r = client.get("/allow/date/3/2020-01-01/2021-01-01/")
    assert r.status_code == 200


def test_download(client):
    r = client.post(
        "/download/",
        data=json.dumps(["Alice", "Bob"]),
        content_type="application/json",
    )
    assert r.status_code == 200
    assert r.content_type == "text/csv; charset=utf-8"


def test_download_invalid(client):
    r = client.post("/download/", data="not-json", content_type="text/plain")
    assert r.status_code == 400
