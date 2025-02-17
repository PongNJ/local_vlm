import os
import sys
import csv
import ollama

def main(folder_path):
    # Define the image extensions to look for
    image_extensions = {'.jpg', '.jpeg', '.png'}
    
    # Convert folder path to absolute path for safety
    folder_path = os.path.abspath(folder_path)

    # Get a list of image file paths from the folder
    images = [
        os.path.join(folder_path, filename)
        for filename in os.listdir(folder_path)
        if os.path.splitext(filename)[1].lower() in image_extensions
    ]
    
    if not images:
        print(f"No images found in {folder_path}.")
        return

    # Prepare CSV file path
    csv_file_path = os.path.join(folder_path, "results.csv")
    
    # Open CSV file for writing results
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write the header
        writer.writerow(["Image", "Response"])
        
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
            
            # Print the result
            print("Response:", result_text)
            print("-" * 40)
            
            # Write the image path and response to the CSV
            writer.writerow([image_path, result_text])
    
    print(f"All results have been saved to {csv_file_path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python test.py /path/to/folder")
        sys.exit(1)
        
    folder_path = sys.argv[1]
    main(folder_path)
