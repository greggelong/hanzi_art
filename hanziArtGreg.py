
#import pillow
from PIL import Image

# import a picture

image = Image.open('greg.jpg')

# get size
org_width,org_height = image.size
print(image.size)
print(org_width,org_height)

# calculate new size
new_width = 50
new_height = int(50 * (org_height/org_width))
print(new_width,new_height)

#resize and convert to grey
small_image =  image.resize((new_width,new_height))

sm_gr_image = small_image.convert("L")




#get the list of pixel  values
pixellist = list(sm_gr_image.getdata())
#print(pixellist)

#set an empty list for in wich to append characters
charlist =[]

#map characters in that list using if statems for range
for num in pixellist:
    if num >= 0 and num <= 25:

        charlist.append('X')

    elif num >=26 and num <= 50:

        charlist.append('履')
    elif num >= 51 and num <= 75:

        charlist.append('素')
    elif num >= 76 and num <= 100:

        charlist.append('愿')

    elif num >= 101 and num <= 125:

        charlist.append('往')
    elif num >=126 and num <= 150:

        charlist.append('独')


    elif num >=151 and num <= 175:

        charlist.append('行')

    elif num >=176 and num <= 200:

        charlist.append('也')

    elif num >= 201 and num <= 225:

        charlist.append('之')

    elif num >=226 and num <= 255:

        charlist.append('一')

    else:
        charlist.append('X')


#convert the list into a string

charstring= "".join(charlist)

# print every 50 characters of charstring to the terminal

firstplace = 0
# range (start stop step)
for linestep in range(49,len(charstring),50):
    prt_line = charstring[firstplace:linestep] #use string slicing to print every fifty characters on one line
    print(prt_line)
    with open('greg_character1.txt',encoding='utf-8', mode='a+')as file1:
        file1.write(prt_line+'\n')

    firstplace = firstplace + 50



