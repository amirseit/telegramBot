CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,                    -- Auto-incrementing primary key
    chat_id BIGINT NOT NULL UNIQUE,           -- Unique chat ID for each user
    username TEXT,                            -- Username of the user
    registered_at TIMESTAMP DEFAULT NOW()     -- Timestamp when the user registered
);
