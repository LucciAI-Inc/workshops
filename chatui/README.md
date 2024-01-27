# Instalar Chat UI para probar LLMs desde un ambiente gráfico

Pasos para correr ChatUI localment
- * Clonar repositorio
- * Instalación
- * MongoDB
- * Configuración inicial

## Clonar repositorio
git clone https://github.com/huggingface/chat-ui?tab=readme-ov-file

## Instalación
npm install
npm run dev
Nota: Pata instalar es necesario que tengas la paqueteria de NPM

## MongoDB
Lo más fácil es levantar un contenedor
    docker run -d -p 27017:27017 --name mongo-chatui mongo:latest
Una vez corriendo la liga para tu BD será la siguiente
    MONGODB_URL=mongodb://localhost:27017.

## Configuración inicial
En la raiz del proyecto creamos o editamos el archivo .env con las siguientes variables de ambiente
MONGODB_URL=mongodb://localhost:27017
HF_TOKEN={TU TOKEN DE HUGGING FACE}