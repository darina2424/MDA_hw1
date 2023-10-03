
input_file = "C:\genes\новая\contigs_5000.fasta"
output_files = {
    ">NODE_1": "output1.fasta",
    ">NODE_2": "output2.fasta",
    ">NODE_3": "output3.fasta",
    ">NODE_4": "output4.fasta"
}


with open(input_file, "r") as infile:
    current_output_file = None

    # Проход по строкам
    for line in infile:
        if line.startswith(">"):
            # Проверяем соотвествие
            for param, output_name in output_files.items():
                if line.startswith(param):

                    if current_output_file:
                        current_output_file.close()
                    current_output_file = open(output_name, "a")
                    break
        if current_output_file:

            current_output_file.write(line)


if current_output_file:
    current_output_file.close()