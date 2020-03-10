FROM node:12-buster

ADD package.json .
ADD package-lock.json .
RUN npm install
ADD . .
RUN npm run build

FROM nginx:alpine

COPY --from=0 dist /usr/share/nginx/html
