from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key
my_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=my_api_key)

directory = ["/Users/maximattiogbe/Desktop/9.66-final-project/GPT-3.5-WebPPL/bAbI_tasks_1-20_v1-2/en/qa1_single-supporting-fact_test.txt"]

queries = []
answers = []

for file_path in directory:
    with open(file_path, 'r') as file:
        # Read the file line by line
        line_cnt = 0
        query = ""
        for line in file:
            query += " ".join(line.strip().split()[1:]) + " "
            line_cnt += 1

            if line_cnt % 3 == 0:
                end = query.index("?")
                answer = query[end + 1:].split()[0]
                query = query[:end + 1]

                queries.append(query)
                answers.append(answer)

                query = ""
                answer = ""

for query in queries:
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": query}
    ]
    )
    print(response.choices[0].message.content)
