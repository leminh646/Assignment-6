# Assignment 6: Medians and Order Statistics & Elementary Data Structures

## Overview

This repository contains Python implementations of elementary data structures and selection algorithms for order statistics. It is accompanied by the assignment specification and lecture notes provided in the included PDF.

## Repository Structure

- `elementary_data_structures/` – implementations of basic data structures such as stacks, queues, linked lists, etc.
- `selection_algos/` – implementations of selection algorithms like Quickselect and Median of Medians to compute order statistics in linear time.
- `Medians and Order Statistics & Elementary Data Structures.pdf` – analysis and report.
- `.gitignore` – ignores Python cache directories (`__pycache__`).
## Prerequisites

- Python 3.6 or higher

## Installation

Clone the repository:
```bash
git clone https://github.com/leminh646/Assignment-6
```

## Usage

### Selection Algorithms
Navigate to the `selection_algos` folder and run:
```bash
python selection_algos/quickselect.py
```
or
```bash
python selection_algos/median_of_medians.py
```
to compute the k-th smallest element in an array.

To compare the two algorithms, run:
```bash
python python selection_algos/benchmark.py
```
to see the run time of each algorithm with different input sizes and distributions.
Results are shown in the terminal and also in a graph by matplotlib.

### Elementary Data Strucutres
Navigate to  the `elementary_data_structures` folder and run the desired script, for example:
```bash
python elementary_data_structures/stack.py
```
Each module includes a `main` block demonstrating basic usage and test case.