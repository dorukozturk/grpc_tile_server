FROM node

COPY client /client
WORKDIR /client
RUN yarn run build

FROM nginx
COPY --from=0 /client/dist /usr/share/nginx/html