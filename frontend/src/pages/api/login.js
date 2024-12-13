import axios from 'axios';
const express = require('express');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const bodyParser = require('body-parser');
const { CustomUser } = require('./models'); 

const app = express();
const PORT = 5000;


app.use(bodyParser.json());

app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;

    if (!email || !password) {
        return res.status(400).json({ error: 'Por favor, proporciona ambos: email y contraseña.' });
    }

    try {
        
        const user = await CustomUser.findOne({ where: { email } });

        if (!user) {
            return res.status(401).json({ error: 'Credenciales inválidas. Por favor, verifica tu email y contraseña.' });
        }

        
        const isPasswordValid = await bcrypt.compare(password, user.password);

        if (!isPasswordValid) {
            return res.status(401).json({ error: 'Credenciales inválidas. Por favor, verifica tu email y contraseña.' });
        }

        
        const token = jwt.sign(
            { id: user.id, email: user.email, rol: user.rol_id },
            'secretKey', 
            { expiresIn: '1h' }
        );

        
        return res.status(200).json({
            message: 'Login exitoso.',
            token,
            user: {
                id: user.id,
                full_name: user.full_name,
                email: user.email,
                rol: user.rol_id
            }
        });
    } catch (error) {
        console.error('Error en el login:', error);
        return res.status(500).json({ error: 'Error interno del servidor.' });
    }
});


app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
