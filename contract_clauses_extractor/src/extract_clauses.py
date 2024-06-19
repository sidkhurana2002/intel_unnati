import os

def read_contract(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def extract_clauses(contract_text):
    labels = {
        "Agreement Details": ["Agreement, dated as of"],
        "Purpose": ["WHEREAS"],
        "Consideration": ["FOR GOOD AND VALUABLE CONSIDERATION"],
        "Confidential Information": ["proprietary and commercially sensitive information", "confidential"],
        "Definition of Information": ["The term \"Information\" shall mean"],
        "Duration of Confidentiality": ["secrecy and confidence for a period of"],
        "Third-Party Disclosure": ["not disclose Information to these individuals without obtaining prior written approval"],
        "Legal Disclosure": ["disclose Information as required by a governmental body"],
        "Severability": ["If any provision of this Agreement is or becomes or is deemed invalid"],
        "Governing Law": ["governed by and construed and enforced in accordance with the laws"],
        "Counterparts": ["executed in any number of counterparts"],
        "Notices": ["All notices from GSEnergy hereunder"]
    }

    clauses = []
    current_label = None

    lines = contract_text.split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        for label, keywords in labels.items():
            if any(keyword in line for keyword in keywords):
                current_label = label
                break
        
        if current_label:
            clauses.append((line, current_label))
    
    return clauses

def save_clauses(clauses, output_path):
    with open(output_path, 'w') as file:
        for clause, label in clauses:
            file.write(f"{clause}\t{label}\n")

def main(input_file, output_file):
    contract_text = read_contract(input_file)
    clauses = extract_clauses(contract_text)
    save_clauses(clauses, output_file)
    print(f"Clauses and labels saved to {output_file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python extract_clauses.py <input_file> <output_file>")
    else:
        main(sys.argv[1], sys.argv[2])
