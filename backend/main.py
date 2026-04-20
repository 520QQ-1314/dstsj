from fastapi import FastAPI
from graph import app as graph_app

app = FastAPI(title="AI Poster SaaS MVP")

@app.post("/generate")
def generate(data: dict):
    result = graph_app.invoke({
        "user_input": data["prompt"]
    })

    return {
        "prompt": result["prompt"],
        "image_url": result["image_url"]
    }
