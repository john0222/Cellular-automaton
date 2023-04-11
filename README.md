# Cellular-automaton
a small-scale cellular automaton build practice

# 螢幕上的生物—細胞自動機之細胞模擬
郭家毓 於4/10修改
Github QR Code 在此，此處與此代碼庫未來將同步更新


## 概覽
1.	細胞自動機是什麼
3.	程式的具體實踐方法與剖析
4.	程式源碼一覽
5.	成果展示
6.	心得與感想

## 細胞自動機是甚麼
細胞自動機是一種基於格子和規則的計算模型，被廣泛應用於生物學和生物工程領域。細胞自動機可以模擬許多生物過程，包括細胞分裂、細胞運動、細胞分化、組織發育等等。細胞自動機的主要優點是它可以提供高度可視化的模擬，使我們能更好地理解和預測生物動作模式。
在生物學中，細胞自動機直接被用於研究細胞行為、細胞運動、細胞分裂等等生物學問題。例如，研究人員可以使用細胞自動機來模擬細胞分裂過程，從而了解細胞分裂時細胞器的運動、染色體的排列等等細節。此外，細胞自動機還可以用於模擬細胞運動和細胞分化，這對於研究癌症轉移、發育過程等問題有相當大的助益。
在生物工程中，細胞自動機被用於設計和優化生物系統。例如，研究人員可以使用細胞自動機模擬細胞內代謝路徑的運作，從而設計更有效的酶工程系統。此外，細胞自動機還可以用於模擬細胞培養過程，從而優化細胞培養條件，提高產品產量。
總結以上，細胞自動機在生物學和生物工程中具有廣泛的應用價值，也對醫學技術的相關領域發展有所貢獻。

## 程式的具體實踐方法與剖析

```python=
import pygame
import numpy as np
```
這兩行引入了pygame和numpy，是我們所需要用到的
```python=
pygame.init()
width, height = 500, 500
WINDOW_SIZE = (width, height)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("簡易細胞動態模擬程式 v1.0 alpha")
```
這部分初始化了pygame的顯示視窗，創建了一個寬度為500，高度為500像素的視窗，設置了視窗的標題。

```python=
BLACK = (0,38, 111)
WHITE = (255, 255, 255)
size = 5
gw, gh = width // size, height // size

# 細胞狀態隨機初始化
grid = np.random.randint(2, size=(gw, gh))
```
這段定義了顏色變量，用於在顯示視窗中繪製細胞。
也定義了細胞的大小size，以及網格的大小width和height，網格的大小通過視窗的大小和細胞大小進行計算得出

```python=
def evolve(state, neighbors):
    alive_neighbors = np.sum(neighbors)
    if state == 1:
        if alive_neighbors < 2 or alive_neighbors > 3:
            return 0
        else:
            return 1
    else:
        if alive_neighbors == 3:
            return 1
        else:
            return 0
```
evolve函式定義細胞動作規則，該函數讀入兩個參數：細胞的當前狀態state和其相鄰細胞格的狀態數neighbors。函數根據以下規則來決定細胞的下一個狀態：如果細胞當前為1且其鄰居數量少於2或大於3，則下一個狀態為0；如果細胞當前為0且其鄰居數量等於3，則下一個狀態為1；否則保持不變。

```python=
def evolve_grid(grid):
    new_grid = np.zeros_like(grid)
    for i in range(gw):
        for j in range(gh):
            neighbors = grid[(i-1):(i+2), (j-1):(j+2)]
            neighbors_sum = np.sum(neighbors) - grid[i, j]
            new_grid[i, j] = evolve(grid[i, j], neighbors_sum)
    return new_grid
```
這個evolve_grid函數，該函數讀入一個二維數組grid作為參數，並輸出一個新的二維數組new_grid，表示經過一次細胞演化後的網格狀態。函數遍歷網格系統中的每個細胞，並計算其鄰居的狀態來計算每個細胞的下一個狀態，最終將新狀態更新在new_grid中。
```python=
while True:
    #開搞
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
           # sys.exit()

    # Evolve the grid and redraw it
    grid = evolve_grid(grid)
    draw_grid(grid)
    pygame.display.flip()
```
最後這裡是程式的主要執行區域，在每次循環中，首先檢查是否有QUIT事件（就是檢查視窗是否被關閉），如果有，則設置running變量為False以結束程式。清空視窗並繪製所有存活的細胞。接著，程序調用evolve_grid函數計算下一個系統狀態，並將新的網格狀態存儲在grid變量中。最後通過pygame.display.flip()更新顯示狀態。當running變量為False時，程序退出主執行區並結束程序的執行。draw_grid的算繪函示這裡就不多做說明。

