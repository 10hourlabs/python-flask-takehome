FROM node:16-alpine 
COPY ./web ./ui
WORKDIR /ui
RUN npm install
# Start the app
CMD [ "npm", "start"]