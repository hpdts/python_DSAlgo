import requests

def transferAmount(name: str, city: str) -> list:
    base_url = "https://jsonmock.hackerrank.com/api/transactions"
    max_credit = 0.0
    max_debit = 0.0

    # Fetch the first page to get pagination details
    response = requests.get(base_url)
    response_data = response.json()
    total_pages = response_data['total_pages']

    # Iterate through all pages
    for page in range(1, total_pages + 1):
        response = requests.get(f"{base_url}?page={page}")
        data = response.json()['data']

        # Filter records by userName and city
        for record in data:
            if record['userName'] == name and record['location']['city'] == city:
                amount = float(record['amount'].replace('$', '').replace(',', ''))
                if record['txnType'] == 'credit':
                    max_credit = max(max_credit, amount)
                elif record['txnType'] == 'debit':
                    max_debit = max(max_debit, amount)

    # Format the results as currency strings
    return [f"${max_credit:,.2f}", f"${max_debit:,.2f}"]

# Example usage
name = "Bob Martin"
city = "Bourg"
result = transferAmount(name, city)
assert result == ['$3,717.84', '$3,568.55'], "Test failed for Alice Johnson in Springfield"

print("All assertions passed!")


def getMinOperations(change, arr):
    n = len(change)
    m = len(arr)
    operations = 0
    nullified = [False] * m  # Track which elements of arr are nullified

    for i in range(m):
        # Decrement arr[i] until it reaches 0
        while arr[i] > 0:
            arr[i] -= 1
            operations += 1

        # Check if arr[i] can be nullified
        nullified_index = -1
        for j in range(n):
            if change[j] == i + 1 and not nullified[i]:
                nullified_index = j
                break

        if nullified_index == -1:
            return -1  # Cannot nullify arr[i]

        nullified[i] = True
        operations += 1  # Nullify operation

    return operations


# Example usage
change = [0, 1, 0, 2]
arr = [1, 1]
print(getMinOperations(change, arr))  # Output: 4

# Additional test case
change = [1, 0, 1, 3, 2, 1, 0, 3, 1, 1]
arr = [3, 2, 1]
print(getMinOperations(change, arr))  # Output: 9