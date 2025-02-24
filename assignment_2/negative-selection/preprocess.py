test_file_paths = [f"syscalls/snd-cert/snd-cert.{n}.test" for n in range(1,4)]
labels_file_paths = [f"syscalls/snd-cert/snd-cert.{n}.labels" for n in range(1,4)]

zipped_labels = []

for path in range(len(test_file_paths)):
    with open(test_file_paths[path], "r") as test_file:
        test_lines = test_file.readlines()

    with open(labels_file_paths[path], "r") as labels_file:
        labels = labels_file.readlines()

    data = [(line.strip(), labels[i].strip()) for i, line in enumerate(test_lines)]
    zipped_labels.append(data)

def split_string(string, N = 7):
    result = []
    for i in range(0, len(string), N):
        result.append(string[i:i+N])

    if len(result[-1]) < N:
        result.pop()
    return result

for zipped_label in zipped_labels:
    for i, (line, label) in enumerate(zipped_label):
        zipped_label[i] = (split_string(line, 7), label)

for id, zipped_label in enumerate(zipped_labels):
    with open(f"output_strings_{id}.txt", "w") as strings_file, open(f"output_labels_{id}.txt", "w") as labels_file:
        for strings, label in zipped_label:
            for string in strings:
                strings_file.write(f"{string}\n")
                labels_file.write(f"{label}\n")