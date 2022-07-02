def read_data(load_file_path):
    # reads the data from the file in the path
    read_list = list()
    for line in open(load_file_path):
        csv_row = line.split()
        read_list.append(csv_row)
    lt = list()
    for i in read_list:
        lt.append(i[0].split(","))
    return lt

