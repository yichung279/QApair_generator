# QApair_generator
a program generating QApair dataset


#規則
[]內是可以抽換的字詞
[?]表示可加可不加
每個類別都有一問一答

# what will we do 

40家店 4種問種類 每個種類 x種問法 y種回答
共 40 * (x1y1 + x2y2 + x3y3 + x4y4) QApair
現在我也算不出有幾種了


## 時間
### 問
* [請問?][長榮路上的?][小茂屋]的營業時間是什麼時候
* [請問?][長榮路上的?][小茂屋]什麼時候營業
* [請問?]什麼時候是[長榮路上的?][小茂屋]的營業時間
* [請問?]什麼時候[長榮路上的?][小茂屋]營業
* [請問?][長榮路上的?][小茂屋]什麼時候有開
### 答
* [長榮路上的?][小茂屋]從[10:00-22:00]都有營業
* [長榮路上的?][小茂屋]從[10:00-22:00]有開
* [長榮路上的?][小茂屋]的營業時間從[10:00-22:00]
* 從[10:00-22:00][長榮路上的?],[小茂屋]都有開

## 地點
### 問
* [請問?][長榮路上的?][小茂屋]在哪裡?
* [請問?]我該怎麼去[長榮路上的?][小茂屋]？
* [請問?][長榮路上的?][小茂屋]怎麼走？

### 答
* [長榮路上的?][小茂屋]的營業地點在[長榮路]
* [長榮路上的?][小茂屋]在[長榮路上]
* [長榮路上的?][小茂屋]開在[長榮路上]
* 在[長榮路上]就能找到[長榮路上的?][小茂屋]

## 電話
###問
* [請問?][長榮路上的?][小茂屋]的電話是幾號?
* [請問?][長榮路上的?][小茂屋]電話多少?
* [請問?]我該怎麼連絡[長榮路上的?][小茂屋]?
###答
* [長榮路上的?][小茂屋]的電話是[09xxxxxx/06xxxxx]
* 打[09xxxxxx/06xxxxx]就可以聯絡到[長榮路上的?][小茂屋]
* [09xxxxxx/06xxxxx]是[長榮路上的?][小茂屋]的電話

## 關於評價 n句
從 google map 亂抓很多句，隨機加在回答前後。

