class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []

        # 將參議員按索引加入各自的列表
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # 模擬過程
        while radiant and dire:
            r = radiant.pop(0)
            d = dire.pop(0)

            # 兩者對比，將較小的放回列表，並將其索引+len(senate)以示下一回合可用
            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))

        # 根據剩下的列表決定勝者
        return "Radiant" if radiant else "Dire"


