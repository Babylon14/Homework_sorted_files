import os

file_directory = os.path.dirname(os.path.abspath(__file__))

result_file_info = []
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
        return lines, len(lines)
    
for filename in os.listdir(file_directory):
    file_path = os.path.join(file_directory, filename)

    if os.path.isfile(file_path) and filename.endswith(".txt"):
        text_file, length_file = read_file(file_path)
        result_file_info.append((filename, length_file, *text_file))

result_file_info.sort(key=lambda x: x[1])

for file_info in result_file_info:
    print("=" * 80)
    for info in file_info:
        print(info)
