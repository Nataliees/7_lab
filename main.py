def one():
    from PIL import Image

    name = "pic.jpeg"
    with Image.open(name) as img:
        img.load()
    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)

def two():
    from PIL import Image

    filename = "pic.jpeg"
    with Image.open(filename) as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))

    new_img.save("pic_new_size.jpg")

    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("pic_mirrored.jpg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("pic_flipped.jpg")

def three():
    from PIL import Image, ImageFilter

    filenames = ["1.jpeg", "2.jpg", "3.jpg", "4.jpeg", "5.jpg"]

    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.FIND_EDGES)
            new_img.save("new_" + file)

def four():
    from PIL import Image

    water = "pngtext.png"
    with Image.open(water) as img_water:
        img_water.load()

    img_water = Image.open(water)
    filename = "pic.jpeg"
    with Image.open(filename) as img:
        img.load()

    img.paste(img_water, (50, 50))
    img.save("pic_with_text.jpg")

one()
two()
three()
four()