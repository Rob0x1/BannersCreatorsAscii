#!/usr/bin/env python
# -*- coding: utf-8 -*-
#date: sáb 29 ene 2022 17:03:16
#Roberto 
from PIL import Image, UnidentifiedImageError
import argparse
import sys

#colorsitos uwu
clean="\033[0m"
black="\033[1;30m"
red="\033[1;31m"
green="\033[1;32m"
yell="\033[1;33m"
pur="\033[1;34m"
blue="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"


def crear_imagen(args):
    try:
        img=Image.open(args.image)
    except (FileNotFoundError, UnidentifiedImageError) as error:
        #print("No se encontro el archivo o directorio, oh no es una imagen",error)
        print(error)
        sys.exit(0)

    if not args.savefile:
        args.savefile=args.image[:args.image.rfind('.')]+'.txt'

    if args.method == "original":
        origin_size=img.size
        img=img.resize((args.widht,int(args.widht*origin_size[1]/origin_size[0])))
    if args.method == "upscaling":
        img=img.resize((args.width,args.heigth))
    if args.method == "aspect-ratio":
        img.thumbnail((args.width,args.heigth))

    pixeles = img.load()
    cadena=''
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            if type(pixeles[j,i])==tuple:
                r,g,b=pixeles[j,i][:3]
                if r == 0 and g == 0 and b == 0:   
                        cadena+=f'\033[0m  '
                else:
                    cadena+=f'\033[48;2;{r};{g};{b}m  '
            else:
                cadena+='\033[%sm'%(30 if pixeles[j,i]else '')

        cadena+='\033[m\n'

    with open(args.savefile,"w") as f:
        f.write(cadena)
    if "Yes" == args.printCLI:
        print(cadena)
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description=f"{black}Creador de Banner con cualquier imagen{yell}")
    parser.add_argument("--image","-i",required=True,help="Selecciona la imagen / select an image")
    parser.add_argument("--width","-w",type=int,required=False,default=30,help="tamaño en anchura / width in size")
    parser.add_argument("--heigth","-H",type=int,required=False,default=35,help="tamaño de altura/ height size")
    parser.add_argument("--method","-m",type=str,
                        choices=['original', 'upscaling', 'aspect-ratio'],
                        default='aspect-ratio', required=False,
                        help='tipo de imagen, original, rescalado y relacion de aspecto / image type, original, upscaling and aspect ratio')

    parser.add_argument("--savefile","-s",type=str,required=False,default=None,help="archivo a guardar, ejmplo: banner.txt / file to save, example: banner.txt")
    parser.add_argument("--printCLI","-p",type=str,required=False,default="Yes",choices=["Yes","No"])
    #parser.add_argument("--version", "-v")
    args = parser.parse_args()
    sys.stdout.write(str(crear_imagen(args)))



if __name__ == '__main__':
    main()

