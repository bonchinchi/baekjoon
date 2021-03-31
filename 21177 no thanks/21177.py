first = int(input())
if(first>0 and first<90001):
    cards = list(map(int,input().split()))
    s = set(cards)
    if (min(cards)>0 and max(cards)<90001 and len(cards)==first):
        if len(cards) == len(s):
            newlist = 0
            cards = sorted(cards)
            prev = cards[0]
            for curr in cards:
                if (curr != prev + 1):
                    newlist += curr
                prev = curr
            output = newlist
            print(output)
    else:
        pass
else:
    pass