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

        '''
        for line in lines:
            # res.append([int(x) for x in line.split(",")])

            # res.append([eval(x) for x in line.split(",")])

        '''

    return result