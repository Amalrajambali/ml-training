from fastapi.testclient import TestClient
import test_iris_fast as app_module

client = TestClient(app_module.app)
sample = [5.9, 4.5, 2.4, 0.8]
resp = client.post('/predict', json={'data': sample})
print('Status code:', resp.status_code)
print('Response JSON:', resp.json())