from images import Image


img=Image("./giphy.gif")

def detect_edges(image):
    """Detects edges using a simple Sobel operator."""
    width, height = image.getWidth(), image.getHeight()
    new_image = Image(width, height)
    
    # Sobel kernels
    Gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    Gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            sum_x, sum_y = 0, 0
            
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    r, g, b = image.getPixel(x + dx, y + dy)
                    intensity = (r + g + b) // 3  # Convert to grayscale
                    sum_x += intensity * Gx[dx + 1][dy + 1]
                    sum_y += intensity * Gy[dx + 1][dy + 1]
            
            edge_intensity = min(255, max(0, int((sum_x**2 + sum_y**2) ** 0.5)))
            new_image.setPixel(x, y, (edge_intensity, edge_intensity, edge_intensity))
    
    return new_image

edged = detect_edges(img)
edged.draw()
