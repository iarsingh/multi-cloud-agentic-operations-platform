from fastapi.testclient import TestClient
from mcagent.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'plan gcp network', **{'payload': {'cloud': 'gcp'}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["cloud"] == "gcp"
    refused = client.post("/agent/run", json={"goal": 'apply in aws'}).json()
    assert refused["refused"] is True
