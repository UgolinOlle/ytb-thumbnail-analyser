FROM node:18-alpine

RUN if [ ! -x "$(command -v yarn)" ]; then npm install -g yarn; fi

WORKDIR /app

COPY package.json .

RUN yarn

COPY . .

RUN yarn build

EXPOSE 3000

CMD ["yarn", "preview"]
