import sys
import os
from PIL import Image
from rembg import remove

# grab the source_folder and output_folder arguments
if len(sys.argv) == 3:
    source_folder, output_folder = sys.argv[1], sys.argv[2]
else:
    source_folder, output_folder = sys.argv[1], "converted_images"

# opening the folder
if (os.path.exists(source_folder)):
    files = os.listdir(source_folder)
else:
    print("No folder found")

# check if the /new exist or not if not then create it
if not os.path.exists(output_folder):
    os.mkdir("converted_images")
    output_folder = "./converted_images"
    output_files = os.listdir(source_folder)

filetype = ".png"
# If user select PNG Check if user want bg remover or not
print("Select Option. Available Options:")
print("     1. Remove Background")
print("     2. Not Remove Background")
background_color = input("Enter the number of your choice: ")

print("Select the desired output format. Available Options: ")
print("     1. PNG")
print("     2. JPEG")
print("     3. GIF")
print("     4. BMP")
user_choice = input("Enter the number of your choice: ")
print("Select Option. Available Options:")
print("     1. Want to Compress Images")
print("     2. Not Want to Compress Images")
compress_choice = input("Enter the number of your choice: ")
if compress_choice == '1':
    print("What is threshold you want to compress")
    threshold = int(input("Enter the number of: "))
else:
    threshold = 0

#Makes sure user put in a valid option, otherwise converts to PNG
if (user_choice.isnumeric()):
    if (user_choice == "2"):
        filetype = ".jpeg"
    elif (user_choice == "3"):
        filetype = ".gif"
    elif (user_choice == "4"):
        filetype = ".bmp"
    

# loop througn poke_dex
try:
    for file in files:
        if background_color == '1':
            img = Image.open(source_folder+"/"+file)
            img = remove(img)
            img = img.convert('RGB') if user_choice == "2" else img
        else:
            img = Image.open(source_folder+"/"+file)
        # convert images to png 
        file = file.split(".")[0]
        path = file + filetype
        #save the image
        if compress_choice == "1":
            width, height = img.size
            new_size = (width//2, height//2)
            img = img.resize(new_size)
            img.save(os.path.join("./"+output_folder, path),optimize = True, quality = threshold)
        else:
            img.save(os.path.join("./"+output_folder, path))
except Exception as e:
    print(f"There is an error in conversion: {e}")
