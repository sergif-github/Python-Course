f = open("new_file.txt", 'w+')
f.write("Here is some text")
f.close()

f = open("new_file2.txt", 'w+')
f.write("Here is some text")
f.close()

import zipfile

# Create the zip file first
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
# Write to zip file
comp_file.write("new_file.txt", compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# Extract from zip files
zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")


import shutil

print("The shutil library can extract or archive everything at once.")
print("Also the shutil library accept a archive format parameter zip, tar, gztar, bztar, or xztar.")

directory_to_zip = 'C:\\Users\\'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', directory_to_zip)
shutil.unpack_archive(output_filename, dir_for_extract_result, 'zip')
