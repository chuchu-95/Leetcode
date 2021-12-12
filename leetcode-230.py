def countMatches(items, ruleKey, ruleValue):
    key_dict = {"type": 0, "color": 1, "name": 2}
    cnt = 0
    for i in range(len(items)):
        if items[i][key_dict[ruleKey]] == ruleValue:
            cnt += 1
    return cnt
print(countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))


def closestCost(baseCosts, toppingCosts, target):
    result = 0
    low_cost = 0
    for i in baseCosts:
        