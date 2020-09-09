#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-

def addFund(objectNet):
    # 原有基金金额
    oldAmount = 25324.63
    # 原有基金净值
    oldNet = 3.1745
    #
    predictNet = 2.8575
    amount = 1000
    while True:
        newNet = (oldAmount + amount) / (oldAmount / oldNet + amount / predictNet)
        if newNet <= objectNet:
            break
        else:
            print("amount = ", amount)
            print("net = ", newNet)
            amount += 500
    print("最终需要投资 amount = ", amount)

addFund(2.9)
