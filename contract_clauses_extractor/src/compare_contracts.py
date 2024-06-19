import os
import pandas as pd
import re

def load_clauses(input_path):
    clauses = []
    with open(input_path, 'r') as file:
        for line in file:
            clause, label = line.strip().split('\t')
            clauses.append((clause, label))
    return clauses

def find_inconsistencies(template_text, example_text, label):
    if template_text == example_text:
        return None
    
    if label == "Agreement Details":
        template_date_match = re.search(r'\b\d{4}\b', template_text)
        example_date_match = re.search(r'\b\d{4}\b', example_text)
        if template_date_match and example_date_match:
            template_date = template_date_match.group()
            example_date = example_date_match.group()
            if template_date != example_date:
                return f"Date of Agreement: Changed from {template_date} to {example_date}."

        template_company_match = re.search(r'("Company"\))', template_text)
        example_company_match = re.search(r'("Company"\))', example_text)
        if template_company_match and example_company_match:
            template_company = template_company_match.group()
            example_company = example_company_match.group()
            if template_company != example_company:
                return f"Company Name: Changed from {template_company} to {example_company}."

    elif label == "Purpose":
        template_program_match = re.search(r'\(([^)]+)\)', template_text)
        example_program_match = re.search(r'\(([^)]+)\)', example_text)
        if template_program_match and example_program_match:
            template_program = template_program_match.group()
            example_program = example_program_match.group()
            if template_program != example_program:
                return f"Program Name: Changed from {template_program} to {example_program}."

    elif label == "Confidential Information":
        template_confidentiality_period_match = re.search(r'\b\d{1,2}\b', template_text)
        example_confidentiality_period_match = re.search(r'\b\d{1,2}\b', example_text)
        if template_confidentiality_period_match and example_confidentiality_period_match:
            template_confidentiality_period = template_confidentiality_period_match.group()
            example_confidentiality_period = example_confidentiality_period_match.group()
            if template_confidentiality_period != example_confidentiality_period:
                return f"Confidentiality period: Changed from {template_confidentiality_period} years to {example_confidentiality_period} years."

    elif label == "Governing Law":
        template_law_match = re.search(r'Commonwealth of [^\s]+', template_text)
        example_law_match = re.search(r'State of [^\s]+', example_text)
        if template_law_match and example_law_match:
            template_law = template_law_match.group()
            example_law = example_law_match.group()
            if template_law != example_law:
                return f"Governing Law: Changed from {template_law} to {example_law}."

    return f"Clause '{label}': Content changed."

def compare_contracts(template_clauses, example_clauses):
    inconsistencies = []

    template_dict = {label: clause for clause, label in template_clauses}
    example_dict = {label: clause for clause, label in example_clauses}

    for label in template_dict.keys():
        if label not in example_dict:
            inconsistencies.append((label, "Missing clause in example contract"))
        else:
            inconsistency = find_inconsistencies(template_dict[label], example_dict[label], label)
            if inconsistency:
                inconsistencies.append((label, inconsistency))

    for label in example_dict.keys():
        if label not in template_dict:
            inconsistencies.append((label, "Unexpected clause in example contract"))

    return inconsistencies

def save_inconsistencies(inconsistencies, output_path):
    with open(output_path, 'w') as file:
        for label, issue in inconsistencies:
            file.write(f"{label}: {issue}\n")

def main():
    template_path = os.path.join('output', 'template_clauses.txt')
    example_path = os.path.join('output', 'example_clauses.txt')
    output_path = os.path.join('output', 'inconsistencies_report.txt')

    template_clauses = load_clauses(template_path)
    example_clauses = load_clauses(example_path)

    inconsistencies = compare_contracts(template_clauses, example_clauses)
    save_inconsistencies(inconsistencies, output_path)

    print(f"Inconsistencies report saved to {output_path}")

if __name__ == "__main__":
    main()
