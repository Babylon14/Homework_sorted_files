import os

file_directory = os.path.dirname(os.path.abspath(__file__))

file_path_1 = os.path.join(file_directory, "1.txt")
file_path_2 = os.path.join(file_directory, "2.txt")
file_path_3 = os.path.join(file_directory, "3.txt")


result_file_info = []

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
        return lines, len(lines)
    
text_file_1, length_file_1 = read_file(file_path_1)
text_file_2, length_file_2 = read_file(file_path_2)
text_file_3, length_file_3 = read_file(file_path_3)

result_file_info.append((os.path.basename(file_path_1), length_file_1, *text_file_1))
result_file_info.append((os.path.basename(file_path_2), length_file_2, *text_file_2))
result_file_info.append((os.path.basename(file_path_3), length_file_3, *text_file_3))

result_file_info.sort(key=lambda x: x[1])

for file_info in result_file_info:
    print("=" * 80)
    for info in file_info:
        print(info)
