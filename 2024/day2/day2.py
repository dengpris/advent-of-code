
def day2(filepath, part2=False):
    def is_grad_decr(arr):
        for i in range(1, len(arr)):
            if arr[i] >= arr[i-1] or arr[i] < arr[i-1]-3:
                return False
        return True
    def is_grad_incr(arr):
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1] or arr[i] > arr[i-1]+3: 
                return False
        return True
    
    res: int = 0
    with open(filepath) as f:
        for line in f:
            arr = [int(x) for x in line.split()]
            n: int = len(arr)
            if is_grad_incr(arr) or is_grad_decr(arr):
                res += 1
            elif part2:
                # remove 1 bad booboo
                for i in range(1, n+1):
                    mod_arr = arr[0:i-1] + arr[i:n]
                    if is_grad_incr(mod_arr) or is_grad_decr(mod_arr):
                        res += 1
                        break
                
    return res

print(day2('input_sample', part2=True))
print(day2('input', part2=True))