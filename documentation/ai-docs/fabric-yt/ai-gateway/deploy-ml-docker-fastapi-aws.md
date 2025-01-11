### Objectives
- Learn to deploy a machine learning model into a production environment using FastAPI, Docker, and AWS.
- Understand the process of creating an API, containerizing it with Docker, and deploying it on AWS.
- Gain hands-on experience with FastAPI, Docker, and AWS Elastic Container Service (ECS).

### Instructions
1. **Set Up the Project Structure**:
   - Create a directory called `app`.
   - Inside the `app` directory, create an empty `__init__.py` file.
   - Create a `main.py` file inside the `app` directory.

2. **Write the API Code**:
   - In `main.py`, import the necessary libraries:
     ```python
     from fastapi import FastAPI
     import polars as pl
     from sentence_transformers import SentenceTransformer
     from sklearn.metrics.pairwise import manhattan_distances
     ```
   - Define the embedding model and load the video index:
     ```python
     model = SentenceTransformer('path/to/your/model')
     video_index = pl.scan_parquet('path/to/your/video_index.parquet')
     ```
   - Create the FastAPI app:
     ```python
     app = FastAPI()
     ```
   - Define the API endpoints:
     ```python
     @app.get("/")
     def health_check():
         return {"message": "Health Check OK"}

     @app.get("/info")
     def get_info():
         return {"name": "YT Search", "description": "Search API for Shai's YouTube videos"}

     @app.get("/search")
     def search(query: str):
         results = return_search_results(query, video_index, model, manhattan_distances)
         return results.to_dict()
     ```

3. **Run the API Locally**:
   - Ensure you are in the directory containing `app`.
   - Run the FastAPI app using:
     ```bash
     uvicorn app.main:app --reload
     ```
   - Test the API using a notebook or any API testing tool.

4. **Create a Docker Image**:
   - Create a `requirements.txt` file with the necessary dependencies:
     ```
     fastapi
     polars
     sentence-transformers
     scikit-learn
     numpy
     ```
   - Create a `Dockerfile` with the following content:
     ```Dockerfile
     FROM python:3.10
     WORKDIR /code
     COPY requirements.txt .
     RUN pip install --no-cache-dir -r requirements.txt
     COPY ./app /code/app
     CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
     ```
   - Build the Docker image:
     ```bash
     docker build -t yt_search_image_test .
     ```

5. **Run the Docker Container Locally**:
   - Run the Docker container:
     ```bash
     docker run -d --name yt_search_container_test -p 8080:80 yt_search_image_test
     ```
   - Test the Docker container using the same notebook or API testing tool.

6. **Push the Docker Image to Docker Hub**:
   - Create a new repository on Docker Hub.
   - Tag the Docker image:
     ```bash
     docker tag yt_search_image_test your_dockerhub_username/yt_search_demo
     ```
   - Push the Docker image to Docker Hub:
     ```bash
     docker push your_dockerhub_username/yt_search_demo
     ```

7. **Deploy the Docker Container on AWS ECS**:
   - Go to the AWS ECS console and create a new task definition.
   - Configure the task definition with the necessary settings (e.g., AWS Fargate, operating system, architecture).
   - Specify the container details, including the Docker image URL from Docker Hub.
   - Create a new cluster in AWS ECS.
   - Create a new service in the cluster using the task definition.
   - Ensure the security group allows inbound traffic from your IP address.

8. **Test the Deployed API**:
   - Use the public IP address of the deployed container to test the API.
   - Integrate the API with a front-end interface if desired.

9. **Automate the Data Pipeline**:
   - Consider creating another container service to automate the data pipeline and update the search API with new videos.

10. **Explore Further**:
    - Check out the code and additional resources on GitHub for more details and follow-up videos.
