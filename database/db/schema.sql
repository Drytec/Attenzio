
\c pos_attenzio

CREATE TABLE student(
    est_id SERIAL PRIMARY KEY,
    full_name VARCHAR(60) NOT NULL ,
    email VARCHAR(100) UNIQUE NOT NULL,
    est_phone VARCHAR(10),
    password VARCHAR(30),
    est_tab VARCHAR(300)
);

CREATE TABLE teacher(
    teacher_id SERIAL PRIMARY KEY,
    teacher_document INTEGER UNIQUE NOT NULL,
    full_name VARCHAR(60) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    teacher_address VARCHAR(300),
    teacher_picture VARCHAR(200),
    password VARCHAR(300)
);

CREATE TABLE session(
    session_id SERIAL PRIMARY KEY,
    session_name VARCHAR(300),
    session_date_start TIME,
    session_date_end TIME,
    session_description VARCHAR(300),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);

CREATE TABLE studentSession(
    est_id INT NOT NULL,
    session_id INT NOT NULL,
    PRIMARY KEY(est_id, session_id),
    FOREIGN KEY (est_id) REFERENCES student(est_id),
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