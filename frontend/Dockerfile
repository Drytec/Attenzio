# Usa una imagen base de Node.js
FROM node:16

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del frontend al contenedor
COPY . .

# Instalar las dependencias del proyecto
RUN npm install

# Si es una SPA (por ejemplo, React), construimos los archivos estáticos
RUN npm run build

# Exponer el puerto en el que queremos servir la aplicación
EXPOSE 3000

# Iniciar un servidor estático con serve (o el comando adecuado para tu framework)
CMD ["npx", "serve", "build", "-s", "-l", "3000"]
