from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
load_dotenv()
client = OpenAI()

llm_model = "gpt-4o-mini"

def ask_gpt(prompt):
    try:
      completion = client.chat.completions.create(
        model=llm_model,
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

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse,\
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

style = """American English \
in a calm and respectful tone
"""

prompt = f"""Translate the text \
that is delimited by triple backticks 
into a style that is {style}.
text: ```{customer_email}```
"""
if __name__ == "__main__":
  print(prompt)
  gpt_response = ask_gpt(prompt)
  print("GPT:", gpt_response)
