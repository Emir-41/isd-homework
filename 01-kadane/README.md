# Assignment 1: Kadane's algorithm

Find the contiguous subarray with the largest sum and return its start index, end index and maximum sum. The stock example applies the same algorithm to consecutive price changes.

This exercise is independent of the Flask app and uses only Python's standard library.

## Run

Open a terminal in `01-kadane` and run:

```bash
python3 kadane.py
```

For the notebook example `[-2, 1, -3, 7, -1, 2, 1, -5, 4]`, the result is:

```text
Start index: 3
End index: 6
Best subarray: [7, -1, 2, 1]
Maximum sum: 9
```

Indices start at 0. Both endpoints are included. `kadane(nums)` returns a dictionary with `start`, `end` and `sum`. It takes O(n) time and O(1) extra space. An empty list raises `ValueError`. For an all-negative list, it returns the largest single element. If several subarrays have the same maximum sum, the first best result encountered is kept.

`best_trade(prices)` first calculates consecutive price changes and applies Kadane to them. For `[100, 98, 99, 96, 103, 102, 104, 105, 100, 104]`, it buys at index 3 for 96 and sells at index 7 for 105, giving a profit of 9. It considers at most one purchase followed by one sale. If no positive profit is possible, profit is 0 and both indices are `None`. The additional list of changes takes O(n) space.
