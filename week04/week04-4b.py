#week04-4b.py(­«¼gweek04-3.py)
        H = [0] * 200
        for nn in nums:
            H[nn] += 1
        for nn in nums:
            if nn % 2 == 0 and H[nn] == 1: return nn
        return -1
