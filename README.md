# AdventOfCode2019
Solutions for Advent of Code 2019 (in Python) with notes, lessons learned, thoughts and frustrations...
I'm still working on solutions even though it's already January. My goal is to finish all challenges

__Day 11__

I wrote code with some debug prints and run it with provided input. Code was running for about 30 seconds and I've, incorrectly, assumed that code stuck in infinite loop. I spend half day debugging only to find out that code was correct I just had to wait longer... I'm too impatient...

__Lessons learned__:
- prints in Python are reeeealy slow, without them code runs 10x faster
- be patient...

__Day 10__
Part 1
- I don't understand how to check visibility of asteroid. Instruction is written in very obfuscated way.
- I thought about cells and this is bad approach. It's simple geometry, you only need to check if asteroid (point) lays on the line between two points.
- I've checked solution on reddit and whole problem is really simple, you just need to calculate angle between asteroids using atan2 and check if such angle for asteroid already exists.
Part 2
- Issue doesn't look hard but I don't know how to calculate steps so that asteroids aren't omitted.
- I was going back in circles so I've looked at some solution and was inspired with my own solution.
- I'm using again angles and distances to calculate rotation of the laser to destroy each asteroid and then I sort them from smallest angle.
- Solution is not working yet, probably I've mixed something with coordinates or calculating angles since laser is rotating clockwise.
- I don't know yet if this is an issue but I'm not taking into account that I shouldn't be storing results because after destruction of each asteroid, old ones could become visible.
- Found description of approach similar to mine but with dictionary with angles as keys, which gave me idea how to solve this. Maybe it will work.