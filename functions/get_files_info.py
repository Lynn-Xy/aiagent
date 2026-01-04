import os

def get_files_info(working_directory, directory="."):
    try:
        absPath = os.path.abspath(working_directory)
        targetDir = os.path.normpath(os.path.join(absPath, directory))
        commonPath = os.path.commonpath([absPath, targetDir])
        if commonPath != absPath:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            if not os.path.isdir(targetDir):
                return f'Error: "{directory}" is not a directory'
            contents = ""
            for file in os.listdir(targetDir):
                name = file
                fileSize = os.path.getsize(os.path.join(targetDir, file))
                isDir = os.path.isdir(os.path.join(targetDir, file))
                contents += f"- {name}: file_size={fileSize} bytes, is_dir={isDir}\n"
            return contents
    except Exception as e:
        return f"Error: {e}"