# Pysis - A python project analyzer



# Usage
```bash

from pysis import analyze_folder, print_header, print_footer

def test_pysis_analysis():
    folder_path = './pysis'
    print_header()
    total_files, total_lines, avg_complexity, total_size, total_variables = analyze_folder(folder_path)
    print_footer(total_files, total_lines, avg_complexity, total_size, total_variables)

if __name__ == '__main__':
    test_pysis_analysis()
```

