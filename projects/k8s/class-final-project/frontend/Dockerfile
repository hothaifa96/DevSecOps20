ARG NODE_VERSION=22-alpine
ARG NGINX_VERSION=stable-alpine

FROM node:${NODE_VERSION} AS build
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

ENV VITE_API_URL=http://127.0.0.1:5000
EXPOSE 5173

CMD [ "npm","run","dev", "--","--host" ]