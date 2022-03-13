import os


class lasso():

    def load(path = './', ext = '.'):
        filelist = []
        print("Loading files from " + str(path) + " of type " + str(ext) + "...")
        for (root, dirs, files) in os.walk(path):
            for file in files:
                print(file)
                if ext in file:
                    filelist.append(path+file)
                    print(str(file))
        print("Done")
        return filelist