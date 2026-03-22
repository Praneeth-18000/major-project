from flask import Flask, render_template, request, jsonify
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize Groq client with API key from environment variable
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    print("Warning: GROQ_API_KEY environment variable not set")

# Lazy initialization of Groq client
_client = None

def get_groq_client():
    global _client
    if _client is None:
        _client = Groq(api_key=GROQ_API_KEY)
    return _client

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/generate_stories', methods=['POST'])
def generate_stories():
    """Generate story outlines based on user inputs"""
    tone = request.form.get('tone', '').strip()
    genre = request.form.get('genre', '').strip()
    topic = request.form.get('topic', '').strip()
    
    if not all([tone, genre, topic]):
        return jsonify({
            "status": "error", 
            "message": "Please provide tone, genre, and topic"
        }), 400
    
    try:
        # Create prompt for story outline generation
        prompt = f"""Generate 5 different story plot outlines based on the following parameters:
- Tone: {tone}
- Genre: {genre}
- Topic: {topic}

Please provide 5 distinct and creative plot outlines, each on a new line. Number them 1-5."""

        # Call Groq API
        client = get_groq_client()
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
        
        # Extract and parse the response
        response_text = chat_completion.choices[0].message.content
        outlines = response_text.split("\n")
        plots = [plot.strip() for plot in outlines if plot.strip() and len(plot.strip()) > 10]
        
        # Ensure we have exactly 5 plots
        if len(plots) < 5:
            plots.extend([f"Plot {len(plots) + 1}: Additional creative storyline needed" for _ in range(5 - len(plots))])
        plots = plots[:5]
        
        return jsonify({
            "status": "success", 
            "plots": plots, 
            "tone": tone, 
            "genre": genre, 
            "topic": topic
        })
    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": f"Error generating stories: {str(e)}"
        }), 500

@app.route('/improve_story', methods=['POST'])
def improve_story():
    """Improve and expand a story plot with additional twists"""
    plot = request.form.get('plot', '').strip()
    tone = request.form.get('tone', '').strip()
    genre = request.form.get('genre', '').strip()
    topic = request.form.get('topic', '').strip()
    twist = request.form.get('twist', '').strip()

    if not plot:
        return jsonify({
            "status": "error", 
            "message": "Please provide a plot to improve"
        }), 400

    try:
        # Create prompt for story improvement
        prompt = f"""Improve and expand the following story plot with more details and creativity:

Plot: {plot}
Tone: {tone}
Genre: {genre}
Topic: {topic}
Additional Twist: {twist if twist else 'None'}

Please provide an improved, more detailed version of the story with:
1. Enhanced character development
2. More vivid descriptions
3. Better pacing and structure
4. Incorporation of the twist (if provided)
5. A compelling narrative arc

Format the response as a well-structured story outline with clear sections."""

        # Call Groq API
        client = get_groq_client()
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
        
        # Extract the response
        improved_story = chat_completion.choices[0].message.content
        
        return jsonify({
            "status": "success", 
            "improved_story": improved_story
        })
    except Exception as e:
        return jsonify({
            "status": "error", 
            "message": f"Error improving story: {str(e)}"
        }), 500

# For Vercel serverless deployment
app.debug = False

if __name__ == '__main__':
    app.run(debug=True)
    print("API KEY:", os.getenv("GROQ_API_KEY"))