from groq import Groq
import os

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY", ""))

# Test input data
tone = "mysterious"
genre = "thriller"
topic = "artificial intelligence"

prompt = f"""Generate 5 different story plot outlines based on the following parameters:
- Tone: {tone}
- Genre: {genre}
- Topic: {topic}

Please provide 5 distinct and creative plot outlines, each on a new line. Number them 1-5."""

try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a creative story writer who generates engaging plot outlines."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0.7,
        max_tokens=1000,
    )
    
    result = chat_completion.choices[0].message.content
    print("Story Outlines:")
    print("-" * 50)
    print(result)
except Exception as e:
    print(f"Error: {str(e)}")