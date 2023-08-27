# Sorting Algorithms

This repository includes different sorting algorithms. The purpose is to show different approaches.

## Algorithms Included

1. **Bubble Sort** - [`bubble_sort.py`](./bubble_sort.py)

Basic Idea: Continuously swap adjacent elements if they are in the wrong order until the list is sorted.

Details: Start from the beginning of the list, and for each pair of adjacent elements, if they are in the wrong order, swap them. This process is repeated for the list until no more swaps are required. During each pass through the list, the largest element "bubbles up" to its correct position.

2. **Insertion Sort** - [`insertion_sort.py`](./insertion_sort.py)

Basic Idea: Build a sorted array (or list) one element at a time by comparing each element with the current largest element and placing it in the appropriate position.

Details: Starting from the second element, compare it with the previous ones. If it's smaller than its predecessor, we compare it with the elements before. Repeat until we reach a number smaller or until we reach the start of the list. Then, insert the element at this position. Continue for all elements.

3. **Merge Sort** - [`merge_sort.py`](./merge_sort.py)

Basic Idea: Divide the list into two halves, sort them, and then merge them.

Details: This is a recursive approach. First, the list is split into halves until each sublist consists of a single element. Then, these smaller sublists are merged back together in such a way that they get sorted. The "merge" operation ensures the resultant list is sorted.

4. **Quick Sort** - [`quick_sort.py`](./quick_sort.py)

Basic Idea: Select a 'pivot' element and partition the list such that all elements less than the pivot are to its left, and all elements greater than the pivot are to its right. Then, recursively sort the two partitions.

Details: A pivot element is chosen from the array. Elements smaller than the pivot are moved to its left, and elements greater are moved to its right. This ensures the pivot is in its correct sorted position. The same process is applied recursively to the left and right partitions.

5. **Selection Sort** - [`selection_sort.py`](./quick_sort.py)

Basic Idea: Repeatedly find the smallest (or largest) element from the unsorted section and move it to the beginning (or end).

Details: Start with the first element as the minimum. Scan through the list to find if there's a smaller element. If one is found, note its position. Swap the minimum element with the first element. Repeat this process for the next position until the entire list is sorted.

## Usage

Each algorithm is implemented in a standalone Python script. To execute any of them, use:

```bash
python <script-name>.py

## To bo added:
- 
