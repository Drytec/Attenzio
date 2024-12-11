\c pos_attenzio

INSERT INTO rol VALUES
    (1, 'teacher'),
    (2, 'student'),
    (3,'admin');
INSERT INTO customUser (
    full_name, document, address, media, email, password, phone, validated, rol_id, last_login, is_superuser, is_staff, is_active, date_joined
) VALUES
-- Profesor no validado
(
    'Jh Gomez', '1234', 'Calle 12', NULL, 'jh.gomez@gmail.com', '1234', '+573001234567', FALSE, 1, CURRENT_TIMESTAMP, FALSE, TRUE, TRUE, CURRENT_TIMESTAMP
),
-- Administrador
(
    'Dylan Morales', '4321', 'Carrera 2', NULL, 'morales@gmail.com', '1212', '+573002345678', TRUE, 3, CURRENT_TIMESTAMP, TRUE, TRUE, TRUE, CURRENT_TIMESTAMP
),
-- Profesor validado
(
    'Nick Coder', '444', 'Calle 132', NULL, 'nick.coder@gmail.com', '1314', '+573001234567', TRUE, 1, CURRENT_TIMESTAMP, FALSE, TRUE, TRUE, CURRENT_TIMESTAMP
),
-- Estudiante
(
    'Este Ban', '3434', 'Calle 13', NULL, 'este.ban@gmail.com', '1234', '+573001234567', FALSE, 2, CURRENT_TIMESTAMP, FALSE, TRUE, TRUE, CURRENT_TIMESTAMP
);
