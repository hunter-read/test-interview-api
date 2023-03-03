CREATE TABLE gms (
    id TEXT NOT NULL PRIMARY KEY,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    image TEXT,
    lastname TEXT,
    modified DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT,
    pronouns TEXT,
    username TEXT,
    lookup_count INTEGER NOT NULL DEFAULT 0,
    description TEXT,
    years_of_professional_gm_experience INTEGER,
    years_of_ttrpg_experience INTEGER,
    next_session_start_time DATETIME,
    number_reviews INTEGER NOT NULL DEFAULT 0
);