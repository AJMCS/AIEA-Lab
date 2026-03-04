from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

message = input("Start you conversation which chatGPT (Type \'quit\' to stop):\n\n")

while(message != "quit"):

    response = client.responses.create(
        model="gpt-5.2",
        reasoning={"effort":"medium"},
        instructions="You are an expert software developer with a specialization in swi-prolog and traditional data structures and algorithms concepts. " \
        "Your specialties lies in the translation of this into swi-prolog specifically.",
        input=message
    )

    print(response.output_text + "\n\n")

    message = input()

