import itertools

def main() -> None:
    # for i in itertools.count(10):
    #     print(i)
    #     if i==15:
    #         break
    # items = ['a','b','c']
    # second_items = ['d','e','f']
    # perms = itertools.permutations(items,2)
    # perms = itertools.combinations(items,2)
    # perms = itertools.combinations_with_replacement(items,2)
    # for perm in perms:
    #     print(perm)
    # print(list(itertools.combinations_with_replacement(items,2)))
    # print(list(itertools.chain(items,second_items)))
    # print(list(itertools.combinations(itertools.chain(items, second_items),2)))
    # print(list(itertools.filterfalse(lambda x:x %2 ==0,range(10))))
    # print(list(itertools.takewhile(lambda x:x %2 !=0,range(10))))
    print(list(itertools.starmap(lambda x, y : x*y,[(2,6),(8,4),(5,3)])))


if __name__ == '__main__':
    main()

