
import pytest
import httpx
from fastapi.testclient import TestClient
from feedback_platform.app.main import App

def test_InboxCreationEndpoint_With_NotCompleteJson():

    # To be placed into a fixture
    app = App()
    client = TestClient(app.fastapi)

    # Test body
    not_complete_json = {}
    response = client.post("/api/v1/inbox/", headers={"Content-Type": "application/json"}, body=not_complete_json)
    assert response.status_code == 422

