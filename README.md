# INF 345 Notes API

A small HTTP service built with Python and Flask.

## What it does

This project provides a simple Notes API.

Endpoints:

- GET / - checks that the API is running
- GET /healthz - health check
- GET /notes - returns the available notes

## How to run

Install dependencies:

pip install -r requirements.txt

Start the service:

./scripts/run.sh

The default port is 8080.

You can also use another port:

PORT=9090 ./scripts/run.sh

## How to test

Run:

./scripts/test.sh

Expected result:

TESTS: 3/3

## Port

The service uses the PORT environment variable.

If PORT is not provided, it uses port 8080.# INF 345 Notes API

A small HTTP service built with Python and Flask.

## What it does

This project provides a simple Notes API.

Endpoints:

- GET / - checks that the API is running
- GET /healthz - health check
- GET /notes - returns the available notes

## How to run

Install dependencies:

pip install -r requirements.txt

Start the service:

./scripts/run.sh

The default port is 8080.

You can also use another port:

PORT=9090 ./scripts/run.sh

## How to test

Run:

./scripts/test.sh

Expected result:

TESTS: 3/3

## Port

The service uses the PORT environment variable.

If PORT is not provided, it uses port 8080.
