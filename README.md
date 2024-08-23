# Fortune Teller Application
##  Project Overview
The Fortune Teller Application is a simple AWS Lambda-based API that provides random responses ("yes", "no", or "maybe") to user queries. It is designed as a serverless application, leveraging AWS services like Lambda and API Gateway. This project includes unit testing, integration testing, and API testing using Postman, demonstrating best practices in cloud application development and quality assurance.

## Features
Random Fortune Generation: Provides random responses of "yes", "no", or "maybe".

AWS Lambda: Serverless backend ensuring high availability and scalability.

API Gateway: Exposes the Lambda function as an HTTP API.

Testing: Comprehensive testing suite with unit tests, integration tests, and API tests.

## Project Structure

- `src/`: Contains the Lambda function code.
- `tests/`: Contains unit tests, integration tests, and Postman API tests along with the respective outputs.
- `architecture/`: Contains architecture diagram.
- `api-gateway/`: Contains api key.

## Setup Instructions

1. Deploy the Lambda function using AWS Management Console.
2. Set up API Gateway to trigger the Lambda function on HTTP GET requests.
3. Run the provided unit tests and integration tests to ensure everything is working.

## Testing

- **Unit Testing**: Tests the function's logic.
- **Integration Testing**: Tests the Lambda function's interaction with the API Gateway.
- **API Testing**: Automated tests using Postman.

## Deployment

- Deploy the Lambda function from the `src/` directory.
- Use the Postman collection to test the API after deployment.


## Prerequisites
To work on this project, you'll need:

AWS Account: To deploy the Lambda function and API Gateway.

Python 3.x: For writing and running the Lambda function and tests.

Python Unit Test lib: UnitTest

Postman: For API testing.
