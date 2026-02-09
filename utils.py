def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    Returns 0 if the input is invalid or no valid numbers are found.
    """
    # Handle None case explicitly
    if numbers is None:
        return 0

    # Ensure it's iterable (but not a string, which is technically iterable)
    try:
        iter(numbers)
    except TypeError:
        return 0

    # Handle string case (strings are iterable but shouldn't be treated as number lists)
    if isinstance(numbers, str):
        return 0

    # Iterate and sum only numeric values
    try:
        total = 0
        count = 0
        for num in numbers:
            # Skip non-numeric values to avoid TypeError
            if isinstance(num, (int, float)) and not isinstance(num, bool):
                # Avoid potential overflow by checking for infinity
                try:
                    total += num
                    count += 1
                except OverflowError:
                    return float('inf') if num > 0 else float('-inf')

        # Avoid division by zero if no valid numbers found
        if count == 0:
            return 0
        # Handle case where total is 0 to prevent potential division issues
        if total == 0:
            return 0
        return total / count
    except (TypeError, AttributeError):
        return 0

def get_user_name(user):
    """
    Extract and format the user name from a user dictionary.
    Returns "UNKNOWN" if the input is invalid or name cannot be extracted.
    """
    # Handle None case to avoid AttributeError
    if user is None:
        return "UNKNOWN"

    # Ensure user is a dictionary to avoid AttributeError on .get()
    if not isinstance(user, dict):
        return "UNKNOWN"

    # Get name with default value (handles None automatically)
    name = user.get("name", "Unknown")

    # Ensure name is a string before calling upper()
    if isinstance(name, str):
        return name.upper()

    # Convert non-string values to string
    return str(name).upper()