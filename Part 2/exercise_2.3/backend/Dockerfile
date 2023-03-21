FROM golang:1.16

EXPOSE 8080

WORKDIR /usr/src/app/

ENV REQUEST_ORIGIN=http://localhost:5000

COPY go* ./

COPY . .

RUN go build

CMD ["./server"]
