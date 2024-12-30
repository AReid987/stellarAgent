
from interpreter import interpreter

interpreter.llm.model = "<model_id>"
interpreter.llm.api_base = "http://localhost:1337/v1 "

interpreter.context_window = 5000
interpreter.chat()
