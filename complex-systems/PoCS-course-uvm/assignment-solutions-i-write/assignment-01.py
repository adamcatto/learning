from sklearn import linear_model
import numpy as np

wr01 = 6+(30.74/60)
wr02 = 5+(59.72/60)
wr04 = 5+(32.26/60)
wr08 = 5+(18.68/60)

pair01 = (1,wr01)
pair02 = (2,wr02)
pair04 = (4,wr04)
pair08 = (8,wr08)

wrv01 = 2000.0/wr01
wrv02 = 2000.0/wr02
wrv04 = 2000.0/wr04
wrv08 = 2000.0/wr08

pairv01 = (1,wrv01)
pairv02 = (2,wrv02)
pairv04 = (4,wrv04)
pairv08 = (8,wrv08)

list1=[1,2,4,8]
list2=[wrv01,wrv02,wrv04,wrv08]
list1fit=[np.log2(x) for x in list1]
list2fit=[np.log2(x) for x in list2]
list1fit=np.reshape(list1fit,(-1,1))
list2fit=np.reshape(list2fit,(-1,1))
reg = linear_model.LinearRegression()
reg.fit(list1fit,list2fit)
print(reg.coef_)
