class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        for i in range(len(garbage)):
            garbage[i] = Counter(garbage[i])
        
        M_pref = [0]
        P_pref = [0]
        G_pref = [0]
        for g in garbage:
            M_pref.append(M_pref[-1] + g.get("M", 0))
            P_pref.append(P_pref[-1] + g.get("P", 0))
            G_pref.append(G_pref[-1] + g.get("G", 0))
        
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        travel = [0] + travel
        
        M_end = -1
        P_end = -1
        G_end = -1
        for i in range(len(garbage) - 1, -1, -1):
            if "M" in garbage[i] and M_end == -1:
                M_end = i
            if "P" in garbage[i] and P_end == -1:
                P_end = i
            if "G" in garbage[i] and G_end == -1:
                G_end = i
        
        minutes = 0
        if M_end != -1:
            minutes += travel[M_end] + M_pref[M_end + 1]
        if P_end != -1:
            minutes += travel[P_end] + P_pref[P_end + 1]
        if G_end != -1:
            minutes += travel[G_end] + G_pref[G_end + 1]
        
        return minutes