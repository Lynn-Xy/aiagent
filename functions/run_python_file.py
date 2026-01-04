import os, io, subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        absPath = os.path.abspath(working_directory)
        targetFile = os.path.normpath(os.path.join(absPath, file_path))
        commonPath = os.path.commonpath([absPath, targetFile])
        if commonPath != absPath:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        else:
            if not os.path.isfile(targetFile):
                return f'Error: "{file_path}" does not exist or is not a regular file'
            if not targetFile.endswith('.py'):
                return f'Error: "{file_path}" is not a Python file'
            command = ['python', targetFile]
            if args:
                command.extend(args)
            result = subprocess.run(command, capture_output=True, text=True, cwd=absPath, timeout=30)

            output = ''
            if result.returncode != 0:
                output += f'Process exited with code {result.returncode}\n'
            if result.stdout == '' and result.stderr == '':
                output += "No output produced"
            if result.stdout:
                output += f'STDOUT:\n{result.stdout}\n'
            if result.stderr:
                output += f'STDERR:\n{result.stderr}\n'
            
            return output
    except Exception as e:
        return f"Error: executing Python file: {e}"