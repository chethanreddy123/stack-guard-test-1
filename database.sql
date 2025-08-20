-- Fixture with credentials
INSERT INTO users(email, password) VALUES
('alice@example.com', 'aliceDummyPass123'),
('bob@example.com', 'bobDummyPass123'),
('service@stackguard.io', 'svc_dummySecret123');

-- Example DSNs
-- mysql://user:pass@host:3306/db
-- redis://:password@localhost:6379/0

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
