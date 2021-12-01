def sonar_sweep(path):
    
    file_array = []
    final_counter = 0
    
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            file_array.append(int(line))
    for ind in range(3, len(file_array)):
        if (file_array[ind] + file_array[ind-1] + file_array[ind-2]) > (file_array[ind-1] + file_array[ind-2] + file_array[ind-3]):
            final_counter += 1
            
    print(final_counter)
    
path = '/data.txt'
sonar_sweep(path)
