import google.generativeai as genai

genai.configure(api_key="AIzaSyCwrFnbSFAQ6PmqbJBDeXLv2m1spco8V9w")

for model in genai.list_models():
    print(model.name)