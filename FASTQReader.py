import gzip


class FASTQReader:
    def __init__(self):
        self.archive = ""
        self.sequences = list()
        self.no_of_reads = 0

    def set_path(self, path):
        self.archive = path

    def extract_sequences(self):
        with gzip.open(self.archive, "rt", encoding="utf-8") as fastq_file:
            lines = fastq_file.read().split("\n")

            for i in range(1, len(lines), 4):
                self.sequences.append(lines[i].strip())

    def get_sequences(self):
        return self.sequences
