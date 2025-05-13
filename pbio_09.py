import random
import os

def generate_dna_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

def insert_name(sequence, name):
    position = random.randint(0, len(sequence))
    return sequence[:position] + name + sequence[position:]

def calculate_statistics(sequence, name):
    # Remove name to analyze only nucleotides
    cleaned_sequence = sequence.replace(name, "")
    total = len(cleaned_sequence)
    stats = {
        'A': cleaned_sequence.count('A') / total * 100,
        'C': cleaned_sequence.count('C') / total * 100,
        'G': cleaned_sequence.count('G') / total * 100,
        'T': cleaned_sequence.count('T') / total * 100
    }
    cg_ratio = (stats['C'] + stats['G'])  # Percentage of C and G combined
    return stats, cg_ratio

# ORIGINAL:
# def save_to_fasta(file_name, seq_id, description, sequence):
#     with open(file_name, 'w') as file:
#         file.write(f">{seq_id} {description}\n")
#         file.write(sequence + "\n")

# MODIFIED (added line-wrapping for better readability in FASTA standard):
def save_to_fasta(file_name, seq_id, description, sequence):
    with open(file_name, 'w') as file:
        file.write(f">{seq_id} {description}\n")
        for i in range(0, len(sequence), 80):  # FASTA formatting: wrap every 80 characters
            file.write(sequence[i:i+80] + "\n")


# ORIGINAL:
# length = int(input("Enter the sequence length: "))

# MODIFIED (added validation to ensure input is a positive integer):
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    # Use validated input function
    length = get_positive_integer("Enter the sequence length: ")
    
    seq_id = input("Enter the sequence ID: ").strip()
    
    # ORIGINAL:
    # description = input("Provide a description of the sequence: ")
    # MODIFIED (strip whitespace to clean input):
    description = input("Provide a description of the sequence: ").strip()
    
    name = input("Enter your name: ").strip()

    dna = generate_dna_sequence(length)
    dna_with_name = insert_name(dna, name)

    stats, cg_ratio = calculate_statistics(dna_with_name, name)

    file_name = f"{seq_id}.fasta"
    
    # ORIGINAL:
    # save_to_fasta(file_name, seq_id, description, dna_with_name)

    # MODIFIED (check if file already exists and warn the user):
    if os.path.exists(file_name):
        print(f"Warning: File {file_name} already exists and will be overwritten.")
    save_to_fasta(file_name, seq_id, description, dna_with_name)

    print(f"\nThe sequence was saved to the file {file_name}")
    print("Sequence statistics:")
    for nucleotide in ['A', 'C', 'G', 'T']:
        print(f"{nucleotide}: {stats[nucleotide]:.1f}%")
    print(f"%CG: {cg_ratio:.1f}")

if __name__ == "__main__":
    main()
