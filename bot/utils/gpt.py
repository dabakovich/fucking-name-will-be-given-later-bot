import openai

from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def get_gpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )

    print('gpt total tokens: ', response.usage)

    return response.choices[0].message


get_gpt_response([{"role": "system", "content": "You are helpful assistant"}, {"role": "user", "content": "Hello"}])
