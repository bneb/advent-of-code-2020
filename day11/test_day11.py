from day11 import get_visible_neighbors

test_input = (
'#######\n'
'#.....#\n'
'#.....#\n'
'#..L..#\n'
'#.....#\n'
'#.....#\n'
'#######\n'
)



if __name__ == '__main__':
    print(test_input)

    print(get_visible_neighbors((3, 3), test_input))
