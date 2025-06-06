scores_files = [f'output_scores_1_r{n}.txt' for n in range(1, 7)]
mask_file = 'output_original_1.txt'

scores = []
original_values = []

for n in range (1, 7):
    scores_file = scores_files[n - 1]
    with open(scores_file, "r") as score_file:
        scores = score_file.readlines()

    with open(mask_file, "r") as score_file:
        original_values = score_file.readlines()

    value_indices = {}
    for index, value in enumerate(original_values):
        value = value.strip()
        if value in value_indices:
            value_indices[value].append(index)
        else:
            value_indices[value] = [index]

    result = [(value, indices) for value, indices in value_indices.items()]

    averages = []
    for value, indices in result:
        total = sum(float(scores[i].strip()) for i in indices)
        average = total / len(indices)
        averages.append((value, average))

    with open(f"output_averages_1_r{n}.txt", "w") as output_file:
        for value, average in averages:
            output_file.write(f"{average}\n")