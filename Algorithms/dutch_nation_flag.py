def dnf(arr, n):
    s_ptr = 0
    m_ptr = 1
    e_ptr = n - 1
    
    while m_ptr < e_ptr:
        if arr[m_ptr] == 1:
            arr[s_ptr], arr[m_ptr] = arr[m_ptr], arr[s_ptr]
            s_ptr += 1
        elif arr[m_ptr] == 2:
            arr[e_ptr], arr[m_ptr] = arr[m_ptr], arr[e_ptr]
            e_ptr -= 1
        else:
            m_ptr += 1
            
  return arr
