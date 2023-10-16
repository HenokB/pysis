import os

COLOR_MAP = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'end': '\033[0m'
}

def _print_colored_text(text, color):
    """Prints text in specified color."""
    print(f"{COLOR_MAP[color]}{text}{COLOR_MAP['end']}")

def print_header():
    """Prints the header for the analysis report."""
    _print_colored_text("Welcome to pyziz", 'blue')
    _print_colored_text("Python Code Analysis Report", 'blue')
    _print_colored_text("="*140, 'blue')

def print_footer(total_files, total_lines, avg_complexity, total_size, total_variables):
    """Prints the footer with the analysis summary."""
    _print_colored_text("="*140, 'blue')
    _print_colored_text(f"Total number of files analyzed: {total_files}", 'green')
    _print_colored_text(f"Total lines of code across all files: {total_lines}", 'green')
    _print_colored_text(f"Average complexity: {avg_complexity:.2f}", 'green')
    _print_colored_text(f"Total file size: {total_size:.2f} KB", 'green')
    _print_colored_text(f"Total number of variables: {total_variables}", 'green')
    _print_colored_text("End of Analysis", 'blue')

def analyze_file(file_path):
    """Analyzes a Python file and prints its metrics."""
    # Initialization
    num_code_lines = 0
    num_comment_lines = 0
    num_variables = 0
    todos = []
    complexity = 1  # Start with 1

    # Read file
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if line.startswith('#'):
                num_comment_lines += 1
                if 'TODO' in line or 'FIXME' in line:
                    todos.append(f"Line {line_num}: {line}")
            elif line:
                num_code_lines += 1
                num_variables += line.count('=')

            # Complexity check
            if any(keyword in line for keyword in ['if ', 'elif ', 'else ', 'for ', 'while ', 'and ', 'or ', 'case ', 'except ', 'finally ']):
                complexity += 1

    # Calculate file size
    file_size = os.path.getsize(file_path) / 1024  # Convert bytes to KB

    # Print file metrics
    print_header()
    _print_colored_text(f"{'File':<50}{'Lines of Code':<20}{'Lines of Comments':<20}{'Complexity':<20}{'File Size (KB)':<15}{'Variable Count':<15}", 'blue')
    _print_colored_text("="*140, 'blue')
    _print_colored_text(f"{file_path:<50}{num_code_lines:<20}{num_comment_lines:<20}{complexity:<20}{file_size:<15.2f}{num_variables:<15}", 'green')

    # Print TODOs
    if todos:
        _print_colored_text("TODOs/FIXMEs:", 'yellow')
        for todo in todos:
            _print_colored_text(todo, 'yellow')

    print_footer(1, num_code_lines, complexity, file_size, num_variables)  # As we're analyzing a single file, total_files is set to 1

    return num_code_lines, num_comment_lines, todos, complexity, num_variables

def analyze_folder(folder_path):
    """Analyzes all Python files in a folder and prints the report."""
    total_files = 0
    total_lines = 0
    total_complexity = 0
    total_size = 0
    total_variables = 0

    # Print table headers
    _print_colored_text(f"{'File':<50}{'Lines of Code':<20}{'Lines of Comments':<20}{'Complexity':<20}{'File Size (KB)':<15}{'Variable Count':<15}", 'blue')
    _print_colored_text("="*140, 'blue')

    # Iterate over files
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.py'):
            file_path = os.path.join(folder_path, file_name)
            num_code_lines, num_comment_lines, todos, complexity, num_variables = analyze_file(file_path)
            file_size = os.path.getsize(file_path) / 1024  # Convert bytes to KB

            # Update totals
            total_files += 1
            total_lines += num_code_lines
            total_complexity += complexity
            total_size += file_size
            total_variables += num_variables

            # Print file metrics
            _print_colored_text(f"{file_path:<50}{num_code_lines:<20}{num_comment_lines:<20}{complexity:<20}{file_size:<15.2f}{num_variables:<15}", 'green')

            # Print TODOs
            if todos:
                _print_colored_text("TODOs/FIXMEs:", 'yellow')
                for todo in todos:
                    _print_colored_text(todo, 'yellow')

    avg_complexity = total_complexity / total_files if total_files > 0 else 0

    return total_files, total_lines, avg_complexity, total_size, total_variables

