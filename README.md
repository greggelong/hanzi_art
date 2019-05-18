## Hanzi Art

[see examples on website](https://greggelong.github.io/index.html)  

Hanzi art process

I am using python and the pillow module for manipulating images

    import the jpeg
    resize image
    convert it to gray-scale
    read the values of the pixels
    map the value of the pixels to stroke number Chinese characters
    Chinese_char = [ 'X','善', '随', '俗', '若', '水', '乡', '上', '入', '。', ' ']
    Darkest pixels will get mapped to the character with most strokes, here '善' with 12 strokes
    The list is turned to a string and then printed according to the number of pixels in the width
    The image is saved to a text file

Hanzi art Philosophy

The choice of set phrases or 成语 perhaps lend some meaning to the image

The image can inspire the phrase

A series of images are being made using the 《千字文》 (Thousand Character Text)

Images aslo from the 《道德经》The Dao

 

 
