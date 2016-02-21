import os

ROOT_DIRECTORY = '/Users/amitshekhar/Documents/Development/Bobble'

# all file name list
file_names = set()
file_names_in_hdpi = set()
file_names_in_xhdpi = set()
files_not_used = set()

# all files list
files = set()


# add all file names of menu
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/menu'):
    # add path to all file names.
    for filename in filenames:
        files.add(os.path.join(dirname, filename)) # add all files of menu
        file_names.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])

# add all file names of drawable
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/drawable'):
    # add path to all file names.
    for filename in filenames:
        files.add(os.path.join(dirname, filename)) # add all files of drawable
        file_names.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])

# add all file names of drawable hdpi
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/drawable-hdpi'):
    # add path to all file names.
    for filename in filenames:
        file_names.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])
        file_names_in_hdpi.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])

# add all file names of drawable xhdpi
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/drawable-xhdpi'):
    # add path to all file names.
    for filename in filenames:
        file_names.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])
        file_names_in_xhdpi.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])

# add all files of layout
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/layout'):
    for filename in filenames:
        files.add(os.path.join(dirname, filename))

# add all files of java
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/java/com/touchtalent/bobbleapp'):
    for filename in filenames:
        files.add(os.path.join(dirname, filename))

files.add(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/raw/seed.json')

# take a file name one by one and search in drawable, layout and java one by one
for file_name in file_names:
    file_is_used = False
    for file in files:
        with open(file, 'r') as opened_file:
            for line in opened_file:
               if file_name in line:
                 file_is_used = True
    if not file_is_used:
        files_not_used.add(file_name)

# print the file which are not used
print('-----------------------------------------------------------------------------')
print('files which are not used :')
for file_not_used in files_not_used:
    print(file_not_used)

# for files present in hdpi but not in xhdpi
print('-----------------------------------------------------------------------------')
print('files present in hdpi but not in xhdpi :')
files_extra_in_hdpi = file_names_in_hdpi.difference(file_names_in_xhdpi)
for file_extra_in_hdpi in files_extra_in_hdpi:
    print(file_extra_in_hdpi)


# for files present in xhdpi but not in hdpi
print('-----------------------------------------------------------------------------')
print('files present in xhdpi but not in hdpi :')
files_extra_in_xhdpi = file_names_in_xhdpi.difference(file_names_in_hdpi)
for file_extra_in_xhdpi in files_extra_in_xhdpi:
    print(file_extra_in_xhdpi)

# files that are only present in hdpi and being used
print('-----------------------------------------------------------------------------')
print('files that are only present in hdpi and being used :')
files_extra_in_hdpi_being_used = files_extra_in_hdpi.difference(files_not_used)
for file_extra_in_hdpi_being_used in files_extra_in_hdpi_being_used:
    print(file_extra_in_hdpi_being_used)

# files that are only present in xhdpi and being used
print('-----------------------------------------------------------------------------')
print('files that are only present in xhdpi and being used :')
files_extra_in_xhdpi_being_used = files_extra_in_xhdpi.difference(files_not_used)
for file_extra_in_xhdpi_being_used in files_extra_in_xhdpi_being_used:
    print(file_extra_in_xhdpi_being_used)