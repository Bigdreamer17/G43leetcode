class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loser_count = {}
        ans = []
        one_lose = set()
        no_lose = set()
        for i in range(len(matches)):
            if matches[i][1] in loser_count:
                loser_count[matches[i][1]] += 1
            else:
                loser_count[matches[i][1]] = 1
        for key,value in loser_count.items():
            if value == 1:
                one_lose.add(key)
        for i in range(len(matches)):
            if matches[i][0] not in loser_count.keys():
                no_lose.add(matches[i][0])
        ans.append(sorted(list(no_lose)))
        ans.append(sorted(list(one_lose)))
        return ans 