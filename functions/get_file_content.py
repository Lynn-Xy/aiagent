import os, io
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["file_path"],
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
    ),
)