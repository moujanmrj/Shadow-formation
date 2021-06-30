from PIL import Image


def load_image_data(im):
    return im.load(), im.size[0], im.size[1]


def create_shadow(pix, x, y):
    shadow_image = Image.new('RGBA', (int(x * 1.3), y ), (255, 255, 255, 255))
    shadow_pix = shadow_image.load()
    for i in range(y):
        for j in range(x):

            try:
                r, g, b, a = pix[j, i]
            except:
                r, g, b = pix[j, i]
            if r < 250 or g < 250 or b < 250:
                shadow_pix[j + int(0.2 * i), i] = (70, 70, 70, 255)
    shadow_image.save("shadow.png")
    return shadow_pix


file_name = input()
image = Image.open(file_name)
pixels, x, y = load_image_data(image)
shadow_pixels = create_shadow(pixels, x, y)
sec_image = Image.new('RGB', (int(x * 1.3), y), (255, 255, 255, 255))
fin_image = sec_image.load()
for i in range(int(x * 1.3)):
    for j in range(y ):
        if i >= x or j >= y:
            fin_image[i, j] = shadow_pixels[i, j]
        else:
            try:
                r, g, b, a = pixels[i, j]
            except:
                r, g, b = pixels[i, j]
            if r >= 250 and g >= 250 and b >= 250:
                fin_image[i, j] = shadow_pixels[i, j]
            else:
                fin_image[i, j] = r,g,b

sec_image.save(file_name.replace('.', '_with_shadow.'))
