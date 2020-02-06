def read_csv(csv_file_path):
    import csv
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    # raise NotImplementedError()
    result = []
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            row = [int(i) for i in row]
            result.append(row)

    return result