def calculate(s):
    num, stack, sign = 0, [], "+"
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in "+-*/" or i == len(s) - 1:
            if sign == "+": stack.append(num)
            elif sign == "-": stack.append(-num)
            elif sign == "*": stack[-1] *= num
            elif sign == "/": stack[-1] = int(stack[-1] / num)
            sign, num = ch, 0
    return sum(stack)
