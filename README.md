# Advent of Code 2020
###### https://adventofcode.com/2020
---

## Code Organization
Witin the repo, there is a directory for each day of the advent calendar.

- Day 1 has directory `day01` containing `day01.py` and `day01_input.txt`.
- Day 2 is structured similarly and so on for the rest of the days.

On days where the puzzle is more difficult, there will be test files as well.

---

## How To

### Get Started Each Day
Simply create the directory and stubbed files for the next day.
```
$ ./new
```
If you've completed days 1 through n, it will create the directory and files for day n+1.

If you need to create a specific day D, use one of these options:
```
$ ./new D
$ python3 new_day.py -d=D
```
This creates a directory `day0D`, and files `day0D.py`, `input.txt`, and `test_input.txt` per the code organization section.

### Produce a Solution
Run the code with the input file to produce the solution(s) for day D as follows:
```
$ cd day0D
$ python3 day0D.py -f=input.txt 
```

In the case of day 1, my result for part 1 would look like:
```
$ python3 day01.py -f=day01_input.txt
Day 01 solution: 73371
```

---

