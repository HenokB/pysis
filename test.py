# from pysis.analyze import analyze_folder, print_header, print_footer
from pysis import analyze_folder, print_header, print_footer

def test_pysis_analysis():
    folder_path = './pysis'
    
    # Print the header
    print_header()
    
    # Analyze the folder
    total_files, total_lines, avg_complexity, total_size, total_variables = analyze_folder(folder_path)
    
    # Print the footer with the summary
    print_footer(total_files, total_lines, avg_complexity, total_size, total_variables)

if __name__ == '__main__':
    test_pysis_analysis()
