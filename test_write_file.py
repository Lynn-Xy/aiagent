from functions.write_file import write_file

def test_write_file():
    result1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"{result1}")
    result2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"{result2}")
    result3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed.")
    print(f"{result3}")

if __name__ == "__main__":
    test_write_file()