import os

file_directory = os.path.dirname(os.path.abspath(__file__))

file_path_1 = os.path.join(file_directory, "1.txt")
file_path_2 = os.path.join(file_directory, "2.txt")
file_path_3 = os.path.join(file_directory, "3.txt")

with open(file_path_1, "r", encoding="utf-8") as file_1, \
    open(file_path_2, "r", encoding="utf-8") as file_2, \
    open(file_path_3, "r", encoding="utf-8") as file_3:
    pass
    
