import os
import shutil


class Directory:
    def __init__(self):
        self.path = None
        self.subdirs = None

    def get_subdirs(self):
        subdirs = []
        for item in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, item)):
                continue
            else:
                subdirs.append(item)
        self.subdirs = subdirs
        return subdirs

    def subdirs_full_path(self):
        return [os.path.join(self.path, x) for x in self.subdirs]

    def get_contents(self):
        return os.listdir(self.path)

    def contents_full_path(self):
        return [os.path.join(self.path, x) for x in self.get_contents()]


def merge_folders(origin_dirs, target_dir, delete_origin=False):
    """Move contents of folders in origin_dirs to target_dir
    origin_dirs (list) : list of directory paths from where to move contents
    target_dir (list) : target directory path
    delete_origin (bool) : whether to remove origin_dirs after moving contents
    """
    for folder in origin_dirs:
        contents = os.listdir(folder)
        for c in contents:
            try:
                shutil.move(os.path.join(folder, c), target_dir)
            except shutil.Error as e:
                print(e)
        if delete_origin:
            os.rmdir(folder)
