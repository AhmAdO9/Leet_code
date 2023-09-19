class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        g_index = gas.index(max(gas))
        c_index = gas.index(max(gas))
        g_value = gas[gas.index(max(gas))]
        c_value = cost[gas.index(max(gas))]
        

        while g_value >= c_value:
                if g_index == -1:
                    break
                if  gas.index(max(gas)) == 0:
                    g_value = gas[len(gas)-1]
                    c_value = cost[len(gas)-1]
                else:
                    g_index -=1
                    c_index -=1
                    g_value = gas[g_index]
                    c_value = cost[c_index]
                   

        g_index +=1
        orig = g_index
        c_index +=1
        g_value = gas[g_index]
        c_value = cost[c_index]

        g_new = []
        c_new = []
        itr1 = len(gas) - g_index

        itr2 = g_index
    
        i = 0
        while i < itr1:
                g_new.append(gas[g_index])
                c_new.append(cost[g_index])
                i+=1
                g_index+=1

        i = 0
        while i < itr2:
            g_new.insert(itr1, gas[i])
            c_new.insert(itr1, cost[i])
            i+=1
            itr1+=1

        i = 0
        g = g_new[i]
        c = c_new[i]
        while g >= c:
            try:
                g = (g - c) + g_new[i+1]
                c = c_new[i+1]
                i+=1
            except IndexError:
                return orig

        return -1
 
    

sol  = Solution()
print(sol.canCompleteCircuit([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]))