def kadane(nums):
    if not nums:
        raise ValueError("The list must not be empty.")

    # current_sum ends at the current index; best_sum can belong to an earlier window.
    # Start with the first number so all-negative lists return a negative result.
    current_sum = nums[0]
    best_sum = nums[0]
    current_start = 0
    best_start = 0
    best_end = 0

    for index in range(1, len(nums)):
        # Drop a negative running sum because it would lower the next total.
        if current_sum < 0:
            current_sum = nums[index]
            current_start = index
        else:
            current_sum += nums[index]

        # Keep the best window's indices whenever the running sum improves it.
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = index

    # Both indices are zero-based and included in the result's window.
    return {"start": best_start, "end": best_end, "sum": best_sum}


def best_trade(prices):
    if len(prices) < 2:
        raise ValueError("At least two prices are required.")

    changes = []
    # Consecutive changes add up to the selling price minus the buying price.
    for index in range(1, len(prices)):
        changes.append(prices[index] - prices[index - 1])

    result = kadane(changes)

    # Choose no trade if every available profit is zero or negative.
    if result["sum"] <= 0:
        return {"buy_day": None, "sell_day": None, "profit": 0}

    return {
        "buy_day": result["start"],
        # The last change ends at the following price index.
        "sell_day": result["end"] + 1,
        "profit": result["sum"],
    }


if __name__ == "__main__":
    # These examples run directly, but not when another file imports the functions.
    nums = [-2, 1, -3, 7, -1, 2, 1, -5, 4]
    result = kadane(nums)

    print("Kadane - notebook example")
    print("Input:", nums)
    print("Start index:", result["start"])
    print("End index:", result["end"])
    print("Best subarray:", nums[result["start"]:result["end"] + 1])
    print("Maximum sum:", result["sum"])

    prices = [100, 98, 99, 96, 103, 102, 104, 105, 100, 104]
    trade = best_trade(prices)

    print("\nStock example - one buy and one later sale")
    print("Prices:", prices)
    print("Buy index:", trade["buy_day"])
    print("Sell index:", trade["sell_day"])
    print("Maximum profit:", trade["profit"])
