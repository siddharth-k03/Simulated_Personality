import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from groq import Groq
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

app = FastAPI()

# Serve the static files
app.mount("/static", StaticFiles(directory="static"), name="static")

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# In-memory store for personality insights
personality_insights = ""

def get_personality_insights(paragraph):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze the following paragraph for personality insights based on the Big Five model of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Also provide data on consumer needs, decision-making values, and consumption preferences: {paragraph}. Also, provide ratings and a 1-2 line description for each, thereby keeping it brief.",
                }
            ],
            model="llama-3.1-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Error getting personality insights: {e}")
        raise HTTPException(status_code=500, detail="Error getting personality insights")

def generate_response(question):
    try:
        # Include personality insights in the prompt
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Assume the identity described by the following personality insights: {personality_insights}. Having taken that identity, answer the question in a concise manner: {question}",
                }
            ],
            model="llama-3.1-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Error generating response: {e}")
        raise HTTPException(status_code=500, detail="Error generating response")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    try:
        with open("static/index.html") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)
    except Exception as e:
        logging.error(f"Error reading index.html: {e}")
        raise HTTPException(status_code=500, detail="Error reading index.html")

@app.post("/personality")
async def personality(request: Request):
    global personality_insights
    try:
        data = await request.json()
        paragraph = data.get('paragraph')
        logging.info(f"Received paragraph: {paragraph}")
        personality_insights = get_personality_insights(paragraph)
        return JSONResponse(content={'insights': personality_insights})
    except Exception as e:
        logging.error(f"Error in /personality route: {e}")
        return JSONResponse(content={'error': str(e)}, status_code=500)

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        question = data.get('question')
        logging.info(f"Received question: {question}")
        response = generate_response(question)
        return JSONResponse(content={'response': response})
    except Exception as e:
        logging.error(f"Error in /chat route: {e}")
        return JSONResponse(content={'error': str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
