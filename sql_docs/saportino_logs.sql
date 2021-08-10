DROP TABLE IF EXISTS log_request;

CREATE TABLE log_request(
    id SERIAL NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT current_timestamp,
    method TEXT NOT NULL,
    url TEXT NOT NULL,
    status_code SMALLINT NOT NULL,
    process_time SMALLINT NOT NULL,
    ip TEXT,
    headers TEXT,
    body TEXT,
    query_params TEXT,
    error_msg TEXT
);