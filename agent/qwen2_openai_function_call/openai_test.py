from openai import OpenAI
client = OpenAI(api_key="sk-...",base_url="http://localhost:8000/v1")
completion = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
{"role": "user", "content": "What is the weather like in Boston?"},
    {"role": "assistant", "content": "", "function_call": {"name": "get_current_weather", "arguments": "{ \"location\": \"Boston, MA\"}"}},
    {"role": "function", "name": "get_current_weather", "content": """{\"temperature\": "22", \"unit\": \"celsius\", \"description\": \"Sunny\"}"""}],
functions=[
    {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"]
      }
    }
  ]
)

print(completion.choices[0].message)