INSERT INTO role(id, created_at, edited_at, name)
VALUES (1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Admin')
ON CONFLICT(id) DO NOTHING;

INSERT INTO role(id, created_at, edited_at, name)
VALUES (2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Default')
ON CONFLICT(id) DO NOTHING;

INSERT INTO role(id, created_at, edited_at, name)
VALUES (3, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Operator')
ON CONFLICT(id) DO NOTHING;

INSERT INTO role(id, created_at, edited_at, name)
VALUES (4, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 'Employer')
ON CONFLICT(id) DO NOTHING;
