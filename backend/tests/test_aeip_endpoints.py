from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_list_receipts():
  response = client.get('/api/aeip/receipts')
  assert response.status_code == 200
  data = response.json()
  assert isinstance(data, list)
  assert any(item['status'] == 'complete' for item in data)
