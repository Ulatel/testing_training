from solution import Solution


a = "4,5,6,7,0,1,2".split(",")
a = [int(item) for item in a]

print(a)
s = Solution()
print(s.search(list(range(10, 5001+1))+list(range(1, 10)), 100))