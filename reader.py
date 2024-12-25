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
      'content': 'Extract all of the text from this photograph of a book page exactly as it appears in the image. Output the text in markdown format.',
      'images': [path],
    }
  ],
)

print(response.message.content)