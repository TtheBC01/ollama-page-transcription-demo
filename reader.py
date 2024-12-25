from ollama import chat
# from pathlib import Path

# Pass in the path to the image
path = input('Please enter the path to the image: ')

# You can also pass in base64 encoded image data
# img = base64.b64encode(Path(path).read_bytes()).decode()
# or the raw bytes
# img = Path(path).read_bytes()

response = chat(
  model='llama3.2-vision',
  messages=[
    {
      'role': 'user',
      'content': 'This is a picture of a page of a book. Extract the text and preserve heading titles. Any equations should be converted to Latex format.',
      'images': [path],
    }
  ],
)

print(response.message.content)