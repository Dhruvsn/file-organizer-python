
import os
import shutil
from datetime import datetime

def organize_files(directory):
	# Ensure the given directory exists
	if not os.path.isdir(directory):
	    print(f" The directory '{directory}' doesn't exist!")
	    return

	# List all files in the directory
	for filename in os.listdir(directory):
	    file_path = os.path.join(directory, filename)

	# only proceed if it's a file (not a folder)
	    if os.path.isFile(file_path):

		# Get the modification timestamp
		mod_time = os.path.getmtime(file_path)
		date = datetime.fromtimestamp(mod_time)
		folder_name = date.strftime('%b-%y')

		# create folder if it doesn't exist
		folder_path = os.path.join(directory,folder_name)
		if not os.path.exists(folder_path):
		    os.makedir(folder_path)
		    print(f" created folder: {folder_path}")

		# Move the file
		shutil.move(file_path,os.path.join(folder_path,filename))
		print(f" Moved '{filename}' to '{folder_name}'")

# --------------- Run the script ----------- 
directory = input("Enter the path of the directory to organize: ")
organize_by_month(directory)
