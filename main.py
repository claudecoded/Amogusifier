import argparse
import numpy as np
from PIL import Image
from amogus_sprites import AMOGUS_MASK, VISOR_COLOR, get_closest_crewmate_color

def amogusify(image_path, output_path, grid_size=50):
    # Load and open image
    img = Image.open(image_path).convert("RGB")
    
    # Calculate aspect ratio and target dimensions
    width, height = img.size
    aspect_ratio = height / width
    
    grid_w = grid_size
    grid_h = int(grid_size * aspect_ratio)
    
    # Resize image to match our grid layout
    small_img = img.resize((grid_w, grid_h), Image.Resampling.BILINEAR)
    img_array = np.array(small_img)
    
    # Sprite base configuration (5x5 pixels per Amogus)
    sprite_h, sprite_w = AMOGUS_MASK.shape
    
    # Create an empty canvas for the final high-res output
    canvas_w = grid_w * sprite_w
    canvas_h = grid_h * sprite_h
    canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)
    
    # Reconstruct image pixel by pixel using Among Us crewmates
    for y in range(grid_h):
        for x in range(grid_w):
            pixel_color = img_array[y, x]
            # Get the optimal matching Among Us color
            body_color = get_closest_crewmate_color(pixel_color)
            
            # Draw the 5x5 sprite onto the canvas
            for sy in range(sprite_h):
                for sx in range(sprite_w):
                    mask_val = AMOGUS_MASK[sy, sx]
                    
                    target_y = y * sprite_h + sy
                    target_x = x * sprite_w + sx
                    
                    if mask_val == 1: # Body
                        canvas[target_y, target_x] = body_color
                    elif mask_val == 2: # Visor
                        canvas[target_y, target_x] = VISOR_COLOR
                    else: # Background / Empty space
                        # Optional: Use a dimmed version of the original color for background
                        canvas[target_y, target_x] = (int(pixel_color[0]*0.15), int(pixel_color[1]*0.15), int(pixel_color[2]*0.15))

    # Save output image
    output_img = Image.fromarray(canvas)
    output_img.save(output_path)
    print(f"Success! Amogusified image saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transform photos into Amogus mosaic pixel art.")
    parser.add_argument("--input", required=True, help="Path to input photo")
    parser.add_argument("--output", default="output.png", help="Path to output saved photo")
    parser.add_argument("--grid-size", type=int, default=60, help="Horizontal resolution (number of Amogus characters wide)")
    
    args = parser.parse_args()
    amogusify(args.input, args.output, args.grid_size)
