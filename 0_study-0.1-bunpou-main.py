# １ 変数の使い方
name1 = 'ねずこ'
name2 = 'ぜんいつ'

print('{}と{}は仲間です'.format(name1, name2))


# ２ if文の使い方
name2 = 'むざん'

if name2 == "むざん":
    print('{}と{}は仲間ではありません'.format(name1, name2))


# ３ 配列の使い方
name_list=["たんじろう","ぎゆう","ねずこ","むざん"]
name_list.append("ぜんいつ")
print(name_list)


# ４ for文の使い方
for n in name_list:
    print(n)


# ５ 関数の使い方
def name(family_name,first_name):
    return family_name + ' ' + first_name

n = name('かまど', 'たんじろう')
print(n)


# ６ 引数を使う関数の使い方
def test(hikisuu):
    if hikisuu in name_list:
        print('{}は含まれます'.format(hikisuu))
    else:
        print('{}は含まれません'.format(hikisuu))

test('たんじろう')
test('ぜんいつ')
test('いのすけ')






