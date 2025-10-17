# os and env 
# workdir
# copy files form the host to the image
# run commands to config the app
# environment variables for config
# save the exact port for the application
# run the application

FROM node

WORKDIR habibi-food

COPY package.json .

RUN npm i 

COPY . .

EXPOSE 3000

CMD [ "node","server.js" ]