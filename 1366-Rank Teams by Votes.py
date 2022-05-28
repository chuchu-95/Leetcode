class Solution:
    def rankTeams(self, votes):
        rank = {v: [0]*len(votes[0])+[v] for v in votes[0]}
        for vote in votes:
            for idx, team in enumerate(vote):
                rank[team][idx] -= 1
        arr = list(rank.values())
        arr.sort()
        return "".join(sub[-1] for sub in  arr)