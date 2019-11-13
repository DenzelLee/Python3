def cutOut(pInNum):
    #aa = 22.13754
    bb = '%s' % pInNum
    cc = bb.split('.')
    dd = cc[0]+'.'+cc[1][:2]
    return dd


def daoqihuanbenJ(principal,apr,Installments):
    s = Installments[-1]
    if s == 'y':
        month_m = principal * apr / 12
        print '******借款人按月还款*********'
    elif s == 't':
        month_m = principal * apr / 365
        print '******借款人按天还款*********'
        
    month_m = round(month_m,2) 
    
    for i in range (int(Installments[:-1])):
        if i == int(Installments[:-1])-1:
            print "第 %s 期还款总额：%s , 应还本金：%s ，应还利息：%s" %(i+1,month_m+principal,principal,month_m)
        else:
            print "第 %s 期还款总额：%s , 应还本金：%s ，应还利息：%s" %(i+1,month_m,0,month_m)

    print '*****************************'


def daoqihuanbenT(principal,apr,Installments):
    s = Installments[-1]
    if s == 'y':
        month_m = principal * apr / 12
        print '******投资人按月收款*********'
    elif s == 't':
        month_m = principal * apr / 365
        print '******投资人按天收款*********'
        
    month_m = float(cutOut(month_m))
  
    for i in range (int(Installments[:-1])):
        if i == int(Installments[:-1])-1:
            print "第 %s 期还款总额：%s , 应还本金：%s ，应还利息：%s" %(i+1,month_m+principal,principal,month_m)
        else:
            print "第 %s 期还款总额：%s , 应还本金：%s ，应还利息：%s" %(i+1,month_m,0,month_m)

    print '*****************************'


if __name__ == '__main__':
    daoqihuanbenJ(10000, 0.1102, '3y')
    daoqihuanbenT(29139, 0.115, '3t')
