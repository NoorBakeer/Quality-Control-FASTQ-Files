from FastqReporter import FastqReporter
from FASTQReader import FASTQReader


def best_fastq_file(r1, r2, r3):
    best = r1
    if r2.get_number_of_reads_with_Ns() < best.get_number_of_reads_with_Ns():
        best = r2
    if r3.get_number_of_reads_with_Ns() < best.get_number_of_reads_with_Ns():
        best = r3
    return best


if __name__ == '__main__':
    first_archive = input()
    second_archive = input()
    third_archive = input()

    reporter1 = FastqReporter()
    reporter2 = FastqReporter()
    reporter3 = FastqReporter()
    reader = FASTQReader()

    reader.set_path(first_archive)
    reader.extract_sequences()
    reporter1.analyze_fastq_file(reader.get_sequences())

    reader.set_path(second_archive)
    reader.extract_sequences()
    reporter2.analyze_fastq_file(reader.get_sequences())

    reader.set_path(third_archive)
    reader.extract_sequences()
    reporter3.analyze_fastq_file(reader.get_sequences())

    best_file = best_fastq_file(reporter1, reporter2, reporter3)

    best_file.print_report()
