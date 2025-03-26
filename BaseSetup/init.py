from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
load_dotenv()
client = OpenAI()

def ask_gpt(prompt):
    try:
      completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
          ]
        )
      return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return None

user_prompt = "What is the capital of newzeland?"
gpt_response = ask_gpt(user_prompt)
print("GPT:", gpt_response)
