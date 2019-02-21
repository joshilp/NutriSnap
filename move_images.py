import os

dir_path = os.path.dirname(os.path.realpath(__file__))
new_path = dir_path + "\\food41\\test"
dir_path += "\\food41\\train"
num_text_files = 250
curr_count = 0
for subdir in os.listdir(dir_path):
    for file in os.listdir(os.path.join(dir_path, subdir)):
        if not (os.path.exists(os.path.join(new_path, subdir))):
            os.mkdir(os.path.join(new_path, subdir))
        #print(os.path.join(new_path, subdir, file))
        if (not os.path.exists(os.path.join(new_path, subdir, file))) and curr_count < num_text_files:
            os.rename(os.path.join(dir_path, subdir, file), os.path.join(new_path, subdir, file))
            curr_count += 1
    curr_count = 0