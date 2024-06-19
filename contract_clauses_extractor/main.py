import os
from src.extract_clauses import main as extract_clauses_main
from src.convert_to_csv import main as convert_to_csv_main
from src.compare_contracts import main as compare_contracts_main

def main():
    print("Step 1: Extract Clauses and Labels from Template Contract")
    extract_clauses_main(os.path.join('input', 'contract_template.txt'), os.path.join('output', 'template_clauses.txt'))

    print("\nStep 2: Extract Clauses and Labels from Example Contract")
    extract_clauses_main(os.path.join('input', 'example_contract.txt'), os.path.join('output', 'example_clauses.txt'))

    print("\nStep 3: Convert Template Clauses to CSV")
    convert_to_csv_main(os.path.join('output', 'template_clauses.txt'), os.path.join('output', 'contract_clauses.csv'))

    print("\nStep 4: Compare Example Contract to Template")
    compare_contracts_main()

if __name__ == "__main__":
    main()
