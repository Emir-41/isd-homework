def kadane(nums):
    if not nums:
        raise ValueError("The list must not be empty.")

    current_sum = nums[0]
    best_sum = nums[0]
    current_start = 0
    best_start = 0
    best_end = 0

    for index in range(1, len(nums)):
        # A negative running sum would reduce the next subarray sum.
        if current_sum < 0:
            current_sum = nums[index]
            current_start = index
        else:
            current_sum += nums[index]

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = index

    return {"start": best_start, "end": best_end, "sum": best_sum}


def best_trade(prices):
    if len(prices) < 2:
        raise ValueError("At least two prices are required.")

    changes = []
    for index in range(1, len(prices)):
        changes.append(prices[index] - prices[index - 1])

    result = kadane(changes)

    # The stock example allows making no trade.
    if result["sum"] <= 0:
        return {"buy_day": None, "sell_day": None, "profit": 0}

    return {
        "buy_day": result["start"],
        "sell_day": result["end"] + 1,
        "profit": result["sum"],
    }


if __name__ == "__main__":
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
