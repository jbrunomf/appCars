import os

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def get_car_sale_description(model, brand, year):
    response = client.completions.create(
        model='gpt-3.5-turbo',
        prompt=f'Crie uma descrição devenda para um veículo do modelo {model} da marca {brand} do ano {year} ressaltando as vantagens desse modelo.',\
        stream=False
    )
    return response['coices'][0]['text']
