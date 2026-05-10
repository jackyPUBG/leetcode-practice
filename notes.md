# LeetCode 解題筆記

## 解題思路三步驟
1. 要做什麼？
2. 需要什麼資料？
3. 用什麼方法？

## 學到的工具

| 工具 | 用法 | 例子 |
|---|---|---|
| `[::-1]` | 反轉字串或 list | `s == s[::-1]` 判斷回文 |
| `range(i+1, len(nums))` | 從 i+1 開始，避免重複 | Two Sum 雙層迴圈 |
| List Comprehension | 簡化 for 迴圈 | `[int(x) for x in str(n)]` |
| `"".join(...)` | 把 list 合併成字串 | `"".join(str(x) for x in digits)` |
| stack | 後進先出，處理配對問題 | Valid Parentheses |
| Binary Search | O(log n)，每次砍一半 | Search Insert Position |
| `.shift(1)` | 取得上一行的值 | 判斷集保戶數是否減少 |
| `.rolling(n).sum()` | 連續 n 天加總 | 判斷連續三天買超 |
