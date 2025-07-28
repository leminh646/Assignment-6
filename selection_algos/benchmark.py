import time
import random
import matplotlib.pyplot as plt
from randomized_quickselect import randomized_quickselect
from median_of_medians import median_of_medians

def run_benchmark():
    input_sizes = [1000, 2000, 5000]
    distributions = {
        "random": lambda n: random.sample(range(n * 2), n),
        "sorted": lambda n: list(range(n)),
        "reversed": lambda n: list(range(n, 0, -1))
    }

    results = {"Quickselect": {}, "MedianOfMedians": {}}

    for dist_name, dist_func in distributions.items():
        results["Quickselect"][dist_name] = []
        results["MedianOfMedians"][dist_name] = []

        for size in input_sizes:
            data = dist_func(size)
            k = size // 2 # Median

            # Time Quickselect
            qs_data = data.copy()
            start = time.perf_counter()
            randomized_quickselect(qs_data, k)
            elapsed_qs = time.perf_counter() - start

            # Time Median of Medians
            mom_data = data.copy()
            start = time.perf_counter()
            median_of_medians(mom_data, k)
            elapsed_mom = time.perf_counter() - start

            results["Quickselect"][dist_name].append(elapsed_qs)
            results["MedianOfMedians"][dist_name].append(elapsed_mom)

            print(f"[{dist_name}] Size {size} - QS: {elapsed_qs:.5f}s, MoM: {elapsed_mom:.5f}s")

    return input_sizes, results
    
# Visualization using matplotlib
def plot_results(input_sizes, results):
    for algo in results:
        for dist_name in results[algo]:
            plt.plot(input_sizes, results[algo][dist_name], label=f'{algo} ({dist_name})')

    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("QuickSelect vs Median of Medians")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Run benchmark
if __name__ == "__main__":
    input_sizes, results = run_benchmark()
    plot_results(input_sizes, results)