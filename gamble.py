import random

G = 1000
print()
print()
print()
print()

print("コインの表と裏で賭けをします。表なら勝ち、裏なら負けです。")
print()
print()
win = 0
lose = 0
#play = 1
#play = input("賭けをしますか？　はい:1 いいえ:0")
#while play != 1 or 0:
    #print("無効な数値です")
#    play = input("賭けをしますか？　はい:1 いいえ:0")

while G > 1:
    print("勝ち:", win, "負け:", lose)
    print()
    print("所持金:", G, "円")
    print()
    bet = input("掛け金を決めてください。")
    b = int(bet)
    coin = random.randint(0, 1)
    print()
    print()
    print()
    if coin == 0:
        G = G - b
        lose = lose + 1
        print()
        print("裏です。あなたは負けました。 -", b, "円")
        print()
        print("のこり", G, "円")
        print()
    else:
        G = G + b
        win = win + 1
        print()
        print("表です。あなたは勝ちました。　+", b, "円")
        print()
        print("のこり", G, "円")
        print()
print()
print()
print("所持金がなくなりました。")
