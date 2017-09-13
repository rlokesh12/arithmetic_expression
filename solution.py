#if x is divisible by n then any no of numbers multiplied to x will also be divisible by n
def operate(val,x):
    if x==n:
        return 'na'
    mval = val * nums[x]
    if mval % 101 == 0:
        mresult = '*'+str(nums[x])
        if x != n-1:
            result = mresult+'*'+'*'.join(str(a) for a in nums[x+1:]) 			#multiplying the rest numbers to expression
        else:
            result = mresult
        return result
    else:
        aval = val + nums[x]
        if aval % 101 == 0:
            aresult = '+'+str(nums[x])
            if x != n-1:
                result = aresult+'*'+'*'.join(str(a) for a in nums[x+1:])		#multiplying the rest numbers to expression
            else:
                result = aresult
            return result
        else:
            sval = val - nums[x]
            if sval % 101 == 0:
                sresult = '-'+str(nums[x])
                if x != n-1:
                    result = sresult+'*'+'*'.join(str(a) for a in nums[x+1:])		#multiplying the rest numbers to expression
                else:
                    result = sresult
                return result
            else:
                mr = operate(mval,x+1)
                if mr != 'na':
                    result = '*'+str(nums[x])+mr
                    return result 
                else:
                    ar = operate(aval,x+1)
                    if ar != 'na':
                        result = '+'+str(nums[x])+ar
                        return result
                    else:
                        sr = operate(sval,x+1)
                        if sr != 'na':
                            result = '-'+str(nums[x])+sr
                            return result
                        else:
                            return 'na'
n = int(input())
nums = [int(n) for n in input().split(' ')]
x=1
val = nums[0]
result = operate(val,x)
print(str(nums[0])+result)
