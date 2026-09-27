# Amogusifier ඞ

A simple Python tool that transforms any input photo into a mosaic/pixel art composition made entirely out of characters from the popular game **Among Us** (Amogus).

<img width="902" height="495" alt="Screenshot 2026-09-27 180231" src="https://github.com/user-attachments/assets/87110171-232c-4308-8612-442695a04b77" />

## Features
- Automatically samples and resizes images to a processing grid.
- Analyzes color regions and maps them to the closest Among Us crewmate color.
- Places mini crewmate sprites to reconstruct your image.
- Supports customizable grid resolution for higher or lower fidelity.

## Prerequisites
Before running the project, ensure you have Python installed, then install the required dependencies:
```bash
pip install pillow numpy
```

## Repository Structure
- `main.py`: The entry point script to process your image.
- `amogus_sprites.py`: Contains the dictionary mapping and matrix definitions for the Amogus sprites.
- `README.md`: Project documentation.

## Usage
1. Place your target image in the root directory (e.g., `input.jpg`).
2. Run the script:
   ```bash
   python main.py --input input.jpg --output output.png --grid-size 60
   ```
3. Check the `output.png` file to see your Amogusified masterpiece!
