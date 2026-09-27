import numpy as np

# A basic 5x5 pixel mask representing an Among Us character (Crewmate)
# 1 = Body color, 2 = Visor color (Light Blue), 0 = Empty/Transparent
AMOGUS_MASK = np.array([
    [0, 1, 1, 1, 0],
    [1, 1, 2, 2, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0]
], dtype=np.uint8)

# Color palette mapped to standard Among Us crewmate colors (RGB)
CREWMATE_PALETTE = {
    "red": (198, 17, 17),
    "blue": (19, 46, 209),
    "green": (17, 127, 45),
    "pink": (237, 84, 186),
    "orange": (240, 125, 13),
    "yellow": (245, 245, 87),
    "black": (63, 71, 78),
    "white": (214, 224, 240),
    "purple": (107, 47, 187),
    "brown": (113, 73, 30),
    "cyan": (56, 254, 220),
    "lime": (80, 239, 57)
}

VISOR_COLOR = (149, 202, 220) # Light blue visor

def get_closest_crewmate_color(rgb_color):
    """Finds the closest crewmate palette color to the given RGB input."""
    colors = list(CREWMATE_PALETTE.values())
    distances = [np.linalg.norm(np.array(rgb_color) - np.array(c)) for c in colors]
    return colors[np.argmin(distances)]
