__author__ = 'tian.du'


def read_file():
    line_counter = 0
    file_handle = open("test.txt", "r")

    f_counter = 0
    m_counter = 0

    for line in file_handle:
        line = line.strip()
        print(line)
        line_counter += 1

        second_char = line.split(",")[1]

        if second_char == "F":
           f_counter += 1
        elif second_char == "M":
            m_counter += 1

    print("")
    print("F: " + str(f_counter))
    print("M: " + str(m_counter))
    print("Total: " + str(line_counter))
    # always close the file
    file_handle.close(line_counter)


if __name__ == "__main__":
    read_file()
