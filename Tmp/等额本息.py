#coding:utf-8
'''
Created on 2016��5��3��

@author: 尹霞
'''

def cut(num):
    tmp = str(num)
    tmp = tmp.split('.')
    num = tmp[0]+'.'+tmp[1][:2]
    return float(num)

#借款人等额本息
def dengebenxiJ(principal,apr,Installments):
    month_apr = apr/12
    tmp = pow((1+month_apr), Installments)
    month_m = (principal * month_apr *tmp)/(tmp-1)
    month_m = round(month_m,2)
    month_interest = 0 #每月利息
    yishou =0
    count =0
    count1=0
    count2=0
    print ("本金：%s, 年利率：%s, 期数: %s 的等额本息还款金额计算"%(principal,apr,Installments)   )
    #每月月供额使用四舍五入
    print ("每月月供额:%s" %month_m      )
    for i in range(Installments):
        tmp2 = pow((1+month_apr), (i+1-1))
        #month_principal = (principal * month_apr * tmp2)/(tmp-1)
        #month_interest =  round(principal * month_apr * (tmp - tmp2)/(tmp-1),2)
        new = (principal * month_apr - month_m) * tmp2 + month_m
        month_interest = round(new,2)
        if i == Installments-1:
            month_principal = principal - yishou

            count=count+month_principal+month_interest
            count1 = count1+month_principal
            count2 = count2+month_interest

            print( "借款人第 %s 期应还本金：%s，应还利息%s" %(i+1,month_principal,month_interest))
            print( "待还金额：%s,待还本金：%s,待还利息：%s" %(count,count1,count2))
        else:
           month_principal =  month_m-month_interest
           yishou = yishou + month_principal

           count=count+month_principal+month_interest
           count1 = count1+month_principal
           count2 = count2+month_interest

           print("借款人第 %s 期应还本金：%s，应还利息%s" %(i+1,month_principal,month_interest)  )


#投资人
#等额本息计算公式：〔贷款本金×月利率×（1＋月利率）＾还款月数〕÷〔（1＋月利率）＾还款月数－1〕
def dengebenxiT(principal,apr,Installments):
    month_apr = apr/12#月利率
    tmp = pow((1+month_apr), Installments)
    month_m = cut((principal * month_apr *tmp)/(tmp-1))
    yishou =0
    month_interest = 0 #每月利息
    print( "本金：%s, 年利率：%s, 期数: %s 的等额本息还款金额计算"%(principal,apr,Installments)   )
    print ("每月月供额:%s" % month_m                               )
    count =0
    count1=0
    count2=0

    for i in range(Installments):
        tmp2 = pow((1+month_apr), (i+1-1))
        #month_principal = (principal * month_apr * tmp2)/(tmp-1)
        tmp3 = principal * month_apr * (tmp - tmp2)/(tmp-1)

        new = (principal * month_apr - month_m) * tmp2 + month_m

        month_interest = cut(new)
        if i == Installments-1:
            month_principal = principal - yishou
            count=count+month_principal+month_interest
            count1 = count1+month_principal
            count2 = count2+month_interest

            print( "投资人第 %s 期应还本金：%s，应还利息%s" %(i+1,month_principal,month_interest)   )
            print( "待还金额：%s,待还本金：%s,待还利息：%s" %(count,count1,count2))
        else:
           month_principal =  month_m - month_interest
           yishou = yishou + month_principal

           count=count+month_principal+month_interest
           count1 = count1+month_principal
           count2 = count2+month_interest

           #print yishou
           print ("投资人第 %s 期应还本金：%s，应还利息%s" %(i+1,month_principal,month_interest)      )
          # print count

def reply(principal,apr,Instsallments):
    pass

if __name__ == '__main__':
    #本金 年利率 期数
    #dengebenxiJ(950.45,0.1203,5)
    #dengebenxiT(950.45,0.1203,5)
    dengebenxiT(300000,0.0455,240)
    #dengebenxiJ(10000,0.1102,12)




    #print cut(2.349)
    # raw_input('please click enter to exit');
