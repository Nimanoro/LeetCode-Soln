class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        stack = []
        for pos, spd in reversed(sorted(zip(position, speed))):
            est = (target - pos) / spd
            if not stack:
                stack.append(est)
            if stack and est > stack[-1]:
                stack.append(est)
        return len(stack)

if __name__ == "__main__":
    pos = [10,8,0,5,3]
    spd = [2,4,1,1,3]
    target = 12
    print(Solution().carFleet(target, pos, spd)) # 3