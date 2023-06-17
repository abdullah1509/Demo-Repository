def add_linked_lists(l1, l2):

    carry = 0
    result = []

    while l1 or l2 or carry:

        x = l1.data if l1 else 0
        y = l2.data if l2 else 0

        sum = x + y + carry

        carry = sum // 10
        result.append(sum % 10)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result



l1 = [2,4,3]
l2 = [5,6,4]
add_linked_lists(l1, l2)
