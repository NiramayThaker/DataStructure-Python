def mul(v1, v2, z=0):
    """
    Multiplies a single digit v2 with a list of digits v1, handling carry and positional zeros.
    
    Parameters:
    v1 (list): The list of digits to multiply.
    v2 (int): The single digit multiplier.
    z (int): The number of trailing zeros to add for positional significance.
    
    Returns:
    list: The product as a list of digits.
    """
    ans = []
    carr = 0
    
    # Multiply each digit of v1 by v2, starting from the least significant digit
    for i in range(len(v1) - 1, -1, -1):
        x = (v1[i] * v2) + carr
        carr = x // 10
        ans.append(x % 10)
    
    # Append any remaining carry
    if carr > 0:
        ans.append(carr)
    
    # Reverse to restore the correct order
    ans.reverse()
    
    # Add trailing zeros for positional significance
    if z >= 1:
        ans.extend([0] * z)
    
    return ans

def add(op):
    """
    Sums up a list of lists representing numbers, digit by digit, handling carry.
    
    Parameters:
    op (list of lists): The list of digit lists to sum.
    
    Returns:
    list: The sum as a list of digits.
    """
    # Find the maximum length of the lists
    max_len = max(len(arr) for arr in op)
    
    # Pad lists with zeros at the beginning to make them of equal length
    for i in range(len(op)):
        op[i] = [0] * (max_len - len(op[i])) + op[i]
    
    result = []
    carry = 0
    
    # Perform addition column by column from the least significant digit
    for i in range(max_len - 1, -1, -1):
        column_sum = carry + sum(arr[i] for arr in op)
        carry = column_sum // 10
        result.append(column_sum % 10)
    
    # Append any remaining carry
    while carry > 0:
        result.append(carry % 10)
        carry //= 10
    
    # Reverse the result since we've appended digits in reverse order
    return result[::-1]

def main_mul(a1, a2):
    """
    Multiplies two lists of digits representing numbers and prints the intermediate 
    and final results.
    
    Parameters:
    a1 (list): The first number as a list of digits.
    a2 (list): The second number as a list of digits.
    
    Returns:
    None
    """
    z_cnt = 0
    op = []
    
    # Perform multiplication for each digit of a2, starting from the least significant digit
    for i in a2[::-1]:
        op.append(mul(a1, i, z_cnt))
        z_cnt += 1
    
    # Print the final sum of intermediate results
    return add(op)


if __name__ == '__main__':
    arr1 = [9, 9]
    arr2 = [9, 9]
    
    arr = main_mul(arr1, arr2)
    a = int(''.join(map(str, arr)))
    print(f"{''.join(map(str, arr1))} * {''.join(map(str, arr2))} = {a}")
    
