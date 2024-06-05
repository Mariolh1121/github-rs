from Bio import SeqIO


def codons_frame(frame_val, seq):
    if frame_val > 3:
        sequence = seq.reverse_complement()
        frame = frame_val - 3
    else:
        sequence = seq
        frame = frame_val
    codons = [str(sequence[i: i + 3]) for i in range((frame - 1), len(sequence), 3) if len(sequence[i: i + 3]) == 3] 
    return " ".join(codons)

              
id_list = list(SeqIO.parse("queso\seq.nt.fa", "fasta"))

frames = [1, 2, 3, 4, 5, 6]
file_names = ['fasta1', 'fasta2', 'fasta3', 'fasta4', 'fasta5', 'fasta6']

for frame, file_name in zip(frames, file_names):
    with open(file_name, 'w') as file:
        for i in range(len(id_list)):
            id = id_list[i].id
            sequence = id_list[i].seq
            codones = codons_frame(frame, sequence)
            file.write(f">{id}\n")
            file.write(f"{codones}\n")
