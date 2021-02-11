THRESHOLD_LOWER = 6
THRESHOLD_UPPER = 8
StateNum = 8
InitState = 0
target = [7]

ActionNum = 11
choices = [(0,0), (0,1), (1,2), (1,3), (2,4), (3,5), (4,6), (4,7), (5,8), (6,9), (7,10)]

trans = {(0,0,1):1, (0,1,7):1, (1,2,3):1, (1,3,2):1, (2,4,4):1, (3,5,6):1, (4,6,6):1, (4,7,5):1, (5,8,7):1, (6,9,7):1, (7,10,7):1}
action_str = """action0: b  action1: a  action2: d  action3: c  action4: e  action5: f  action6: h  action7: g  action8: i  action9: j  action10: stop  """

RewardNum = 1
reward = {(0,0,0,1):2, (0,0,1,7):6, (0,1,2,3):2, (0,1,3,2):1, (0,2,4,4):2, (0,3,5,6):5, (0,4,6,6):2, (0,4,7,5):1, (0,5,8,7):2, (0,6,9,7):3}
rewards_str = """reward0: dist  """

