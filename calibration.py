#dataset1

#ber[]
#inu = input("choose imageredp
redp=22545
greenp= 1148



diff=redp-greenp
ratio=float(redp)/greenp
print(diff)
print(ratio)

#check these two
if(ratio>0.02 and ratio<0.1  and redp>400 and redp<1500 and diff>-10000): #1 error case0010
    print("0011")



elif(redp-greenp>-850   and      diff<0): #1 error case 0111
    print("0000")



elif(redp>greenp*40):      #bada error
    print("1100")



elif(redp>8000):
     if(ratio>2 and ratio<3 and diff>7500):
        print("1111")

     elif(ratio > 1.5 and ratio < 3 and diff < 7500):
         print("1011")

     elif(ratio > 17 and ratio < 22): #error with  1101 #not possible even with difference
         print("1000")

     elif((ratio>6.3)and(ratio<9.5) and diff>10500):
         print("1110")

     elif(ratio > 3 and ratio < 9.5 and diff < 10500 and diff >7500):
         print("1010")

     elif((ratio > 4) and (ratio < 9.5) and diff >8500):
         print("1001")



elif(redp>15000):
         if(ratio > 15 and ratio < 21):  # error with  1000
             print("1101")





elif(redp>500 and redp <3000):  # 3000 can be reduced further
         if(ratio>0.1 and diff>-6000):
          print("0001")
         elif(ratio>0 and diff>-15000):
          print("0010")



if(redp>2500 and greenp<11000):
         if(ratio >4 and ratio <8 and diff>5000 and diff<8000):
             print("0100")

         elif(ratio >0.5 and ratio<2.5 and diff>65 and diff<3000):
             print("0110")

         elif(ratio >1 and ratio<3.8 and diff>2500 and diff<6000): # error with 0110
             print("0101")

         elif (ratio > 0 and ratio < 1.5 and diff < 0) : # error with 0110
             print("0111")

else:
    print("galat")
