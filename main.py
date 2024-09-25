from fastapi import FastAPI, Request
import transformers
import torch
import os
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

app = FastAPI()

@app.post("/generate")
async def generate_text(request: Request):
    data = await request.json()
    message = data.get("message")
    if not message:
        return {"error": "No message provided"}

    model_id = "meta-llama/Meta-Llama-3.1-8B"

    pipeline = transformers.pipeline(
        "text-generation", model=model_id, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto"
    )

    val = pipeline(message)
    print(val)

    return {"response": val}
