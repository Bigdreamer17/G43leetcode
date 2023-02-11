class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left = right = 0
        ans = 0
        while right < len(trainers) and left < len(players):
            if players[left] > trainers[right]:
                right += 1
            elif players[left] <= trainers[right]:
                ans += 1
                left += 1
                right += 1
        return ans