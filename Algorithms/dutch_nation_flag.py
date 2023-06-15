def dnf(nums, n):
    s_ptr = 0
    m_ptr = 0
    e_ptr = n - 1

    while m_ptr <= e_ptr:
        if nums[m_ptr] == 0:
            nums[s_ptr], nums[m_ptr] = nums[m_ptr], nums[s_ptr]
            s_ptr += 1
            m_ptr += 1
        elif nums[m_ptr] == 2:
            nums[e_ptr], nums[m_ptr] = nums[m_ptr], nums[e_ptr]
            e_ptr -= 1
        else:
            m_ptr += 1

    return nums
