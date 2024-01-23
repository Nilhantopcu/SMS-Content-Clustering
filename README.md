# SMS Clustering Tool

This Python tool is designed to evaluate the performance of the k-means clustering algorithm (with a k value of 2) as an unsupervised learning technique in correctly classifying short message (SMS) contents as either spam or ham (non-spam) messages. The project utilizes a dataset containing text messages sent and received by people living in English-speaking countries, where each message has a tag indicating whether it is perceived as a spam or ham message by the receiving person.

## Usage

1. Add your data file named `SMSSpamCollection.txt` to the directory of your project.
2. Run the project.
3. First, a data file named `smsdata.txt` will be generated, and then the k-means clustering algorithm will be executed.
4. The user will be prompted to enter the number of clusters they desire.
5. Once the k-means clustering algorithm completes, the spam and ham message percentage values for each cluster will be displayed.
6. The user will be asked if they want to rerun the algorithm.

## Requirements

- Python 3.x
- scikit-learn (for KMeans)
- NumPy

## Project Contents

- `smsdata.txt`: The data file generated in the first step.
- `SMSSpamCollection.txt`: Your initial data set file.

## K-Means Parameters

The user can choose the number of clusters the k-means clustering algorithm will create.
