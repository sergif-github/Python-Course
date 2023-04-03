# PILLOW
print('''PILLOW''')

from PIL import Image

img = Image.open('img.png')
print("My image type:", type(img))
print("My image size:", img.size)
print("My image filename:", img.filename)

print("\nCropping, copying and pasting images")
img.show()
img_cropped = img.crop((img.width/2-200, 800, img.width/2+200, 1257))
img.paste(im=img_cropped, box=(0, 0))
img.paste(im=img_cropped, box=(796, 0))
img.show()

print("\nResizing images")
img = img.resize((3000, 500))
img.show()

print("\nRotating images")
img = img.rotate(120, expand=True)
img.show()

print("\nTransparency")
red_img = Image.open('red.png')
red_img.show()
red_img.putalpha(128)
red_img.show()


print("\nSaving images")
red_img.save("red_transparency.png")

