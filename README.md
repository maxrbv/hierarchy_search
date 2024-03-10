# Hierarchy search microservice

This microservice is designed to perform hierarchy search within a given structure. It utilizes a JSON file representing the hierarchical structure and enables searching for a path to a specific element within this structure.

## Setup

1.  Clone the repository to your local machine
    ```
    git clone https://github.com/maxrbv/hierarchy_search.git
    ```
2.  Ensure you have Docker installed on your machine.

## Configuration

Before running the microservice, you need to configure it by providing the required settings.

Follow these steps:

1.  Navigate to `assets` directory.
2.  Replace your `structure.json` hierarchy structure file with existing one.
3.  Make sure that you have a proper structure json file.

## Usage

To use the microservice within Docker, follow these steps:

1.  Build the Docker image:
    ```
    docker build -t hierarchy-search-service .
    ```
2.  Run the Docker container:
    ```
    docker run -d -p 8000:8000 --name=hss hierarchy-search-service
    ```
3.  Check logs:
    ```
    docker logs -f hss
    ```
4.  Now you can access the microservice at `http://localhost:8000`.

## Testing

To run test for the microservice you can use the following command:
```
python draft.py <your-uuid>
```

Replace `<your-uuid>` with on of the UUID in your `structure.json` 