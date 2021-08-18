def meraki_helper(n):

    cnt_meraki = 0
    cnt_non_meraki = 0

    for num in n:
        st = str(num)
        if len(st)==1:
            print("Yes - {0} is a Meraki number".format(st))
            cnt_meraki += 1

        else:
            last_ch = st[0]
            flag = True
            for ch in st[1:]:
                if (abs(int(ch)-int(last_ch))!=1):
                    print("No - {0} is not a Meraki number".format(st))
                    cnt_non_meraki += 1
                    flag = False
                    break
                else:
                    last_ch = ch
            if flag:
                print("Yes - {0} is a Meraki number".format(st))
                cnt_meraki += 1

    print("the input list contains {0} meraki and {1} non meraki numbers".format(cnt_meraki, cnt_non_meraki))


input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]
meraki_helper(input)