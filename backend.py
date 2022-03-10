import csv




with open('backend-data/sample_addresses.csv', 'r') as f:
    rows = csv.reader(f, delimiter=',')

    with open('output.csv', 'w+') as f_out:
        writer = csv.writer(f_out, delimiter=',')
        for row in rows:
            print(''.join(row))
            # print(row)
            writer.writerow([''.join(row)])

        f_out.close()
    f.close()