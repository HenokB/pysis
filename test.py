# from pyziz.analyze import analyze_folder, print_header, print_footer
from pyziz import analyze_folder, print_header, print_footer

def test_pyziz_analysis():
    folder_path = './pyziz'
    print_header()
    total_files, total_lines, avg_complexity, total_size, total_variables = analyze_folder(folder_path)
    print_footer(total_files, total_lines, avg_complexity, total_size, total_variables)

if __name__ == '__main__':
    test_pyziz_analysis()

