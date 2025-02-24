test_file_paths = [f"syscalls/snd-cert/snd-cert.{n}.test" for n in range(1,4)]
labels_file_paths = [f"syscalls/snd-cert/snd-cert.{n}.labels" for n in range(1,4)]
train_file = "syscalls/snd-cert/snd-cert.train"

zipped_labels = []
train_lines = []

N = 7

with open (train_file, "r") as train_file:
    train_lines = train_file.readlines()

for path in range(len(test_file_paths)):
    with open(test_file_paths[path], "r") as test_file:
        test_lines = test_file.readlines()

    with open(labels_file_paths[path], "r") as labels_file:
        labels = labels_file.readlines()

    data = [(line.strip(), labels[i].strip()) for i, line in enumerate(test_lines)]
    zipped_labels.append(data)

train_labels = [0 for i in range(len(train_lines))]
zipped_train = [(line.strip(), train_labels[i]) for i, line in enumerate(train_lines)]

def split_string(string, N = 7):
    result = []
    for i in range(0, len(string), N):
        result.append(string[i:i+N])

    if len(result[-1]) < N:
        result.pop()
    return result

for zipped_label in zipped_labels:
    for i, (line, label) in enumerate(zipped_label):
        zipped_label[i] = (split_string(line, N), label)

for i, (line, label) in enumerate(zipped_train):
        zipped_train[i] = (split_string(line, N), label)

for id, zipped_label in enumerate(zipped_labels):
    with open(f"output_strings_{id}.txt", "w") as strings_file, open(f"output_labels_{id}.txt", "w") as labels_file, open(f"output_original_{id}.txt", "w") as original_file:
        for i, (strings, label) in enumerate(zipped_label):
            for string in strings:
                strings_file.write(f"{string}\n")
                labels_file.write(f"{label}\n")
                original_file.write(f"{i}\n")

with open(f"train_strings.txt", "w") as strings_file, open(f"train_labels.txt", "w") as labels_file:
    for strings, label in zipped_label:
        for string in strings:
            strings_file.write(f"{string}\n")
            labels_file.write(f"{label}\n")