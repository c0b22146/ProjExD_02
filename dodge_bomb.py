import sys
import pygame as pg
import random


WIDTH, HEIGHT = 1600, 900

def check_bound(rect: pg.rect) -> tuple[bool,bool]: #画面外に出た時の判定
    yoko,tate = True,True
    if rect.left <= 0 or WIDTH <= rect.right: #縦の判定
        yoko = False
    if rect.top <= 0 or HEIGHT <= rect.bottom: #横の判定
        tate = False
    return yoko,tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900,400
    clock = pg.time.Clock()
    tmr = 0

    vx = 5 #横方向速度 #練習2
    vy = 5 #縦方向速度

    enn = pg.Surface((20,20)) #練習1
    pg.draw.circle(enn,(255,0,0),(10,10),10)
    enn.set_colorkey((0,0,0))
    # 黒い部分の透明化
    xx = random.randint(0,WIDTH)
    yy = random.randint(0,HEIGHT)
    # 円の座標の乱数
    enn_rct = enn.get_rect()
    enn_rct.center = xx,yy
    # 円の座標の抽出

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return    
        if kk_rct.colliderect(enn_rct):
            print("ゲームオーバー")
            return #ゲームオーバー
        合計移動量 = [0,0] #練習3
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:合計移動量[1] -= 5
        if key_lst[pg.K_DOWN]:合計移動量[1] += 5  #キー押下時の処理
        if key_lst[pg.K_LEFT]:合計移動量[0] -= 5
        if key_lst[pg.K_RIGHT]:合計移動量[0] += 5
        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(合計移動量[0],合計移動量[1])

        if check_bound(kk_rct) != (True,True):
            kk_rct.move_ip(-合計移動量[0],-合計移動量[1]) 
            #こうかとんの位置を更新前に戻す

        screen.blit(kk_img, kk_rct) 
        #こうかとんの移動処理
        enn_rct.move_ip(vx,vy)
        # 円の移動処理
        yoko,tate = check_bound(enn_rct)
        if not yoko:
            vx *= -1 #横方向の速度を反転させる
        if not tate:
            vy *= -1 #縦方向の速度を反転させる
        screen.blit(enn,enn_rct)
        # 円の描画
        pg.display.update()
        tmr += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()