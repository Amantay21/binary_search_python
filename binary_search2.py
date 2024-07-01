def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid][0] == target:
            return arr[mid][1]
        elif arr[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

phone_book = [('Musa', '+996-778-00-15-26'), ('Isa', '+7(807)888-89-01'), ('John', '+234-708-9012'), ('Wasya', '+1-902-231-7883')]

name = input("write the name you want to find: ")
phone_number = binary_search(phone_book, name)

if phone_number:
    print(f"{name}'s phone number is {phone_number}.")
else:
    print(f"Sorry, {name}'s contact doesn't exist in the phone book.")