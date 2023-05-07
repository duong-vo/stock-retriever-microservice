# Super Simple Stock Retriever
### Description
A super simple stock retriever built upon 2 microservices. One microservice is a stock retriever built by FastAPI. The other is a simple python script to retrieve stock data from yfinance. Both microservices share a Redis database. The application is deployed using docker.

### Why I build this
It took me 2 hours to build this to learn about the microservice architecture as well as using docker to organize both microservice so that they can work together.