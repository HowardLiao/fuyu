# 富宇大地社區管理維護治理體系暨官方數位公佈欄
> Fuyu Dadi Community Governance Handbook, Property Management SOP & Digital Bulletin Board

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-38BDF8?style=flat&logo=github)](https://howardliao.github.io/fuyu/)
[![License](https://img.shields.io/badge/License-MIT-emerald?style=flat)](LICENSE)
[![Design](https://img.shields.io/badge/Theme-Deep%20Obsidian-020617?style=flat)](#)
[![Compliance](https://img.shields.io/badge/MOI-Taiwan%20Condominium%20Act-F59E0B?style=flat)](#)

---

## 專案簡介 (Overview)

本專案為**「富宇大地社區」**打造之全景式數位治理體系平台，嚴格遵循中華民國《公寓大廈管理條例》、內政部《公寓大廈管理服務人管理辦法》及定型化管理維護契約範本（台內營字第 8771990 號令），確立：

> **「物業經理負責把事情做好、做透明；管理委員會負責決定做什麼、並承擔法定決策責任。」**

系統整合高管戰情版面視覺（Deep Obsidian 風格），提供三合一無縫切換架構：
1. **權責規範手冊 (Governance Handbook)**：權責分立、RACI 矩陣、DOA 核決授權表、三級彙報（日報/週報/月報）與法定 7 大類 52 項必備檔卷目錄。
2. **官方數位公佈欄 (Public Bulletin)**：分類篩選、置頂標記、閱讀人次統計與官方電子防偽彈出式閱覽。
3. **後端上稿管理中心 (Admin CMS)**：支援多重身分切換（主任委員、監察委員、財務委員、物業經理）、即時發布、編輯、刪除及 LocalStorage 自動資料持久化與 JSON 備份。

---

## 核心治理體系模組

### 1. 權責定位與 RACI 治理矩陣
- **管理委員會**：法定決策與管理主體（公共基金、重大修繕、招標定約、規約處分）。
- **物業經理 / 服務人**：專業執行人與幕僚長（機電日巡、工單閉環、廠商督考、月會提案）。
- **核決權限 (DOA)**：
  - 零用金例行支出：3,000 元以內。
  - 限額維修請修：3,001 ～ 20,000 元（常委/主委核准）。
  - 重大工程發包：逾 20,000 元（管委會全體常會審議表決）。
  - 緊急突發搶修：20,000 元限額內先行止損，事後補行追認。

### 2. 物業管理 7 大類別 52 項法定檔卷清冊
- **第一類：法定資產與原始建置檔卷**（使用執照、全套管線竣工圖、公設點交報告書等 6 項，永久保存）。
- **第二類：組織架構、規約與會議檔卷**（規約、報備證明、區權會議紀錄、印鑑清冊等 7 項）。
- **第三類：外包採購與契約管理檔卷**（物業契約、保全清潔合約、比價卷宗等 6 項）。
- **第四類：財務會計與公共基金檔卷**（收繳清冊、發票憑證、傳票帳簿、定存單等 6 項，法定 5~10 年）。
- **第五類：法定公共安全、消防與機電運維檔卷**（公安申報、消檢申報、電梯合格證、發電機紀錄等 8 項）。
- **第六類：住戶服務、裝潢施工與違規爭議檔卷**（裝修許可、報修工單、違規存證、存證信函等 7 項）。
- **第七類：日常現場作業與三級週期性彙報檔卷**（日報、週報、月報、交接日誌、重大事故報告等 6 項）。

### 3. 三級週期性彙報體系
- **日報（Daily）**：哨點出勤、機房日巡、住戶請修、施工動態、突發異常、次日待辦。
- **週報（Weekly）**：常會決議進度、工單時效分析、外包廠商 KPI 稽核（保全打卡率 &ge;98%）。
- **月報（Monthly）**：管理費收繳率（目標 98%+）、公積金財務報表、公安消防申報、常會提案審議包。

---

## 本地開發與瀏覽

本平台採純原生前端架構（Single-File Progressive Web Application），無任何外部依賴或編譯打包流程：

```bash
# Clone repository
git clone git@github.com:HowardLiao/fuyu.git

# 開啟網頁
open index.html
```

---

## 作者與版權說明

- **維護發布主體**：富宇大地管理委員會（Fuyu Dadi Management Committee）
- **架構規劃與技術指導**：Howard Liao Ph.D. (廖倫豪 博士)
- **合規依據**：中華民國內政部國土管理署法規規章規範
