import sys
import os

def main():
    argv = sys.argv[1:]
    

    dash = [arg for arg in argv if arg.startswith('-')]
    file_paths = [arg for arg in argv if not arg.startswith('-')]
    

    for_lines = '-l' in dash
    for_words = '-w' in dash
    for_bytes = '-c' in dash

    total_lines = 0
    total_words = 0
    total_bytes = 0

    def print_output(lines, words, bytes_count, label):
        if for_lines:
            print(f"{str(lines).rjust(8)} {label}")
        elif for_words:
            print(f"{str(words).rjust(8)} {label}")
        elif for_bytes:
            print(f"{str(bytes_count).rjust(8)} {label}")
        else:
            print(f"{str(lines).rjust(8)} {str(words).rjust(8)} {str(bytes_count).rjust(8)} {label}")

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as fs:
                content = fs.read()
        except (FileNotFoundError, IsADirectoryError):
            print(f"wc: {file_path}: No file or directory exists", file=sys.stderr)
            sys.exit(1)

        lines = len(content.split('\n')) - 1
        words = 0 if content.strip() == '' else len(content.strip().split())
        bytes_count = len(content.encode('utf-8'))

        total_lines += lines
        total_words += words
        total_bytes += bytes_count

        print_output(lines, words, bytes_count, file_path)

    if len(file_paths) > 1:
        print_output(total_lines, total_words, total_bytes, "total")


if __name__ == "__main__":
    main()