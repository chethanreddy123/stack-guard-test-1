import os

# Hardcoded creds for test (do not use in production)
HARDCODED_PASSWORD = "P@ssw0rd!"
HARDCODED_TOKEN = "bearer abcdefghijklmnopqrstuvwx1234567890abcd"
HARDCODED_BASIC_AUTH = "Basic YWxhZGRpbjpvcGVuc2VzYW1l"

GOOGLE_SERVICE_ACCOUNT_JSON = {
  "type": "service_account",
  "project_id": "stack-guard-fixture",
  "private_key_id": "abcd1234efgh5678ijklmnopqrstuvwx12345678",
  "private_key": "-----BEGIN PRIVATE KEY-----\nabcdefghijklmnopqrstuvwx1234567890abcd\n-----END PRIVATE KEY-----\n",
  "client_email": "fixture@stack-guard.iam.gserviceaccount.com",
  "client_id": "111111111111111111111",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/fixture%40stack-guard.iam.gserviceaccount.com"
}

def connect():
    dsn = "postgresql://admin:DummyPassword123@localhost:5432/app"
    return dsn

if __name__ == "__main__":
    print("Fixture running")
