import pandas as pd

# Define local files to process directly from this folder
files = [
    ("Amazon", "amazon_cells_labelled.txt"),
    ("Yelp", "yelp_labelled.txt")
]

frames = []

for source, filename in files:
    # Read local tab-separated files without header rows
    df = pd.read_csv(filename, sep="\t", header=None, names=["feedback_text", "sentiment_label"])
    df["source"] = source
    frames.append(df)

# Merge datasets together into a single master sheet
feedback_df = pd.concat(frames, ignore_index=True)

# Generate dataset metrics for your presentation slides
print("--- Data Summary Statistics ---")
print(f"Total Rows Loaded: {len(feedback_df)}")
print(f"\nBreakdown by Source:\n{feedback_df['source'].value_counts()}")
print(f"\nBreakdown by Sentiment (1=Pos, 0=Neg):\n{feedback_df['sentiment_label'].value_counts()}")

# Export out to your clean working CSV file
feedback_df.to_csv("capstone_customer_feedback.csv", index=False)
print("\nSuccess! 'capstone_customer_feedback.csv' has been created.")
