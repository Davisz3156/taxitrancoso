from PIL import Image
import os

def process_image(input_path, output_path, size=(800, 800)):
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if not already
            if img.mode != "RGB":
                img = img.convert("RGB")
            
            # Crop to square (1:1 ratio) to match "aspect-ratio: 1 / 1" in CSS
            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2
            
            img = img.crop((left, top, right, bottom))
            
            # Resize
            img = img.resize(size, Image.Resampling.LANCZOS)
            
            # Save as WebP
            img.save(output_path, "WEBP", quality=80)
            print(f"Successfully processed {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

if __name__ == "__main__":
    process_image("cliente5.jpeg", "cliente5.webp")
    process_image("cliente6.jpeg", "cliente6.webp")
