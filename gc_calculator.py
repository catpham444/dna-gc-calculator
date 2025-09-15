def gc_content(sequence):
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return round(gc / len(sequence) * 100, 2) if len(sequence) > 0 else 0
