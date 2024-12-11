\c pos_attenzio

CREATE TABLE rol(
    rol_id INT PRIMARY KEY,
    rol_name VARCHAR(100)
);

CREATE TABLE customUser (
    custom_user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    document VARCHAR(20) UNIQUE NOT NULL,
    address VARCHAR(100),
    media VARCHAR(200),
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    phone VARCHAR(30),
    validated BOOLEAN DEFAULT FALSE,
    rol_id INT REFERENCES rol(rol_id),
    last_login TIMESTAMPTZ,
    is_superuser BOOLEAN DEFAULT FALSE,
    is_staff BOOLEAN DEFAULT FALSE,
    is_active BOOLEAN DEFAULT TRUE,
    date_joined TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE course(
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(300),
    course_schedule VARCHAR(300)
);

CREATE TABLE material(
    material_id SERIAL PRIMARY KEY,
    material_link VARCHAR(300)
);

CREATE TABLE session(
    session_id SERIAL PRIMARY KEY,
    session_name VARCHAR(300),
    session_date_start TIME,
    session_date_end TIME,
    session_description VARCHAR(300),
    qr_code VARCHAR(300),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);

CREATE TABLE materialSession(
    session_id INT NOT NULL,
    material_id INT NOT NULL,
    PRIMARY KEY(session_id, material_id),
    FOREIGN KEY (session_id) REFERENCES session(session_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES material(material_id) ON DELETE CASCADE
);

CREATE TABLE customUserCourse(
    customusercourse_id SERIAL PRIMARY KEY,
    custom_user_id INT NOT NULL,
    course_id INT NOT NULL,
    FOREIGN KEY (custom_user_id) REFERENCES customUser(custom_user_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);

CREATE TABLE question(
    question_id SERIAL PRIMARY KEY,
    question_text VARCHAR(400),
    session_id INT NOT NULL,
    FOREIGN KEY (session_id) REFERENCES session(session_id) ON DELETE CASCADE
);

CREATE TABLE option(
    option_id SERIAL PRIMARY KEY,
    option_text VARCHAR(200),
    is_correct BOOLEAN DEFAULT FALSE,
    question_id INT,
    FOREIGN KEY (question_id) REFERENCES question(question_id) ON DELETE CASCADE
);

CREATE TABLE customUserOption(
    custom_user_id INT NOT NULL,
    option_id INT NOT NULL,
    PRIMARY KEY (custom_user_id, option_id),
    FOREIGN KEY (custom_user_id) REFERENCES customUser(custom_user_id) ON DELETE CASCADE,
    FOREIGN KEY (option_id) REFERENCES option(option_id) ON DELETE CASCADE
);