class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        fleets = 0
        lastTime = 0
        for p, s in pair:
            time = (target - p) / s
            if time > lastTime:
                fleets += 1
                lastTime = time
        return fleets
        

