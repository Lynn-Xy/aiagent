from functions.run_python_file import run_python_file

def test_run_python_file():
    result1 = run_python_file("calculator", "main.py", [])
    print(f"{result1}")
    result2 = run_python_file("calculator", "pkg/calculator.py", ["3 + 5"])
    print(f"{result2}")
    result3 = run_python_file("calculator", "tests.py", [])
    print(f"{result3}")
    result4 = run_python_file("calculator", "../main.py", [])
    print(f"{result4}")
    result5 = run_python_file("calculator", "nonexistent.py", [])
    print(f"{result5}")
    result6 = run_python_file("calculator", "lorem.txt", [])
    print(f"{result6}")

if __name__ == "__main__":
    test_run_python_file()