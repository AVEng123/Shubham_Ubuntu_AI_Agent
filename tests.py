from functions.get_files_info import get_files_info

def main():
    working_directory = "calculator"
    root_contents = get_files_info(working_directory)
    print("Contents of the root directory:")
    print(root_contents)
    pkg_contents = get_files_info(working_directory, "calculator/pkg")
    print("Contents of the calculator/pkg directory:")
    print(pkg_contents)
    bin_contents = get_files_info(working_directory, "/bin")
    print("Contents of the /bin directory:")
    print(bin_contents)
    
    
    
if __name__ == "__main__":
    main()