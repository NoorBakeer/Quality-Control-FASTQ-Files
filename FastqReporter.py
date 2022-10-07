from statistics import mean


class FastqReporter:
    def __init__(self):
        self.reads_counter_dict = dict()
        self.unique_sequences: set[str] = set()
        self.number_of_repeats = 0
        self.Ns_percentages_record = list()
        self.reads_with_N_counter = 0
        self.gc_levels = list()
        self.number_of_reads = 0
        self.sequence = ""

    def count_reads(self, seq_length):
        self.reads_counter_dict.setdefault(seq_length, 0)
        self.reads_counter_dict[seq_length] += 1

    def count_repeated_reads(self):
        if self.sequence in self.unique_sequences:
            self.number_of_repeats += 1
        else:
            self.unique_sequences.add(self.sequence)

    def calculate_Ns_percentage(self):
        self.reads_with_N_counter += 1
        Ns_percentage = (self.sequence.count('N') / len(self.sequence)) * 100
        self.Ns_percentages_record.append(round(Ns_percentage, 2))

    def get_reads_no(self):
        return

    def calculate_gc_content(self):
        gc_counter = 0
        other_nucleotides = 0
        for nucleotide in self.sequence:
            if nucleotide == 'C' or nucleotide == 'G':
                gc_counter += 1
            else:
                other_nucleotides += 1
        gc_average = (gc_counter / (other_nucleotides + gc_counter)) * 100
        return round(gc_average, 2)

    def record_gc_content(self):
        self.gc_levels.append(self.calculate_gc_content())

    def calculate_avg_read_length(self):
        total = 0
        for item in self.reads_counter_dict:
            total += (item * self.reads_counter_dict[item])

        avg_length = round(total / self.number_of_reads)
        return avg_length

    def mean_of_all_averages(self):
        return round(mean(self.gc_levels), 2)

    def mean_of_all_Ns_percentages(self):
        return round(mean(self.Ns_percentages_record), 2)

    def get_number_of_reads_with_Ns(self):
        return self.reads_with_N_counter

    def analyze_fastq_file(self, sequences):
        self.number_of_reads = len(sequences)

        for item in sequences:
            self.sequence = item
            self.count_reads(len(item))
            self.record_gc_content()
            self.count_repeated_reads()
            if 'N' in item:
                self.calculate_Ns_percentage()

    def print_report(self):
        print(f"Reads in the file = {self.number_of_reads}:")
        print(f"Reads sequence average length = {self.calculate_avg_read_length()}"
              )
        print(f"\nRepeats = {self.number_of_repeats}")
        print(f"Reads with Ns = {self.reads_with_N_counter}")
        print(f"\nGC content average = {self.mean_of_all_averages()}%")
        print(f"Ns per read sequence = {self.mean_of_all_Ns_percentages()}%")
