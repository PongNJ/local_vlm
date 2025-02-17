# Run `llama3.2-vision` Locally Using Ollama

This guide demonstrates how to use the `llama3.2-vision` model with Ollama to analyze images. You can modify the prompt by changing the `'content'` field.

## Installation

Ensure you have [Ollama](https://ollama.ai) installed on your system.

```sh
pip install ollama  # Install Ollama if not already installed


## Example Usage

The following script processes images and asks the model to count the number of lanes:

```python
for image_path in images:
    print(f"Processing image: {image_path}")
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'How many lanes are there?',
            'images': [image_path]
        }]
    )
    result_text = response['message']['content']
    print(f"Result: {result_text}")
```
## Running the Script
Save the script as test.py and execute it with the path to the image folder:
```python
python test.py /path/to/folder

```


Replace /path/to/folder with the actual directory containing your images.



