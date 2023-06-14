from django.shortcuts import render
import os

import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = os.getenv('GPT_API_KEY')
