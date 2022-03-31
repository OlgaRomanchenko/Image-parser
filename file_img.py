import sys
from PIL import Image


def flip_image(image_path, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)
    #rotated_image.show()


def new_image(first_image, second_image):
    images = [Image.open(x) for x in [first_image, second_image]]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))
    x = 0
    for im in images:
        new_im.paste(im, (x, 0))
        x += im.size[0]

    new_im.save('new_image.jpg')
    new_im.show()


def main():
    image = 'images/images.jpg'
    image2 = 'images/images2.jpeg'
    flip_image(image, 'mirror_image.jpg')
    flip_image(image2, 'mirror_image2.jpg')
    new_image('mirror_image.jpg', 'mirror_image2.jpg')


if __name__ == '__main__':
    main()
