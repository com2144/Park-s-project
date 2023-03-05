import glob
import re
import os

class Re_path:
    def __init__(self):
        self._project_path = ''
        self.my_list = []
    
    @property
    def project_path(self):
        return self._project_path

    @project_path.setter
    def project_path(self, path):
        self._project_path = path
     
    def path_edit(self):
        for roots, dirs, files in os.walk(self.project_path):
            for dir in dirs:
                file_paths = os.path.join(roots, dir)
                file_list = glob.glob(file_paths + '/*.jpg')
                if file_list:
                    frame = len(file_list)
                    info = {"project name":None,
                            "seq name":None,
                            'shot name':None,
                            'version':None,
                            'frame':None,
                            'path':None} 
                    mat_path = re.search(self.project_path + '/(\w+)/shot/(\w+)/(\w+)/plate/(\w+)',file_paths)
                    if mat_path:
                        info["project name"] = mat_path.group(1)
                        info["seq name"] = mat_path.group(2)
                        info["shot name"] = mat_path.group(3)
                        info["version"] = mat_path.group(4)
                        info["frame"] = frame
                        info["path"] = file_paths
                        self.my_list.append(info)
                else:
                    print('path is None')

def main():
    t = Re_path()
    t.project_path = '/home/rapa/project'
    t.path_edit()
    
if __name__ == '__main__':
    main()