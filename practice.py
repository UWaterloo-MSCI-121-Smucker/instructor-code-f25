
def get_matrix(filename):
    infile = open(filename, "r")
    matrix = list()
    num_rows = int(infile.readline())
    num_cols = int(infile.readline())
    line = infile.readline()
    while line != "":
        str_values = line.strip().split()
        row = list()
        for elt in str_values:
            row.append(float(elt))
        matrix.append(row)
        line = infile.readline()

    infile.close()
    return matrix
 

def sum_matrices(m1, m2):
    pass

def main():
    matrix = get_matrix("matrix.txt")
    two_times = sum_matrices(matrix, matrix)

if __name__ == "__main__":
    main()
    