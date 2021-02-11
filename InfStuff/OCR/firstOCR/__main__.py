import pytesseract as tess
from PIL import Image


def main():
    img = Image.open('test.png')
    text = tess.image_to_string(img)



if __name__ == '__main__':
    main()
