# BCA法
# 曲线方程为：y = 970.61x - 17.806 PBS
#y = 1045x - 33.974 变性液

# R² = 0.9916

print("欢迎实用BCA定量法测蛋白浓度背景为PBS")
od562 = float(input("请输入酶标仪所测数据值-->"))

def bca_pbs(od562):
    pron = (970.61 * od562) - 17.806
    return pron

def bca_ripa(od562):
    pron = 1045 * od562 - 33.974
    return pron

select = int(input("背景液为PBS还是RIPA？\n--->1 PBS\n---->2 RIPA\n"))

if select == 1:
        bca_pbs(od562)
        break
    elif select == 2:
        bca_ripa(od562)
        break
    else:
        print("您输入有误，请重新输入")

print("您的蛋白浓度为：%.2f ug/mL"% pron)



