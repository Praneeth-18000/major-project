# StoryForge Setup Guide

## Quick Start

Follow these steps to get StoryForge up and running on your machine:

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- groq (Groq API client)
- python-dotenv (environment variable management)

### Step 2: Get Your Groq API Key

1. Visit https://console.groq.com/keys
2. Sign up or log in to your account
3. Create a new API key
4. Copy the API key (it starts with "gsk_")

### Step 3: Configure Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Open `.env` in your text editor and replace `your_groq_api_key_here` with your actual API key:
```
GROQ_API_KEY=gsk_your_actual_api_key_here
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

Navigate to: http://127.0.0.1:5000

## Testing Individual Components

### Test Story Generation (1.py)

```bash
python 1.py
```

This will generate 5 story plot outlines using predefined test data.

### Test Story Improvement (2.py)

```bash
python 2.py
```

This will improve and expand a sample story plot.

## Troubleshooting

### Issue: "GROQ_API_KEY environment variable not set"
**Solution**: Make sure you've created a `.env` file with your API key.

### Issue: "ModuleNotFoundError: No module named 'groq'"
**Solution**: Run `pip install -r requirements.txt`

### Issue: API rate limit errors
**Solution**: Groq's free tier has rate limits. Wait a moment and try again, or check your usage at https://console.groq.com

### Issue: Empty or invalid responses
**Solution**: Check that your API key is valid and has not expired.

## Features

- **Story Generation**: Generate 5 unique plot outlines based on tone, genre, and topic
- **Story Improvement**: Expand and enhance selected plots with additional details and twists
- **Interactive UI**: Drag-and-drop interface for easy story creation
- **Dark/Light Theme**: Toggle between themes for comfortable viewing
- **Download Stories**: Save your generated stories as text files

## API Models Used

- **llama-3.1-70b-versatile**: A powerful language model for creative story generation
- Fast response times (~1-2 seconds)
- High-quality, coherent story outputs

## Support

For issues or questions:
- Check the main README.md
- Review error messages in the terminal
- Ensure your API key is valid and properly set

Happy storytelling! 🎭📚
