import sys
from PIL import Image

args = ["alta", "baixa", "help"]

if len(sys.argv) < 2:
    exit("preciso de mais argumentos!")

if sys.argv[1] not in args:
    print("argumento não permitido!")
    print("hint:", args)
    exit()

def safePixel(w,h,i,j):
    if (i >=0 and i < w) and (j >=0 and j < h):
        return True
    return False

img = Image.open("images/soro.jpg")
img.show()

if img.mode is not "RGB":
    print("convertendo imagem para RGB:")
    img.convert("RGB")


def passa_baixa(image, n = 2):
    neib_sub = n
    img_result = Image.new("RGB",image.size)
    result_pixels = img_result.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = (0,0,0)
            fac = 0;
            for i_neib in range(i - neib_sub, i + neib_sub):
                for j_neib in range(j - neib_sub, j + neib_sub):
                    if(safePixel(image.size[0], image.size[1], i_neib, j_neib)):
                        pr, pg, pb = image.getpixel((i_neib,j_neib))
                        r += pr
                        g += pg
                        b += pb
                        fac += 1

            result_pixels[i,j] = (int(r/fac),int(g/fac),int(b/fac))
    return img_result

def passa_alta(image, n = 1):
    neib_sub = n
    img_result = Image.new("RGB",image.size)
    result_pixels = img_result.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = image.getpixel((i,j))
            nr,ng,nb = (0,0,0)
            fac = 0;
            for i_neib in range(i - neib_sub, i + neib_sub):
                for j_neib in range(j - neib_sub, j + neib_sub):
                    if(safePixel(image.size[0], image.size[1], i_neib, j_neib)):
                        if i_neib is not i and j_neib is not j:
                            pr, pg, pb = image.getpixel((i_neib,j_neib))
                            nr += pr
                            ng += pg
                            nb += pb
                            fac += 1

            result_pixels[i,j] = (int((r*fac - nr)/fac),int((g*fac - ng)/fac),int((b*fac - nb)/fac))
    return img_result

if sys.argv[1] == "baixa":
    print("passa_baixa")
    passa_baixa(img,2).show()
elif sys.argv[1] == "alta":
    passa_alta(img,3).show()
