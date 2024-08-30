import os, glob, shutil

def make_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def copy_dir(source_dir, dest_dir):
    for filename in glob.glob(os.path.join(source_dir, '*.*')):
        shutil.copy(filename, dest_dir)

count = 2 # count item
while count < 3: 
    make_dir("/[To]"+str(count))
    copy_dir("/[From]", "/[To]" +str(count)) 
    count = count + 1