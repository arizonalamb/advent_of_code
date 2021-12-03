def dive(path):
    
    depth = 0
    horizontal = 0
    
    with open(path, 'r', encoding='UTF=8') as file:
        for line in file:
            if line.split()[0] == 'forward':
                horizontal += int(line.split()[1])
            elif line.split()[0] == 'down':
                depth += int(line.split()[1])
            else:
                depth -= int(line.split()[1])
    return horizontal*depth
  
  
  def dive2(path):
    
    depth = 0
    horizontal = 0
    aim = 0
    
    with open(path, 'r', encoding='UTF=8') as file:
        for line in file:
            if line.split()[0] == 'forward':
                horizontal += int(line.split()[1])
                depth += aim*int(line.split()[1])
            elif line.split()[0] == 'down':
                aim += int(line.split()[1])
            elif line.split()[0] == 'up':
                aim -= int(line.split()[1])
    print(horizontal, depth)
    return horizontal*depth
