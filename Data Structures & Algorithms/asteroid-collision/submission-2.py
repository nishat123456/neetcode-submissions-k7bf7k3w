class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #meet, small gone
        #same size, both gone
        #same dir, never meet
        #make stack, return stack.
        #for, calculate who stays, then we compare with stack[-1] and we put to stack

        stack = []
        val = 0

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = asteroid + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    asteroid = 0
                    stack.pop()
                else:
                    asteroid = 0


            if asteroid != 0:
                stack.append(asteroid)
        return stack