import pandas as pd

s1 = pd.read_csv("student_resource/dataset/train/train_source1.tsv", sep="\t", nrows=1000)
gt = pd.read_csv("student_resource/dataset/train/train_ground_truth.tsv", sep="\t", nrows=1000)

print(s1.shape)
print(s1.head())
print(gt.head())
