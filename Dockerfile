FROM node:14-alpine AS coquin-build
COPY coquin /coquin/
WORKDIR /coquin
RUN npm install --no-progress
RUN npm run -s build

FROM nginx AS coquin
COPY --from=coquin-build /coquin/dist/ /usr/share/nginx/html/
EXPOSE 80
