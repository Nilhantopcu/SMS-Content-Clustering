import re
import numpy as np
from sklearn.cluster import KMeans

def getwords(text):
    words = re.compile(r'[^A-Z^a-z]+').split(text.lower())
    return [word for word in words if word]

def process_sms_data(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    word_counts = {}
    sms_data = []

    for line in lines:
        parts = line.strip().split('\t')
        label = parts[0]
        content = ' '.join(parts[1:])
        words = getwords(content)

        sms_data.append((label, words))

        for word in words:
            word_counts.setdefault(word, 0)
            word_counts[word] += 1

    word_list = [word for word, count in word_counts.items() if count > 1]

    with open(output_file, 'w') as out_file:
        out_file.write('Messages\t{}\n'.format('\t'.join(word_list)))

        for sms_label, sms_words in sms_data:
            out_file.write(sms_label)
            for word in word_list:
                count = sms_words.count(word)
                out_file.write('\t{}'.format(count))
            out_file.write('\n')

    return word_list, sms_data

def k_means_clustering(word_list, sms_data, num_clusters):
    counts_matrix = np.array([[sms_words.count(word) for word in word_list] for _, sms_words in sms_data])
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=42)
    clusters = kmeans.fit_predict(counts_matrix)
    return clusters

def evaluate_clusters(clusters, sms_data):
    total_messages = len(clusters)
    unique_clusters, counts = np.unique(clusters, return_counts=True)

    for cluster_id, count in zip(unique_clusters, counts):
        cluster_sms_data = [sms_data[i] for i in range(total_messages) if clusters[i] == cluster_id]
        spam_percentage = (sum(1 for label, _ in cluster_sms_data if label == 'spam') / count) * 100
        ham_percentage = 100 - spam_percentage

        print(f'Total number of messages in the {cluster_id + 1} cluster: {count}')
        print(f'Percentage of SPAM messages in the {cluster_id + 1} cluster: %{spam_percentage:.2f}')
        print(f'Percentage of HAM messages in the {cluster_id + 1} cluster: %{ham_percentage:.2f}\n')

if __name__ == '__main__':
    results = []

    for _ in range(5):
        word_list, sms_data = process_sms_data('SMSSpamCollection.txt', 'smsdata.txt')

        num_clusters = int(input("Enter the number of clusters: "))

        clusters = k_means_clustering(word_list, sms_data, num_clusters)
        evaluate_clusters(clusters, sms_data)

        answer = input("Do you want to run the clustering algorithm again? (yes/no): ").lower()
        if answer != 'yes':
            break
