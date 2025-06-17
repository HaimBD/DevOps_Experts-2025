FROM node:16 AS builder
WORKDIR /app
ENV NPM_CONFIG_LOGLEVEL info
COPY package.json ./
RUN npm install
COPY . .
RUN npm run build


FROM node:16-alpine
WORKDIR /app
COPY --from=builder /app/dist /app
CMD ["node", "app.js"]
