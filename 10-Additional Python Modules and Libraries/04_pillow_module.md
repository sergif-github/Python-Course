# Module 10: Additional Python Modules and Libraries

## Part 4: Working with Images (Pillow module)

The `Pillow` module is a powerful library for working with images in Python. It provides a wide range of image processing capabilities,
such as opening, manipulating, and saving images in various formats.

### 4.1 Pillow module

To use the `Pillow` module, you need to install it first. You can install it using `pip` with the following command:

```pip install pillow```

Once `Pillow` is installed, you can import it and start working with images. Here's an example that demonstrates some basic image operations:

```python
from PIL import Image

# Open an image file
image = Image.open("image.jpg")

# Display basic information about the image
print("Image Format:", image.format)
print("Image Size:", image.size)
print("Image Mode:", image.mode)

# Show the image
image.show()

# Resize the image
resized_image = image.resize((800, 600))
resized_image.show()

# Convert the image to grayscale
grayscale_image = image.convert("L")
grayscale_image.show()

# Rotate the image by 90 degrees
rotated_image = image.rotate(90)
rotated_image.show()

# Save the modified image
resized_image.save("resized_image.jpg")
grayscale_image.save("grayscale_image.jpg")
rotated_image.save("rotated_image.jpg")
```

In this example, we import the Image module from the PIL package and use it to perform various operations on an image file. Here's what each step does:
- We open an image file using the open() function and store it in the image variable.
- We display basic information about the image, such as its format, size, and mode.
- We show the image using the show() method, which opens a viewer to display the image.
- We resize the image using the resize() method, which takes the desired width and height as parameters.
- We convert the image to grayscale using the convert() method and the "L" mode.
- We rotate the image by 90 degrees using the rotate() method.
- We save the modified images using the save() method, specifying the file name and desired format.

### 4.2 Summary 
 
The Pillow module provides a rich set of functions and methods for advanced image manipulation, including cropping, filtering, blending, and more.
You can refer to the official Pillow documentation for a comprehensive list of capabilities and usage examples.