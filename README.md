# SMS Clustering with K-Means

This project is a tool for evaluating the ability of the k-means clustering algorithm to classify short message (SMS) contents as either spam or ham (non-spam) messages.

## Dataset

The dataset contains text message contents with tags indicating whether each message is spam or ham. The tool prepares a dataset file named `smsdata.txt` for clustering.

## Usage

1. Run the `sms_clustering.py` script.
2. Enter the number of clusters (k value) when prompted.
3. View the clustering results, including the total number of messages and the spam and ham percentages in each cluster.

## Instructions

- The program reads the data from the file and parses its contents.
- The tool generates a dataset file (`smsdata.txt`) similar to the "blogdata.txt" file used in class.
- Each row corresponds to a specific short message, and each column corresponds to a word.
- Non-alphanumeric characters are removed, and unnecessary words are eliminated.
- The category information (spam or ham) is not included in the output file.

## Evaluation

- Ideally, all spam messages should be grouped in one cluster, and ham messages should be grouped in the other.
- Displayed results show the total number of messages and spam and ham message percentages in each cluster.

## Notes

- The dataset is not provided; users should create their own list if they want to use the tool with a different dataset.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
