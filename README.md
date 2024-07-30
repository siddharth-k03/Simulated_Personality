# Chatbot Application with Personality Insights

This project is a web application that utilizes the Groq API with the Llama model to provide personality insights based on a user's input paragraph. It then uses these insights to generate responses to user questions in the context of the provided personality.

## Features

- Analyze a paragraph to derive personality insights based on the Big Five personality traits.
- Generate responses to user questions considering the derived personality insights.
- Serve a web interface using FastAPI and Uvicorn.

## Prerequisites

- Python 3.7+
- Groq API key (sign up at [Groq](https://groq.com) to obtain an API key)

## Setup

### Step 1: Clone the Repository
```bash
git clone  https://github.com/siddharth-k03/Simulated_Personality.git
cd Simulated_Personality
```

### Step 2: Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```

### Step 3: Install the Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Obtain the Groq API Key
Sign up or log in to your account at Groq.
Navigate to the API section and generate a new API key.

### Step 5: Create a .env File
In the root directory of the project, create a file named .env and add your Groq API key:

```makefile
GROQ_API_KEY=your_groq_api_key
```

## Running the Application

1. Start the FastAPI server:
    ```bash
    uvicorn server:app --reload
    ```

2. Open your web browser and go to `http://localhost:8000`.

## Project Structure

- `static/index.html`: The frontend of the application.
- `static/styles.css`: The CSS file for styling the frontend.
- `server.py`: The backend code using FastAPI.
- `requirements.txt`: The file to install project dependencies.
- `README.md`: The project documentation.

## Usage

### Personality Insights

1. Enter a paragraph detailing the personality in the provided text area.
2. Click the "Get Personality Insights" button.
3. The insights will be displayed below the text area.

### Chat with Chatbot

1. After getting the personality insights, enter a question in the provided input field.
2. Click the "Ask" button.
3. The response considering the personality context will be displayed below the input field.

## Example

**Personality Paragraph:**
I am a creative and detail-oriented individual who thrives in dynamic environments. I am always eager to explore new ideas and embrace innovative solutions. I am highly organized and conscientious, ensuring that every task I undertake is completed to the highest standard. While I enjoy working independently, I also value collaboration and believe in the power of teamwork to achieve common goals. I am known for my positive attitude and ability to remain calm under pressure, which helps me navigate challenging situations effectively. I am driven by a strong sense of purpose and am committed to making a meaningful impact in my work and community.

**Question:**
What is your favorite season?

**Response:**
Based on my personality, which values creativity, innovation, and collaboration, my favorite season is Autumn. It inspires an appreciative spirit and reflects the qualities of change and creativity, making it a perfect time for new discoveries and cultural celebrations.

##Acknowledgments

This project utilizes the following sources and technologies:

- [FastAPI](https://fastapi.tiangolo.com/) for creating the web API.
- [Uvicorn](https://www.uvicorn.org/) as the ASGI server.
- [Groq API](https://groq.com) for accessing the Llama model and generating personality insights.
- [python-dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables.
- [Llama Model](https://huggingface.co/models) for language understanding and generation.
