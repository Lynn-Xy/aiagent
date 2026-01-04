from functions.get_files_info import get_files_info

def test_get_files_info():
    result1 = get_files_info("calculator", ".")
    print(f"{result1}")
    result2 = get_files_info("calculator", "pkg")
    print(f"{result2}")
    result3 = get_files_info("calculator", "../")
    print(f"{result3}")

if __name__ == "__main__":
    test_get_files_info()