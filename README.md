# Streamlit Blog App

This project is a Streamlit-based web application designed for blogging, specifically focusing on data engineering topics. The app structure facilitates easy navigation through educational and technical posts, providing an interactive learning experience.

## Structure

- `app/`: Main application directory.
  - `images/`: Contains images used within the app.
  - `pages/`: Contains the Python scripts for the app's pages.
    - `Home.py`: The homepage of the app.
    - `Experience.py`: Page detailing the author's experience.
    - `Technical.py`: Technical discussions and tutorials.
    - `tech_posts/`: Directory for blog posts written in Markdown format.

## Setup and Requirements

To set up and run this application, ensure you have Docker installed. The app includes a `Dockerfile` and a `docker-compose.yml` for containerization, making the setup process straightforward.

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Build the Docker container using the provided `Dockerfile`:
   ```sh
   docker build -t streamlit_blog .
