# ------------------------------------------------------------------------------
# Program: DNA FASTA Generator with Statistics and Metadata
# Author: [Your Name]
# Description:
#     This Python program generates a random DNA nucleotide sequence of user-defined length,
#     inserts a user's name at a random location (excluded from statistics),
#     and saves the final sequence in a valid FASTA file format.
#     It also prints sequence statistics (A, C, G, T percentages, CG ratio).
#
# Context:
#     Useful in education, biology labs, and testing bioinformatics tools with synthetic data.
#     The script can be run in Python development environments like VS Code or Thonny.
# ------------------------------------------------------------------------------

import random  # To generate random DNA sequences and positions
import os      # To check if output file already exists

# Function to generate a random DNA sequence composed of A, C, G, and T
def generate_dna_sequence(length):
    return ''.join(random.choices('ACGT', k=length))

# Function to insert the user's name at a random position in the sequence
def insert_name(sequence, name):
    position = random.randint(0, len(sequence))
    return sequence[:position] + name + sequence[position:]

# Function to calculate and return nucleotide statistics and %CG ratio
def calculate_statistics(sequence, name):
    # Remove the inserted name before calculating stats
    cleaned_sequence = sequence.replace(name, "")
    total = len(cleaned_sequence)

    # Count each nucleotide and calculate its percentage
    stats = {
        'A': cleaned_sequence.count('A') / total * 100,
        'C': cleaned_sequence.count('C') / total * 100,
        'G': cleaned_sequence.count('G') / total * 100,
        'T': cleaned_sequence.count('T') / total * 100
    }

    # Calculate percentage of C and G combined
    cg_ratio = stats['C'] + stats['G']
    return stats, cg_ratio

# ORIGINAL:
# def save_to_fasta(file_name, seq_id, description, sequence):
#     with open(file_name, 'w') as file:
#         file.write(f">{seq_id} {description}\n")
#         file.write(sequence + "\n")

# MODIFIED (Improvement: line wrapping every 80 characters as per FASTA format standard):
# Justification: Bioinformatics tools expect FASTA sequences to be wrapped for readability and compatibility.
def save_to_fasta(file_name, seq_id, description, sequence):
    with open(file_name, 'w') as file:
        file.write(f">{seq_id} {description}\n")
        for i in range(0, len(sequence), 80):
            file.write(sequence[i:i+80] + "\n")

# ORIGINAL:
# length = int(input("Enter the sequence length: "))

# MODIFIED (Improvement: input validation for positive integer)
# Justification: Prevents crashes due to invalid or negative input.
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main function to control program flow
def main():
    # Ask user for sequence length and validate input
    length = get_positive_integer("Enter the sequence length: ")

    # Ask user for sequence ID (used in FASTA file and header)
    seq_id = input("Enter the sequence ID: ").strip()

    # ORIGINAL:
    # description = input("Provide a description of the sequence: ")
    # MODIFIED (Improvement: strip input to remove whitespace)
    # Justification: Clean input ensures formatting consistency in FASTA header.
    description = input("Provide a description of the sequence: ").strip()

    # Ask user for their name to be inserted in the sequence (not counted in stats)
    name = input("Enter your name: ").strip()

    # Generate base DNA sequence and insert the name
    dna = generate_dna_sequence(length)
    dna_with_name = insert_name(dna, name)

    # Calculate stats from sequence without name
    stats, cg_ratio = calculate_statistics(dna_with_name, name)

    # Define FASTA output file name
    file_name = f"{seq_id}.fasta"

    # MODIFIED (Improvement: warn user if file already exists)
    # Justification: Prevents silent overwriting of existing data files
    if os.path.exists(file_name):
        print(f"Warning: File {file_name} already exists and will be overwritten.")

    # Save sequence to FASTA file
    save_to_fasta(file_name, seq_id, description, dna_with_name)

    # Output results to user
    print(f"\nThe sequence was saved to the file {file_name}")
    print("Sequence statistics:")
    for nucleotide in ['A', 'C', 'G', 'T']:
        print(f"{nucleotide}: {stats[nucleotide]:.1f}%")
    print(f"%CG: {cg_ratio:.1f}")

# Entry point of the script
if __name__ == "__main__":
    main()
