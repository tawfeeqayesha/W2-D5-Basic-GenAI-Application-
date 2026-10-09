
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# 1. Load API key from .env file
load_dotenv()

# 2. Initialize the language model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

# 3. Create the breakfast prompt
prompt = ChatPromptTemplate.from_template("""
You are a helpful breakfast recipe assistant.

Suggest exactly 5 healthy vegetarian breakfast ideas.

Requirements:
- Number the ideas from 1 to 5.
- Use vegetables wherever possible.
- Give each idea a short, clear name.
- Include the main ingredients.
- Include a brief preparation method.
- Keep the recipes simple and suitable for beginners.
- Do not include meat, fish, or eggs.

User request: {user_request}
""")

# 4. Create the LangChain chain
chain = prompt | llm | StrOutputParser()

# 5. Run the prompt twice
requests = [
    "Suggest five Indian vegetarian breakfast ideas using vegetables.",
    "Suggest five different vegetarian breakfast ideas using vegetables, without repeating the first set."
]

for run_number, user_request in enumerate(requests, start=1):
    print("\n" + "=" * 60)
    print(f"BREAKFAST IDEAS - RUN {run_number}")
    print("=" * 60)

    response = chain.invoke({"user_request": user_request})

    print(response)
    print()
