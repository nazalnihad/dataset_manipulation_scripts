import os

def process_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            modified_lines = []
            for line in lines:
                parts = line.split()
                if parts[0] != '0':
                    parts[0] = '0'
                    modified_line = ' '.join(parts)
                    modified_lines.append(modified_line)
                    print(f"Modified: {modified_line}")
                else:
                    modified_lines.append(line.strip())
            
            # Write the modified lines back to the file
            with open(file_path, 'w') as file:
                file.write('\n'.join(modified_lines) + '\n')

# Specify the directory containing the .txt files
directory_path = 'backup_data/final/labels'
process_files(directory_path)
