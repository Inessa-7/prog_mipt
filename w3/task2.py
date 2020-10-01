def write_array(array, file_name):
    with open(file_name, 'w') as ouf:
        output = '\n'.join(array)
        ouf.write(output)


arr = ['safdsf', 'asdasdas', 'dasdadsadsdas', 'asdsadda']
name = 'answer_task2.txt'
write_array(arr, name)
