from rembg import remove
from PIL import Image
input = Image.open("image.jpg") #nama file sesauikan sendiri
output=remove(input)
output.save("output.png")