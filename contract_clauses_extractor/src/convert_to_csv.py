import pandas as pd
import os

def load_clauses(input_path):
    clauses = []
    with open(input_path, 'r') as file:
        for line in file:
            clause, label = line.strip().split('\t')
            clauses.append((clause, label))
    return clauses

def convert_to_csv(clauses, output_csv_path):
    df = pd.DataFrame(clauses, columns=['Clause', 'Label'])
    df.to_csv(output_csv_path, index=False)
    print(f"CSV file saved to {output_csv_path}")

def main(input_file, output_file):
    clauses = load_clauses(input_file)
    convert_to_csv(clauses, output_file)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python convert_to_csv.py <input_file> <output_file>")
    else:
        main(sys.argv[1], sys.argv[2])
