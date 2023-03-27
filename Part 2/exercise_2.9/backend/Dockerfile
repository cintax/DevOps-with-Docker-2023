FROM golang:1.16

WORKDIR /usr/src/app/

ENV REQUEST_ORIGIN=http://localhost

COPY . .

RUN go build

CMD ["./server"]
