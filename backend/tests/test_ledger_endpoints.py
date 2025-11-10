from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_list_ledger_entries():
  response = client.get('/api/ledger/entries')
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, list)
  assert data[0]['id'] == 'ledger-001'
