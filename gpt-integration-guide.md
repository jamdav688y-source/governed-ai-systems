# GPT Integration Guide

## Setup Instructions for GPT Integration

### Dependencies Installation
To get started with GPT integration, you'll need to install the following dependencies:

```bash
# Install the required libraries
pip install openai
pip install requests
dependencies_other_here
```

### API Key Configuration

1. Obtain your OpenAI API key by signing up at [OpenAI](https://openai.com/api/).
2. Create a `.env` file in your project root directory and add the following line:
   
   ```bash
   OPENAI_API_KEY='your_api_key_here'
   ```
3. Load the environment variables in your application using a library like `python-dotenv`:
   
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   API_KEY = os.getenv('OPENAI_API_KEY')
   ```

### Usage Examples

Here's a simple example of how to use the GPT integration:

```python
import openai
import os

# Load API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to generate a response from GPT
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['choices'][0]['message']['content']

# Example usage
user_prompt = "What is the future of AI?"
print(generate_response(user_prompt))
```

Replace `gpt-3.5-turbo` with the model you wish to use. Run your script, and it should return a response based on the prompt provided.

---