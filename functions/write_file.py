import os, io

def write_file(working_directory, file_path, content):
    try:
        absPath = os.path.abspath(working_directory)
        targetFile = os.path.normpath(os.path.join(absPath, file_path))
        commonPath = os.path.commonpath([absPath, targetFile])
        if commonPath != absPath:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        else:
            if os.path.isdir(targetFile):
                return f'Error: Cannot write to "{file_path}" as it is a directory'
            dirName = os.path.dirname(targetFile)
            if not os.path.exists(dirName):
                os.makedirs(dirName, exist_ok=True)
            file = open(targetFile, 'w')
            file.write(content)
            file.close()
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"