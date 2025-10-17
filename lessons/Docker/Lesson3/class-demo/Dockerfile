FROM node

WORKDIR habibi-food

COPY package.json .

RUN npm i 

COPY . .

EXPOSE 3000

CMD [ "node","server.js" ]