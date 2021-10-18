dividend = 10, divisor = 3
a,b,res = abs(dividend), abs(divisor), 0
for i in range(31,-1,-1):
    if b << i <= a:
        res += 1<<i
        a -= b<<i

return res if (dividend > 0) == (divisor > 0) else -res