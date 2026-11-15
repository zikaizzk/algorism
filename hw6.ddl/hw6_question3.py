import sys
from ast import literal_eval
from hw6_question2 import MinHeap


def running_medians(values):
    lower=MinHeap()
    upper=MinHeap()
    medians=[]

    for value in values:
        if lower.is_empty() or value<=-lower.peek():
            lower.insert(-value)
        else:
            upper.insert(value)

        if len(lower)>len(upper)+1:
            upper.insert(-lower.extract_min())
        elif len(upper)>len(lower):
            lower.insert(-upper.extract_min())

        if len(lower)==len(upper):
            median=(-lower.peek()+upper.peek())/2
        else:
            median=float(-lower.peek())

        medians.append(median)

    return medians


def main():
    values=literal_eval(sys.stdin.read())
    print(running_medians(values))


if __name__=="__main__":
    main()
