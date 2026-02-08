from functions.get_files_info import get_files_info
from functions.get_files_contents import get_files_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_directory = "calculator"
    
    """
    root_contents = get_files_info(working_directory)
    print("Contents of the root directory:")
    print(root_contents)
    print("Contents of each file in the root directory:")
    for content_item in root_contents.splitlines():
        item_name = content_item.split(":")[0].strip("- ").strip()
        item_path = f"{working_directory}/{item_name}"
        item_content = get_files_content(working_directory, item_path)
        print(f"Content of {item_name}:")
        print(item_content)
    print("\n")
    
    pkg_contents = get_files_info(working_directory, "calculator/pkg")
    print("Contents of the calculator/pkg directory:")
    print(pkg_contents)
    print("\n")
    bin_contents = get_files_info(working_directory, "/bin")
    print("Contents of the /bin directory:")
    print(bin_contents)
    print("\n")
   
    file_content = get_files_content(working_directory, "text.txt")
    print(file_content)
    
    file_content = get_files_content("calculator", "main.py")
    print(f"Content of main.py:\n{file_content}")
        
    file_content = get_files_content("calculator", "/bin/cat")
    print(f"Content of /bin/cat:\n{file_content}")
    
    file_content = get_files_content("calculator", "pkg/does_not_exist.py")
    print(f"Content of does_not_exist.py:\n{file_content}")
    
    
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
        
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    """
    print("----------------------------------------------------------------------")
    print(run_python_file("calculator", "main.py"))
    print("----------------------------------------------------------------------")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(f"----------------------------------------------------------------------")
    print(run_python_file("calculator", "tests.py"))
    print(f"----------------------------------------------------------------------")
    print(run_python_file("calculator", "../main.py"))
    print(f"----------------------------------------------------------------------")
    print(run_python_file("calculator", "nonexistent.py"))
    print(f"----------------------------------------------------------------------")
    print(run_python_file("calculator", "lorem.txt"))
    
    
    
if __name__ == "__main__":
    main()