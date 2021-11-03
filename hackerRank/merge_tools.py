def merge_the_tools(string, k):
    # your code goes here
    def merge(string):
        output = list(dict.fromkeys(string).keys())
        return ''.join(output)

    for i in range(len(string) // k):
        print(merge(string[i * k:(i + 1) * k]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)