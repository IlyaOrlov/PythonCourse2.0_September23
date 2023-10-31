def copy_file(source, destination):
    try:
        with open(source, 'r') as f_src:
            data = f_src.read()

        with open(destination, 'x') as f_dest:
            f_dest.write(data)
    except (FileNotFoundError, FileExistsError) as e:
        print(e)


source_file = "file1.txt"
destination_file_valid = "file2.txt"

copy_file(source_file, destination_file_valid)
