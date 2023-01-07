import os
import sys
import subprocess

def find_duplicate_file_path(filename):
    result = []
    search_path = os.path.dirname(os.path.realpath(__file__))
    for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
    return result


if __name__ == '__main__':
    length = len(sys.argv);
    if(length == 1):
        print("Error: please do add file name")
    else:
        duplicateFilePaths = find_duplicate_file_path(sys.argv[1])
        if(len(duplicateFilePaths) == 1):
            print(f"No duplicate Files are found for {sys.argv[1]}")
        else:
            for path in duplicateFilePaths:
                output = subprocess.check_output(f'cmd /c "git log -1 --pretty="format:%ci" {path}"', shell=True)
                if(len(output) > 0):
                    print(f'Existing file path {path} - uploaded datetime {str(output)}')
                else:
                    print(f'Duplicate File path - {path}')

