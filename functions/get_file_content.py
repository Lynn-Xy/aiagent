import os, io

def get_file_content(working_directory, file_path):
    try:
        absPath = os.path.abspath(working_directory)
        targetFile = os.path.normpath(os.path.join(absPath, file_path))
        commonPath = os.path.commonpath([absPath, targetFile])
        if commonPath != absPath:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        else:
            if not os.path.isfile(targetFile):
                return f'Error: File not found or is not a regular file: "{file_path}"'
            file = open(targetFile)
            content = file.read(10000)
            contentCont = file.read(10001)
            if len(contentCont) > len(content):
                content += f'[...File "{file_path}" truncated at 10000 characters]'
            file.close()
            return content
    except Exception as e:
        return f"Error: {e}"