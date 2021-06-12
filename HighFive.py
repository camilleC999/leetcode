class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        idDict={}
        output = []
        items.sort(key= lambda x: x[1], reverse = True)
        for i in items:
            if i[0] not in idDict.keys():
                idDict[i[0]] = []
                idDict[i[0]].append(i[1])
                idDict[i[0]].append(1)
            else:
                if idDict[i[0]][1] < 5:
                    idDict[i[0]][0] = idDict[i[0]][0] + i[1]
                    idDict[i[0]][1] = idDict[i[0]][1] + 1
                    if idDict[i[0]][1] == 5:
                        output.append([i[0], int((idDict[i[0]][0])/5)])
        return sorted(output)
        