**<font color="#f00">簡易的流程如下圖</font>**
```flow
st=>start: 開始
op1=>operation: 初始化 pygame
op2=>operation: 創建初始的細胞網格
sub1=>subroutine: 進入主循環
op3=>operation: 檢查是否有QUIT事件
cond1=>condition: QUIT事件?
op4=>operation: 清空視窗
op5=>operation: 繪製所有存活的細胞
op6=>operation: 計算下一個網格狀態
op7=>operation: 將新的網格狀態存儲在grid變量中
op8=>operation: 更新顯示視窗
op9=>operation: 等待下一個循環
cond2=>condition: 結束程序?
op10=>operation: 結束 pygame
e=>end: 結束

st->op1->op2->sub1
sub1->op3->cond1
cond1(yes)->op10
cond1(no)->op4->op5->op6->op7->op8->op9->cond2
cond2(no)->sub1
cond2(yes)->op10->e


```



## 程式源碼一覽

這裡是全部區塊組合成的完整程式碼
```pyton=
import pygame
import numpy as np

#pygame設定環節
pygame.init()
width, height = 500, 500
WINDOW_SIZE = (width, height)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("簡易細胞動態模擬程式 v1.0 alpha")

# 可以色色與設網格
BLACK = (0,38, 111)
WHITE = (255, 255, 255)
size = 5
gw, gh = width // size, height // size

# 細胞狀態隨機初始化
grid = np.random.randint(2, size=(gw, gh))

#細胞規則
def evolve(state, neighbors):
    alive_neighbors = np.sum(neighbors)
    if state == 1:
        if alive_neighbors < 2 or alive_neighbors > 3:
            return 0
        else:
            return 1
    else:
        if alive_neighbors == 3:
            return 1
        else:
            return 0

#動作函數
def evolve_grid(grid):
    new_grid = np.zeros_like(grid)
    for i in range(gw):
        for j in range(gh):
            neighbors = grid[(i-1):(i+2), (j-1):(j+2)]
            neighbors_sum = np.sum(neighbors) - grid[i, j]
            new_grid[i, j] = evolve(grid[i, j], neighbors_sum)
    return new_grid

#純顯示
def draw_grid(grid):
    screen.fill(BLACK)
    for i in range(gw):
        for j in range(gh):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (i*size, j*size, size, size))

while True:
    #開搞
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
           # sys.exit()

    # Evolve the grid and redraw it
    grid = evolve_grid(grid)
    draw_grid(grid)
    pygame.display.flip()


```

## 成果展示

![](https://i.imgur.com/KetJvyT.png)
開始執行的初始狀態


![](https://i.imgur.com/APKBiOB.png)
後期細胞早已存活不多

### **影片紀錄**

{%youtube i59Nmr5IwJs %}

:::info
:bulb: 原始影片從初始狀態到完全無細胞動作的最終狀態耗時相當久，故影片經過後製快轉與增加說明
:::


## 心得與感想
因為我一直以來做的都是以程式為主軸導向的自主學習，但我對生物與醫學也有相當的興趣，然而這方面的實作相對麻煩，資源也比較少，所以我就開始思考有哪些課題是能夠簡單的創造實質成果而非單純的文獻研討與分析，我第一個想到的便是將我的技能(寫程式)和興趣(生物醫學與engineering)結合在一起，所以我創造了這個簡易的小程式來模擬生物細胞的動作模式，不但滿足了生物與工程方面的技能要求，也使我藉著程式撰寫加強磨練了邏輯能力，可謂是一舉數得。
由於像素的特性與視窗大小的限制，目前我無法將細胞做到完全閉合或貼近於真實，這是源於專業知識不足的問題，將來會再繼續深入研究並修改程式碼或新增功能來完善這組專案。
