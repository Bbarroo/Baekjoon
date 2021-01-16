import sys

sys.setrecursionlimit(10**6)

class histo:
    def __init__(self, histo):
        self.histo = histo

    def findLargest(self,head,tail):
        histo = self.histo[head:tail+1]
        if len(histo) == 1:
            return histo[0]
        mid = int(len(histo)/2)
        last = len(histo)


        center_height = min(histo[mid],histo[mid-1])

        center_large = center_height*2
        left = mid-1
        right = mid

        while True:
            if left == 0 and right == last - 1:
                break
            if left == 0 and right != last-1:
                right += 1
                check = right
            if right == last-1 and left != 0:
                left -= 1
                check = left
            if right != last -1  and left != 0:
                if histo[left-1] > histo[right+1]:
                    left -= 1
                    check = left
                else:
                    right += 1
                    check = right
            center_height = min(histo[check],center_height)
            center_large = max(center_large,center_height * (right-left+1))

        left_large = self.findLargest(head,head+mid-1)
        right_large = self.findLargest(head+mid,tail)

        return max([center_large,left_large,right_large])


while True:
    case = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    n_histo = case[0]
    if n_histo == 0:
        break
    a = histo(case[1:])
    print(a.findLargest(0,n_histo-1))