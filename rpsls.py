#coding=gbk
"""
Ŀ�ģ����RPSLS��Ϸ
����:������
"""
import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��
def name_to_number(name):
	"""
	 ����Ϸ�����Ӧ����ͬ������
	 """
	if name=="ʯͷ":
		number=0
	elif name=="ʷ����":
		  number=1
	elif name=="ֽ":
		  number=2
	elif name=="����":
		  number=3
	elif name=="����":
		  number=4
	return number

def number_to_name(number):
	"""
	��������0��1��2��3��4����Ӧ����Ϸ�Ĳ�ͬ����
	"""
	if number==0:
		name="ʯͷ"
	elif number==1:
		name="ʷ����"
	elif number==2:
		name="ֽ"
	elif number==3:
		name="����" 
	else:
		name="����"
	return name


import random
com_number=random.randrange(0,5)
def rpsls(player_choice):
	player_choice=name_to_number(player_choices)
	name=number_to_name(com_number)
	print("--------")
	print("����ѡ��Ϊ%s"%player_choices)
	print("�������ѡ��Ϊ%s"%name)
	if player_choice==0 and com_number==4:
	    print("��Ӯ��")
	elif player_choice==0 and com_number==3:
	    print("��Ӯ��")   
	elif player_choice==0 and com_number==1:
	    print("����Ӯ��")
	elif player_choice==0 and com_number==2:
	    print("����Ӯ��")	
	elif player_choice==1 and com_number==4:
	    print("��Ӯ��")       
	elif player_choice==1 and com_number==0:
	    print("��Ӯ��")
	elif player_choice==1 and com_number==3:
	    print("����Ӯ��")
	elif player_choice==1 and com_number==2:
	    print("����Ӯ��")	
	elif player_choice==2 and com_number==0:
	    print("��Ӯ��")
	elif player_choice==2 and com_number==1:
	    print("��Ӯ��")
	elif player_choice==2 and com_number==3:
	    print("����Ӯ��")
	elif player_choice==2 and com_number==4:
	    print("����Ӯ��")	
	elif player_choice==3 and com_number==1:
	    print("��Ӯ��")
	elif player_choice==3 and com_number==2:
	    print("��Ӯ��")
	elif player_choice==3 and com_number==4:
	    print("����Ӯ��")
	elif player_choice==3 and com_number==0:
	    print("����Ӯ��")	
	elif player_choice==4 and com_number==3:
	    print("��Ӯ��")
	elif player_choice==4 and com_number==2:
	    print("��Ӯ��")
	elif player_choice==4 and com_number==1:
	    print("����Ӯ��")	
	elif player_choice==4 and com_number==0:
	    print("����Ӯ��")
	else:
	    print("���ͼ��������һ����")
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��")
player_choices=input()
if player_choices=="ʯͷ":
	rpsls(player_choices)
elif player_choices=="ֽ":
	rpsls(player_choices)
elif player_choices=="ʷ����":
	rpsls(player_choices)
elif player_choices=="����":
	rpsls(player_choices)
elif player_choices=="����":
	rpsls(player_choices)
else:
	print("Error: No Correct Name")

