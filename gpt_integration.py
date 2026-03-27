# GPT Integration Code

import openai

# Function to integrate GPT

def integrate_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Example usage
if __name__ == '__main__':
    prompt = "What are the benefits of using GPT for software development?"
    print(integrate_gpt(prompt))