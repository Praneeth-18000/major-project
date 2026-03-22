from groq import Groq
import os

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY", ""))

# Test input data
plot = "A detective discovers that the AI assistant helping them solve crimes is actually the culprit."
tone = "dark"
genre = "sci-fi thriller"
topic = "artificial intelligence"
twist = "The detective is also an AI"

prompt = f"""Improve and expand the following story plot with more details and creativity:

Plot: {plot}
Tone: {tone}
Genre: {genre}
Topic: {topic}
Additional Twist: {twist}

Please provide an improved, more detailed version of the story with:
1. Enhanced character development
2. More vivid descriptions
3. Better pacing and structure
4. Incorporation of the twist
5. A compelling narrative arc

Format the response as a well-structured story outline with clear sections."""

try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an expert story editor who improves and expands plot outlines into detailed, engaging narratives."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=2000,
    )
    
    result = chat_completion.choices[0].message.content
    print("Improved Story:")
    print("-" * 50)
    print(result)
except Exception as e:
    print(f"Error: {str(e)}")