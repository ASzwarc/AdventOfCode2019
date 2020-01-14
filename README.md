# AdventOfCode2019
Solutions for Advent of Code 2019 (in Python) with notes, lessons learned, thoughts and frustrations...
I'm still working on solutions even though it's already January. My goal is to finish all challenges

__Day 11__

I wrote code with some debug prints and run it with provided input. Code was running for about 30 seconds and I've, incorrectly, assumed that code stuck in infinite loop. I spend half day debugging only to find out that code was correct I just had to wait longer... I'm too impatient...

__Lessons learned__:
- prints in Python are reeeealy slow, without them code runs 10x faster
- be patient...

__Day 10__

- I don't understand how to check visibility of asteroid. Instruction is written in very obfuscated way.
- I thought about cells and this is bad approach. It's simple geometry, you only need to check if asteroid (point) lays on the line between two points.
- I still don't know how to do it in optimal way...