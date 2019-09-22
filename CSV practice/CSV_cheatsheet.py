import csv

# - > open 'names.csv' and name it csv_file.
# - > than we read csv and store is in the environment
# - > we can do somethig with it, e.g. write to another file
# - > which we first open and write there stuff

# first line of csv usually works as entries in the table
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        # opening a new file, named new_names -> new_file
        # we also provide a new delimeter
        # writer method writes each line with a new delimiter
        # new file is in the same directory
        for line in csv_reader:
            csv_writer.writerow(line)

# Dictionary reader and writer - recommended

with open('names.csv', 'r') as csv_file1:
    csv_reader1 = csv.DictReader(csv_file1)

    # for line in csv_reader1:
    # print(line)
    # print(line['email'])
    # easier to acess the data, and it is visible what we are printing out
    with open('new_names.csv', 'w') as new_file1:

        fieldnames = ['last_name']
        # first row will be fieldnames
        # we specify fieldnames and delimeter
        csv_writer1 = csv.DictWriter(
            new_file1, fieldnames=fieldnames, delimiter='\t')

        csv_writer1.writeheader()
        # it is possible to delete some stuff from writing it to the new_file

        for line in csv_reader1:
            del line['email']
            del line['first_name']
            # thus we acquire only the last_name
            csv_writer1.writerow(line)
