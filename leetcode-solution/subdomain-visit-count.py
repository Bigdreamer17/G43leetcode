class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        table = {}


        for cp in cpdomains:
            l = cp.split(' ')
            count = l[0]
            domain = l[1]

            subdomains = domain.split(".")

            for i in range(len(subdomains)):
                sub = ".".join(subdomains[i:])


                if sub not in table:
                    table[sub] = count
                else:
                    table[sub] = str(int(table[sub]) + int(count))

        for k, v in table.items():
            ans.append(v + " " + k)

        return ans