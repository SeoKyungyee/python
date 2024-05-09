dict_1 = {'name': '홍길동', 'birth': 1990, 'addr': 'KR'}
print(dict_1)
print(dict_1['birth'])

dict_1['weight'] = 60.5
dict_1['family'] = ['아빠', '엄마', '여동생']
print(dict_1)

dict_1.update({'weight':67.8,'hobby': ['게임', '독서']})
print(dict_1)

dict_1['hobby'] = ['축구','등산']
print(dict_1)

del dict_1['weight']
del dict_1['birth']
del dict_1['addr']
print(dict_1)