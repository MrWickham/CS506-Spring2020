
def read_csv(csv_file_path):
    import csv
    """
    Given a path to a csv file
    Read data from csv file
    Convert data into its original data type
    return a matrix
    """
    # raise NotImplementedError()
    result = []
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            row = [int(i) for i in row]
            result.append(row)
    return result

    
    '''
    for line in lines:
        # res.append([int(x) for x in line.split(",")])

        # res.append([eval(x) for x in line.split(",")])

    '''
    # res = []
    # with open(csv_file_path, "r") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         row = []
    #         for x in line.split(","):
    #             row.append(eval(x))
    #         res.append(row)

    # return res

