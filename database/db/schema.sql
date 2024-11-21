
\c pos_attenzio


CREATE TABLE rol(
    rol_id INT PRIMARY KEY,
    rol_name VARCHAR(100)
);
CREATE TABLE customuser (
        custom_user_id SERIAL PRIMARY KEY,
        full_name VARCHAR(100) NOT NULL,
        document VARCHAR(20) NOT NULL UNIQUE,
        address VARCHAR(100),
        picture VARCHAR(200),
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(128) NOT NULL,
        rol_id INT REFERENCES rol(rol_id),
        last_login TIMESTAMPTZ,
        is_superuser BOOLEAN DEFAULT FALSE,
        is_staff BOOLEAN DEFAULT FALSE,
        is_active BOOLEAN DEFAULT TRUE,
        date_joined TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE session(
    session_id SERIAL PRIMARY KEY,
    session_name VARCHAR(300),
    session_date_start TIME,
    session_date_end TIME,
    session_description VARCHAR(300),
    custom_user_id INT,
    FOREIGN KEY (custom_user_id) REFERENCES customUser(custom_user_id)
);

CREATE TABLE userSession(
    custom_user_id INT NOT NULL,
    session_id INT NOT NULL,
    PRIMARY KEY(custom_user_id, session_id),
    FOREIGN KEY (custom_user_id) REFERENCES customUser(custom_user_id),
    FOREIGN KEY (session_id) REFERENCES session(session_id)
);

CREATE TABLE question(
    question_id SERIAL PRIMARY KEY,
    question_text VARCHAR(400),
    session_id INT NOT NULL,
    FOREIGN KEY (session_id) REFERENCES session(session_id)
);

CREATE TABLE option(
    option_id SERIAL PRIMARY KEY,
    option_text VARCHAR(200),
    is_correct BOOLEAN,
    question_id INT,
    FOREIGN KEY (question_id) REFERENCES question(question_id)
);