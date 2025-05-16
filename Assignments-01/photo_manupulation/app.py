# Photo Manipulation Project

# Importing necessary libraries 
from PIL import Image, ImageFilter, ImageEnhance

# Opening an image
image = Image.open("./photo.jpg")
# image.show()

# Applying a brightness enhancement
image_enhancer = ImageEnhance.Brightness(image)
color_enhancer = ImageEnhance.Color(image)
enhance_image = image_enhancer.enhance(2)  # Increase brightness by 50%
enhance_image.show()


