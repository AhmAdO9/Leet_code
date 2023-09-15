my_list = []
def findItinerary(tickets,n, past):
        a = 0
        i = 0
        index = []
        index.append(tickets[n])
        while i < len(tickets):
                if len(my_list) == len(tickets)-1:
                            my_list.append(tickets[n])
                            return
                if index[0][1] == tickets[i][0] and a==0 and past == False:
                    if tickets[i] not in my_list:
                        my_list.append(index[0])
                        a+=1
                        n=0
                        n+=tickets.index(tickets[i])
                        findItinerary(tickets,n, past=False)
               

                if index[0][0] == tickets[i][1] and a==0 and past == True:
                    a+=1
                    index.pop(0)
                    my_list.insert(0,tickets[i])
                    index.append(tickets[i])
                    n=0
                    n+=tickets.index(tickets[i])
                    if index[0][0] == tickets[0][0]:
                        return
                    else:
                        findItinerary(tickets,n, past=True)
                        findItinerary(tickets,0, past=False)
                i+=1

        li = []
        for i in my_list:
                li.append(i[0])
        li.append(i[1])
        return my_list
            
print(findItinerary([["MUC","LHR"],["HBD","JFK"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],0,past= True))
