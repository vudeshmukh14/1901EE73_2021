def meraki_helper(n):

    cnt_meraki = 0
    cnt_non_meraki = 0

    for num in n:
        st = str(num)
        if len(st)==1:
            print(f"Yes - {st} is a Meraki number")
            cnt_meraki += 1

        else:
            last_ch = st[0]
            flag = True
            for ch in st[1:]:
                if (abs(int(ch)-int(last_ch))!=1):
                    print(f"No - {st} is not a Meraki number")
                    cnt_non_meraki += 1
                    flag = False
                    break
                else:
                    last_ch = ch
            if flag:
                print(f"Yes - {st} is a Meraki number")
                cnt_meraki += 1

    print(f"the input list contains {cnt_meraki} meraki and {cnt_non_meraki} non meraki numbers")


input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
meraki_helper(input)