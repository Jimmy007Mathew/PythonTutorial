from images import Image
from functools import reduce

img=Image("./giphy.gif")

def blur_image(image, intensity=1):
   
    width, height = image.getWidth(), image.getHeight()
    new_image = image.clone()
    
    kernel_size = 2 * intensity + 1  
    offset = intensity  

    for x in range(offset, width - offset):
        for y in range(offset, height - offset):
            r, g, b = 0, 0, 0
            count = 0  
            for dx in range(-offset, offset + 1):
                for dy in range(-offset, offset + 1):
                    nr, ng, nb = image.getPixel(x + dx, y + dy)
                    r += nr
                    g += ng
                    b += nb
                    count += 1
            
            new_image.setPixel(x, y, (r // count, g // count, b // count))
    
    return new_image


blurred = blur_image(img, intensity=2) 
blurred.draw()
