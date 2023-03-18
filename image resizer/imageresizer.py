from PIL import Image

img = Image.open('image resizer\hello.jpg')

print(f"Current size: {img.size}")

resized_image = img.resize((500, 500))

resized_image.save("resized-500.jpeg")
