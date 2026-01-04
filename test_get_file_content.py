from functions.get_file_content import get_file_content

def test_get_file_content():
    result1 = get_file_content("calculator", "lorem.txt")
    if 'truncated at 10000 characters]' in result1:
        print(f"{result1[:60]}...[truncated]")
    result2 = get_file_content("calculator", "main.py")
    print(f"{result2}")
    result3 = get_file_content("calculator", "pkg/calculator.py")
    print(f"{result3}")
    result4 = get_file_content("calculator", "/bin/cat")
    print(f"{result4}")
    result5 = get_file_content("calculator", "pkg/does_not_exist.txt")
    print(f"{result5}")

if __name__ == "__main__":
    test_get_file_content()