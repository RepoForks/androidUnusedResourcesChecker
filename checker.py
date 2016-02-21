import os

ROOT_DIRECTORY = '/Users/amitshekhar/Documents/Development/Bobble'

# all file name list
file_names = set()
file_names_in_hdpi = set()
file_names_in_xhdpi = set()

# all files list
files = set()


# add all file names in menu
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/menu'):
    # add path to all file names.
    for filename in filenames:
        files.add(os.path.join(dirname, filename)) # add all files of menu
        file_names.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])

# add all file names in drawable
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/drawable'):
    # add path to all file names.
    for filename in filenames:
        files.add(os.path.join(dirname, filename)) # add all files of drawable
        file_names.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])

# add all file names in drawable hdpi
for dirname, dirnames, filenames in os.walk(ROOT_DIRECTORY+'/comic-book/ComicBook/app/src/main/res/drawable-hdpi'):
    # add path to all file names.
    for filename in filenames:
        file_names.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])
        file_names_in_hdpi.add(os.path.splitext(os.path.basename(os.path.join(dirname, filename)))[0])

# add all file names in drawable xhdpi
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
    file_is_present = False
    for file in files:
        with open(file, 'r') as opened_file:
            for line in opened_file:
               if file_name in line:
                 file_is_present = True
    if not file_is_present:
        print(file_name)

# for files present in hdpi but not in xhdpi
print('-----------------------------------------------------------------------------')
print('files present in hdpi but not in xhdpi :')
print(file_names_in_hdpi.difference(file_names_in_xhdpi))


# for files present in xhdpi but not in hdpi
print('-----------------------------------------------------------------------------')
print('files present in xhdpi but not in hdpi :')
print(file_names_in_xhdpi.difference(file_names_in_hdpi))