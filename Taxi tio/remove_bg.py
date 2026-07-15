from rembg import remove
from PIL import Image
import sys

input_path = 'tiggo.png'
output_path = 'tiggo_no_bg.png'

try:
    print("Loading image...")
    input_img = Image.open(input_path)
    print("Removing background...")
    output_img = remove(input_img)
    print("Saving image...")
    output_img.save(output_path)
    print("Done!")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
