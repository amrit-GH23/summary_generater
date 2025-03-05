import google.generativeai as genai
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from dotenv import load_dotenv

load_dotenv() 

# Replace 'YOUR_API_KEY' with your actual Gemini API key
GOOGLE_API_KEY = os.getenv("api_key")

genai.configure(api_key=GOOGLE_API_KEY)

def summarize_text(text, model_name="gemini-1.5-pro-latest"):
    """Summarizes a given text using the Gemini API."""
    model = genai.GenerativeModel(model_name)

    prompt = f"""
    Summarize the following text into a concise summary, highlighting the key points:
    {text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"


@csrf_exempt  
def generate_summary(request):
    summary = None

    if request.method == "POST":
        input_text = request.POST.get("text", "")
        if input_text.strip():
            summary = summarize_text(input_text)

    return render(request, "index.html", {"summary": summary})
