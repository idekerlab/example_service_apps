DROP TABLE IF EXISTS posts;

CREATE TABLE task (
    id TEXT PRIMARY KEY AUTOINCREMENT,
    status TEXT NOT NULL,
    result TEXT NOT NULL
);