def calculate_total(value, multiplier=1.15):
    """
    Calculate the total value by multiplying with a given multiplier.

    Args:
        value (float): The original value.
        multiplier (float): The multiplier to apply. Default is 1.15.

    Returns:
        float: The calculated total value.
    """
    return value * multiplier

def display_total(value):
    """
    Display the total value in a formatted string.

    Args:
        value (float): The value to display.
    """
    formatted_string = f"Total: {value:.2f}"
    print(formatted_string)

def log_results(results, filename="log.txt"):
    """
    Log the results to a file.

    Args:
        results (list): The list of results to log.
        filename (str): The name of the log file. Default is "log.txt".
    """
    with open(filename, "a") as f:
        f.write(str(results) + "\n")

def process_data(data, multiplier=1.15):
    """
    Process the data by calculating totals, displaying them, logging, and returning results.

    Args:
        data (list): List of values to process.
        multiplier (float): Multiplier for calculations. Default is 1.15.

    Returns:
        list: List of calculated total values.
    """
    results = []
    for value in data:
        total = calculate_total(value, multiplier)
        display_total(total)
        results.append(total)
    log_results(results)
    return results
