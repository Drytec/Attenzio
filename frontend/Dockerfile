# Usa una imagen base que tenga Node.js
FROM node:16

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias del proyecto
RUN npm install

# Copia el código fuente del proyecto en el contenedor
COPY . .

# Construye la aplicación (esto genera la carpeta "build")
RUN npm run build

# Instala 'serve' globalmente para poder usarlo para servir la app
RUN npm install -g serve

# Expone el puerto en el que se va a servir la app
EXPOSE 3000

# Comando para servir la aplicación usando serve
CMD ["serve", "-s", "build", "-l", "3000"]