from PIL import Image
import os

def jpg_to_jpeg(entry_field):
    try:
        input_path = entry_field.get()
        output_directory = os.path.dirname(input_path)
        output_path = os.path.join(output_directory, os.path.basename(input_path).replace(".jpg", ".jpeg"))
        img = Image.open(input_path)
        img.save(output_path)
        img.close()
        print(f"Image saved at {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")