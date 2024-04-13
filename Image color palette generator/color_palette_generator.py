from PIL import Image
import pandas as pd
import os


def rgb_to_hex(r, g, b):
    '''
    convert rgb to hex which is conversiom from decimal to hexa decimal
    '''
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def generate_palette(filename):
    image = Image.open(filename)

    image.save('static/images/input_image.png')

    os.remove(filename)

    #getting list of rgba values of each pixel in the the image
    image_array = list(image.getdata())

    #converting the rgba list to hexcode list
    hex_array = [rgb_to_hex(rgb[0],rgb[1],rgb[2]) for rgb in image_array]


    df = pd.DataFrame({'hex_code' : hex_array})

    #using pandas function value_counts() to get the number of occurence for each hexcode
    #it gives us dataframe most to least occured hexcodes 
    df2 = pd.DataFrame(data = df['hex_code'].value_counts())

    df2.rename(columns={'hex_code':'Count'}, inplace=True)

    # #getting top 10 codes and removing the white and black hexcode
    # generated_palette = [(df2.index[i], df2['Count'][i]) for i in range(0,12) if df2.index[i] != '#ffffff' and df2.index[i] != '#000000']


    generated_palette = []
    last_i = 0
    i = 0
    while len(generated_palette) != 10:
        if i == 0 :
            generated_palette.append((df2.index[i], df2['Count'][i]))
            print(generated_palette)
            i += 1
            last_i = len(generated_palette)-1
            print( i, last_i)
        elif abs(int(generated_palette[last_i][0][1:3],16)-int(df2.index[i][1:3],16)) > 20 or abs(int(generated_palette[last_i][0][3:5],16)-int(df2.index[i][3:5],16)) > 20 or abs(int(generated_palette[last_i][0][5:7],16)-int(df2.index[i][5:7],16)) > 20:
            generated_palette.append((df2.index[i], df2['Count'][i]))
            i += 1    
            last_i = len(generated_palette)-1
            print( i, last_i)
        else:
            i += 1    
        print(i)    

    return generated_palette


# l = generate_palette('input_image.png')
# print(l)
