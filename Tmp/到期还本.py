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
        print '******����˰��»���*********'
    elif s == 't':
        month_m = principal * apr / 365
        print '******����˰��컹��*********'
        
    month_m = round(month_m,2) 
    
    for i in range (int(Installments[:-1])):
        if i == int(Installments[:-1])-1:
            print "�� %s �ڻ����ܶ%s , Ӧ������%s ��Ӧ����Ϣ��%s" %(i+1,month_m+principal,principal,month_m)
        else:
            print "�� %s �ڻ����ܶ%s , Ӧ������%s ��Ӧ����Ϣ��%s" %(i+1,month_m,0,month_m)

    print '*****************************'


def daoqihuanbenT(principal,apr,Installments):
    s = Installments[-1]
    if s == 'y':
        month_m = principal * apr / 12
        print '******Ͷ���˰����տ�*********'
    elif s == 't':
        month_m = principal * apr / 365
        print '******Ͷ���˰����տ�*********'
        
    month_m = float(cutOut(month_m))
  
    for i in range (int(Installments[:-1])):
        if i == int(Installments[:-1])-1:
            print "�� %s �ڻ����ܶ%s , Ӧ������%s ��Ӧ����Ϣ��%s" %(i+1,month_m+principal,principal,month_m)
        else:
            print "�� %s �ڻ����ܶ%s , Ӧ������%s ��Ӧ����Ϣ��%s" %(i+1,month_m,0,month_m)

    print '*****************************'


if __name__ == '__main__':
    daoqihuanbenJ(10000, 0.1102, '3y')
    daoqihuanbenT(29139, 0.115, '3t')
