from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

# Путь к исходному файлу FASTA
input_fasta = 'spades_scaffolds (1).fasta'

# Задайте желаемую длину контигов
target_length = 1000

# Путь к новому выходному файлу FASTA
output_fasta = 'new_file.fasta'

# Список для хранения выбранных контигов
selected_contigs = []

# Открываем входной файл и итерируемся по последовательностям
with open(input_fasta, 'r') as input_file:
    for record in SeqIO.parse(input_file, 'fasta'):
        if len(record.seq) >= target_length:
            selected_contigs.append(record)

# Записываем выбранные контиги в новый файл FASTA
with open(output_fasta, 'w') as output_file:
    SeqIO.write(selected_contigs, output_file, 'fasta')

print(f'Выделено контигов длиной {target_length} и сохранено в {output_fasta}')