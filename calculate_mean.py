import numpy as np

def calculate_mean(data):
    mean = np.mean(data)
    return mean

def main():
    # Sample dataset as a numpy array
    data = np.array([10, 20, 30, 40, 50])

    # Calculate the mean
    mean = calculate_mean(data)

    print(f"Mean of the dataset: {mean}")

if __name__ == "__main__":
    main()
