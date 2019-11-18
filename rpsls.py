#coding=gbk
"""
目的：完成RPSLS游戏
作者:陈欣妍
"""
import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数
def name_to_number(name):
	"""
	 将游戏对象对应到不同的整数
	 """
	if name=="石头":
		number=0
	elif name=="史波克":
		  number=1
	elif name=="纸":
		  number=2
	elif name=="蜥蜴":
		  number=3
	elif name=="剪刀":
		  number=4
	return number

def number_to_name(number):
	"""
	将整数（0，1，2，3，4）对应到游戏的不同对象
	"""
	if number==0:
		name="石头"
	elif number==1:
		name="史波克"
	elif number==2:
		name="纸"
	elif number==3:
		name="蜥蜴" 
	else:
		name="剪刀"
	return name


import random
com_number=random.randrange(0,5)
def rpsls(player_choice):
	player_choice=name_to_number(player_choices)
	name=number_to_name(com_number)
	print("--------")
	print("您的选择为%s"%player_choices)
	print("计算机的选择为%s"%name)
	if player_choice==0 and com_number==4:
	    print("您赢了")
	elif player_choice==0 and com_number==3:
	    print("您赢了")   
	elif player_choice==0 and com_number==1:
	    print("电脑赢了")
	elif player_choice==0 and com_number==2:
	    print("电脑赢了")	
	elif player_choice==1 and com_number==4:
	    print("您赢了")       
	elif player_choice==1 and com_number==0:
	    print("您赢了")
	elif player_choice==1 and com_number==3:
	    print("电脑赢了")
	elif player_choice==1 and com_number==2:
	    print("电脑赢了")	
	elif player_choice==2 and com_number==0:
	    print("您赢了")
	elif player_choice==2 and com_number==1:
	    print("您赢了")
	elif player_choice==2 and com_number==3:
	    print("电脑赢了")
	elif player_choice==2 and com_number==4:
	    print("电脑赢了")	
	elif player_choice==3 and com_number==1:
	    print("您赢了")
	elif player_choice==3 and com_number==2:
	    print("您赢了")
	elif player_choice==3 and com_number==4:
	    print("电脑赢了")
	elif player_choice==3 and com_number==0:
	    print("电脑赢了")	
	elif player_choice==4 and com_number==3:
	    print("您赢了")
	elif player_choice==4 and com_number==2:
	    print("您赢了")
	elif player_choice==4 and com_number==1:
	    print("电脑赢了")	
	elif player_choice==4 and com_number==0:
	    print("电脑赢了")
	else:
	    print("您和计算机出的一样呢")
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择：")
player_choices=input()
if player_choices=="石头":
	rpsls(player_choices)
elif player_choices=="纸":
	rpsls(player_choices)
elif player_choices=="史波克":
	rpsls(player_choices)
elif player_choices=="蜥蜴":
	rpsls(player_choices)
elif player_choices=="剪刀":
	rpsls(player_choices)
else:
	print("Error: No Correct Name")

