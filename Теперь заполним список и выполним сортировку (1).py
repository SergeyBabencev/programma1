def main():
    input_list = [1.20, 0.22, 0.43, 0.36,0.39,0.27]
    print('ORIGINAL LIST:')
    print(input_list)
    sorted_list = bucket_sort(input_list)
    print('SORTED LIST:')
    print(sorted_list)