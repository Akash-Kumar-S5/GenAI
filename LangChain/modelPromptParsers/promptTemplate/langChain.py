from langchain_openai import ChatOpenAI
from LangChain.modelPromptParsers.directApiCall import llm_model
from langchain.prompts import ChatPromptTemplate 


chat = ChatOpenAI(temperature=0.0, model=llm_model)

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

if __name__ == "__main__":

    prompt_template = ChatPromptTemplate.from_template(template_string)
    print(prompt_template.messages[0].prompt)
    print(prompt_template.messages[0].prompt.input_variables)

    customer_style = """American English \
    in a calm and respectful tone
    """

    customer_email = """
    Arrr, I be fuming that me blender lid \
    flew off and splattered me kitchen walls \
    with smoothie! And to make matters worse, \
    the warranty don't cover the cost of \
    cleaning up me kitchen. I need yer help \
    right now, matey!
    """

    cust_msg = prompt_template.format_messages(style=customer_style,text=customer_email)
    print(cust_msg[0])

    response = chat.invoke(cust_msg)
    print(response.content)
