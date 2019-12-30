#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    attr = dir(hidden_4)
    for i in attr:
        if i.startswith('__'):
            continue
        print(i)
