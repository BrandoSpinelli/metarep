import argparse 
import string
import matplotlib.pyplot as plt
import time

from loguru import logger 


def count_characters(file_path, plot_histogram, elapsed_time):
    start_time = time.time()
    logger.info(f"Starting to measure time...")
    counts = {char: 0 for char in string.ascii_lowercase}

    with open(file_path, 'r', encoding='utf-8') as input_file:
        logger.debug(f"Reading input data from {file_path}...")
        data = input_file.read()
    logger.debug(f"Done, {len(data)} character(s) found.")
    logger.info("Counting characters...")

    for char in data.lower():
        if char in counts:
            counts[char] += 1 

    logger.info(f"Character counts: {counts}")

    num_characters = sum(counts.values())
    logger.info(f"Total number of characters: {num_characters}")

    for key, value in counts.items():
        counts[key] = value / num_characters
    logger.info(f'Character frequences: {counts}')
    
    logger.info("Done measuring elapsed time.")
    end_time = time.time()
    time_taken = end_time - start_time

    if plot_histogram:
        plot_character_histogram(counts)
    
    if elapsed_time:
        logger.info(f"Time taken to count characters: {time_taken} seconds")

def plot_character_histogram(counts):
    characters = list(counts.keys())
    frequencies = list(counts.values())

    # Set a style
    plt.style.use('seaborn-darkgrid')

    plt.figure(figsize=(12, 6))
    bars = plt.bar(characters, frequencies, color='#1f77b4', edgecolor='black')

    # Add data labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2%}', ha='center', va='bottom', fontsize=10)

     # Set font properties
    font_title = {'family': 'Helvetica Neue', 'weight': 'bold', 'size': 16}
    font_labels = {'family': 'Helvetica Neue', 'weight': 'normal', 'size': 14}

    plt.xlabel('Characters', fontdict=font_labels)
    plt.ylabel('Frequencies', fontdict=font_labels)
    plt.title('Character Frequency Histogram', fontdict=font_title)
    plt.xticks(rotation=0)
    plt.ylim(0, max(frequencies) * 1.1)  # Extend y-axis slightly
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count the characters in a text file')
    parser.add_argument('file')
    parser.add_argument('--time', action='store_true', help='display the time taken to count characters')
    parser.add_argument('--histogram', action='store_true',
        help='plot a histogram of the character frequencies')
    args = parser.parse_args()
    count_characters(args.file, args.time, args.histogram)
    