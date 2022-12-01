import sys
import os
from PIL import Image

# grab the first and the second argument.
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if output_folder exists, if not create.
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

# loop through image_folder and convert images to png
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	filename_without_extension = os.path.splitext(filename)[0]
	# save to the output_folder folder
	img.save(f'{output_folder}{filename_without_extension}.png', 'png')
	print('Successfully converted!')