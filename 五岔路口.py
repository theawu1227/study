# s_t = """0	0	0	0	1	1	1	0	0	1	1	0	0
# 0	0	0	0	1	0	1	1	0	1	1	0	0
# 0	0	0	0	0	0	0	0	0	1	1	1	0
# 0	0	0	0	0	0	0	0	0	0	0	0	0
# 1	1	0	0	0	0	1	0	0	1	1	1	0
# 1	0	0	0	0	0	0	1	0	0	1	0	0
# 1	1	0	0	1	0	0	0	0	0	1	1	0
# 0	1	0	0	0	1	0	0	0	0	0	1	0
# 0	0	0	0	0	0	0	0	0	0	0	0	0
# 0	1	1	0	1	0	0	0	0	0	0	0	0
# 1	1	1	0	1	1	1	0	0	0	0	0	0
# 1	0	1	0	1	0	1	1	0	0	0	0	0
# 0	0	0	0	0	0	0	0	0	0	0	0	0"""
# b = []
# for s in s_t.replace('\t', ',').split('\n'):
#     b1 = []
#     for dd in s.split(','):
#         num = eval(dd)
#         b1.append(num)
#     b.append(b1)
# print(b)


def dye(jd, color_num):
    if jd == 13:
        print(color_num)
        exit(0)
    # 依次测试每一种颜色(此时颜色用从0开始的数字表示)
    for i in range(color_num):
        # 第 jd 条道路的指示灯为颜色 i
        a[jd] = i
        bool = True
        # 进行冲突测试
        # 假设jd 是主要考虑道路，则j为次道路，该循环用于测试两条道路是否为冲突道路
        # 此处的j 不会循环所有的道路，只会循环以赋予颜色的道路，其余道路依旧默认为颜色0
        for j in range(jd):
            # 如果在道路列表中 主线路指示灯颜色与次道路颜色一致，
            # 并且 在冲突列表中jd和j互为冲突道路，则跳出当前测试冲突的循环
            # 冲突道路颜色不能一致
            if a[jd] == a[j] and b[jd][j] == 1:
                bool = False
                print('冲突道路，重新赋予指示灯颜色')
                break
        if bool is True:
            # 当前道路测试完毕，迭代下一个道路
            dye(jd + 1, color_num)

        # 如果bool为False, 则证明当前道路颜色i，与前面已经赋予颜色的道路，存在冲突道路，
        # 所以需要更换当前主道路的知识灯颜色

        # 例：
        # [ab,ac,ad,ba,bd·····]
        # 假如现在迭代到了bd（4）,已知他和ab（0）为冲突道路，冲突列表中的[0][4] == 1 冲突成立，跳出冲突循环
        # bool 为False 进行下一个颜色的测试
        # 直至13个道路颜色检测完毕，且没有冲突道路颜色相同的状况出现，完成程序


if __name__ == '__main__':
    # # 最少2种颜色，最多13种
    # # 一共有13种交通路线 ，默认每一条路线的颜色为0
    # # todo [AB,AC,·····,EC] 将a定义为道路列表
    a = [0 for i in range(13)]
    # # 1 代表两条路径有交叉点，道路冲突，不能同时为同一种颜色
    # # todo b定义为冲突列表
    b = [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
         [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
         [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for color_num in range(2, 14):
        # 每考虑一次可能出现的颜色种类，就默认从一条道路出发，如从AB开始
        # 传入的0 指的是 已经创建的a列表的下标的第一个元素的交通灯
        dye(0, color_num)
        # 如果2种颜色不能满足13条道路的完全不冲突，则增加颜色考虑情况


