from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result = []
        friends_set = set(friends)

        for i in range(len(order)):
            if order[i] in friends_set:
                result.append(order[i])

        return result
