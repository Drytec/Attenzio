
\c pos_attenzio

CREATE TABLE student (
    estId SERIAL PRIMARY KEY,
    estFullName VARCHAR(60) NOT NULL ,
    estEmail VARCHAR(100) UNIQUE NOT NULL,
    estPhone VARCHAR(10),
    estTab VARCHAR(300)
);

CREATE TABLE professor(
    profId SERIAL PRIMARY KEY,
    profCedula INTEGER UNIQUE NOT NULL,
    profFullName VARCHAR(60) NOT NULL,
    profEmail VARCHAR(100) UNIQUE NOT NULL,
    profAddress VARCHAR(300),
    profPicture VARCHAR(200),
    profPass VARCHAR(30)
);

CREATE TABLE session(
    sessionId SERIAL PRIMARY KEY,
    dateSession DATE,
    hourSession TIME,
    qrCode VARCHAR(200),
    sessionMaterial VARCHAR(300),
    profId INT,
    FOREIGN KEY (profId) REFERENCES professor(profId)
);

CREATE TABLE studentSession(
    estId INT NOT NULL,
    sessionId INT NOT NULL,
    PRIMARY KEY(estId, sessionId),
    FOREIGN KEY (estId) REFERENCES student(estId),
    FOREIGN KEY (sessionId) REFERENCES session(sessionId)
);

CREATE TABLE question(
    questionId SERIAL PRIMARY KEY,
    questionText VARCHAR(400),
    sessionId INT NOT NULL,
    FOREIGN KEY (sessionId) REFERENCES session(sessionId)
);

CREATE TABLE option(
    optionId SERIAL PRIMARY KEY,
    optionText VARCHAR(200),
    isCorrect BOOLEAN,
    questionId INT,
    FOREIGN KEY (questionId) REFERENCES question(questionId)
);