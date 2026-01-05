import os, io
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory, creating directories as needed",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path", "content"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file",
            ),
        },
    ),
)