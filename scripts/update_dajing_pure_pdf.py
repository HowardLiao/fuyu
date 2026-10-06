# -*- coding: utf-8 -*-
import os

html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>富宇大境（A2 區・6 戶）法定獨立分割卷宗與專案報告下載專區</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Noto+Serif+TC:wght@400;600;700;900&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-deep: #0B0F19;
      --bg-card: #151B28;
      --bg-card-hover: #1A2233;
      --gold-primary: #D4AF37;
      --gold-bright: #F59E0B;
      --gold-light: #E6D5AC;
      --gold-dark: #B8860B;
      --text-main: #FFFFFF;
      --text-muted: #94A3B8;
      --border-gold: rgba(212, 175, 55, 0.35);
      --border-subtle: rgba(255, 255, 255, 0.1);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-deep);
      color: var(--text-main);
      font-family: 'Noto Sans TC', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      padding-bottom: 60px;
      overflow-x: hidden;
    }

    /* Ambient Gold Glow */
    .glow-top {
      position: absolute;
      top: -150px;
      left: 50%;
      transform: translateX(-50%);
      width: 800px;
      height: 400px;
      background: radial-gradient(circle, rgba(212, 175, 55, 0.15) 0%, rgba(11, 15, 25, 0) 70%);
      pointer-events: none;
      z-index: 0;
    }

    .container {
      max-width: 1040px;
      margin: 0 auto;
      padding: 0 24px;
      position: relative;
      z-index: 1;
    }

    /* Header */
    header {
      padding: 44px 0 28px;
      text-align: center;
      border-bottom: 1px solid var(--border-gold);
    }

    .tag-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      background: rgba(212, 175, 55, 0.12);
      border: 1px solid var(--gold-primary);
      border-radius: 9999px;
      color: var(--gold-primary);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 1px;
      margin-bottom: 14px;
    }

    h1 {
      font-family: 'Noto Serif TC', serif;
      font-size: 2.2rem;
      font-weight: 900;
      color: var(--text-main);
      margin-bottom: 10px;
      letter-spacing: 0.5px;
      line-height: 1.3;
    }

    h1 span {
      color: var(--gold-primary);
    }

    .subtitle {
      color: var(--gold-light);
      font-size: 1.02rem;
      font-weight: 500;
      max-width: 800px;
      margin: 0 auto 18px;
    }

    .reporter-bar {
      display: inline-flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 16px;
      font-size: 0.86rem;
      color: var(--text-muted);
      background: rgba(21, 27, 40, 0.6);
      padding: 8px 20px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
    }

    .reporter-bar strong {
      color: var(--gold-bright);
    }

    /* 4-Bento Summary Bar */
    .bento-stats {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin: 28px 0 36px;
    }

    .bento-card {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 16px 18px;
      position: relative;
      overflow: hidden;
    }

    .bento-card.highlight {
      border-color: var(--gold-primary);
      box-shadow: 0 0 20px rgba(212, 175, 55, 0.12);
    }

    .bento-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background: var(--gold-primary);
      opacity: 0.4;
    }

    .bento-card.highlight::before {
      opacity: 1;
      background: linear-gradient(to bottom, var(--gold-bright), var(--gold-primary));
    }

    .bento-label {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 500;
      margin-bottom: 2px;
    }

    .bento-val {
      font-family: 'Cinzel', serif;
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 2px;
    }

    .bento-card.highlight .bento-val {
      color: var(--gold-primary);
    }

    .bento-desc {
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    /* Section Title */
    .section-title {
      font-family: 'Noto Serif TC', serif;
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--gold-primary);
      margin: 32px 0 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .section-title::after {
      content: '';
      flex: 1;
      height: 1px;
      background: var(--border-subtle);
    }

    /* Dossier List Card */
    .dossier-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .dossier-row {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 20px 24px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      transition: all 0.2s ease;
    }

    .dossier-row:hover {
      background: var(--bg-card-hover);
      border-color: var(--gold-primary);
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.3);
    }

    .dossier-row.spotlight {
      background: linear-gradient(135deg, rgba(21, 27, 40, 0.95) 0%, rgba(30, 40, 60, 0.95) 100%);
      border: 1.5px solid var(--gold-primary);
      box-shadow: 0 0 25px rgba(212, 175, 55, 0.15);
    }

    .dossier-meta {
      display: flex;
      align-items: flex-start;
      gap: 16px;
      flex: 1;
      min-width: 280px;
    }

    .dossier-badge {
      background: rgba(212, 175, 55, 0.15);
      color: var(--gold-primary);
      font-weight: 700;
      font-size: 0.78rem;
      padding: 4px 10px;
      border-radius: 4px;
      border: 1px solid rgba(212, 175, 55, 0.3);
      white-space: nowrap;
      margin-top: 2px;
    }

    .dossier-badge.badge-primary {
      background: var(--gold-primary);
      color: #000;
      border-color: var(--gold-bright);
    }

    .dossier-texts h3 {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 4px;
    }

    .dossier-texts p {
      font-size: 0.83rem;
      color: var(--text-muted);
      line-height: 1.45;
    }

    .dossier-actions {
      display: flex;
      gap: 10px;
      flex-wrap: nowrap;
    }

    .btn-pdf {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.84rem;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 6px;
      text-decoration: none;
      transition: all 0.2s;
      white-space: nowrap;
    }

    .btn-preview {
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid var(--gold-primary);
      color: var(--gold-bright);
    }

    .btn-preview:hover {
      background: var(--gold-primary);
      color: #000;
    }

    .btn-download {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
    }

    .btn-download:hover {
      background: rgba(212, 175, 55, 0.2);
      border-color: var(--gold-primary);
      color: var(--gold-primary);
    }

    /* Notice Footer Box */
    .notice-box {
      margin-top: 36px;
      background: rgba(21, 27, 40, 0.5);
      border: 1px dashed var(--gold-dark);
      border-radius: 10px;
      padding: 20px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.6;
    }

    .notice-box strong {
      color: var(--gold-light);
    }

    .back-nav {
      margin-top: 28px;
      text-align: center;
    }

    .back-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: var(--gold-primary);
      text-decoration: none;
      font-size: 0.88rem;
      font-weight: 600;
      transition: color 0.2s;
    }

    .back-link:hover {
      color: var(--gold-bright);
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="glow-top"></div>

  <div class="container">
    <!-- Header -->
    <header>
      <div class="tag-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        《公寓大廈管理條例》第 26 條第 1 項法定程序 ｜ 專案編號：FY-SPLIT-2026-A2
      </div>
      <h1>富宇大境（A2 區・6 戶）<br><span>法定獨立分割卷宗與專案報告下載專區</span></h1>
      <p class="subtitle">台中市沙鹿區龍社路 593～603 號全體住戶專屬 ｜ 迎回 28 萬自有公款 ｜ 管理費自 $1,000 大降至 $400</p>
      <div class="reporter-bar">
        <span>專案受託召集人：<strong>廖倫豪 博士（Howard Liao Ph.D.）</strong></span>
        <span>戶別門牌：<strong>A17 棟（沙鹿區龍社路 595 號）</strong></span>
        <span>法定門檻：<strong>6 戶全數連署即啟動</strong></span>
      </div>
    </header>

    <!-- 4 Bento Stats -->
    <div class="bento-stats">
      <div class="bento-card">
        <div class="bento-label">專案標的建物</div>
        <div class="bento-val">6 戶別墅</div>
        <div class="bento-desc">龍社路 593～603 號全體住戶</div>
      </div>
      <div class="bento-card highlight">
        <div class="bento-label">依法迎回自有公款</div>
        <div class="bento-val">$284,731</div>
        <div class="bento-desc">定存 22 萬 ＋ 交屋基金 6 萬 ＋ 結餘</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">每月管理費負擔</div>
        <div class="bento-val">-60%</div>
        <div class="bento-desc">每戶由 $1,000 降至 $400（年省 $7,200）</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">年度常態滾存結餘</div>
        <div class="bento-val">+$21,600</div>
        <div class="bento-desc">扣除門前路燈公電後，老本越滾越多</div>
      </div>
    </div>

    <!-- Section: Presentation Spotlight -->
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
      高階專案報告簡報
    </div>

    <div class="dossier-list">
      <div class="dossier-row spotlight">
        <div class="dossier-meta">
          <div class="dossier-badge badge-primary">重點簡報</div>
          <div class="dossier-texts">
            <h3>富宇大境 A2 獨立分割專案報告（PDF 簡報）</h3>
            <p>15 頁全彩高解析高管審計簡報 ｜ 完整收錄法理依據、四大痛點、三大王牌、28 萬公款試算表與五大推進階段 SOP。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <a href="富宇大境A2獨立分割專案報告.pdf" class="btn-pdf btn-preview" target="_blank">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </a>
          <a href="富宇大境A2獨立分割專案報告.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>
    </div>

    <!-- Section: 5 Legal Dossiers -->
    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
      法定公文五大卷宗（PDF 印刷檔）
    </div>

    <div class="dossier-list">
      <!-- Item 1: 主件 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">法定主件</div>
          <div class="dossier-texts">
            <h3>富宇大境區分所有權人獨立分割正式提案申請書暨全體連署同意書</h3>
            <p>共 2 頁 ｜ 含主旨說明辦法、管委會提案條款、管理費代收提存共管及第二頁 6 戶親筆連署名冊簽章冊。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <a href="富宇大境區分所有權人獨立分割正式提案申請書暨全體連署同意書.pdf" class="btn-pdf btn-preview" target="_blank">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </a>
          <a href="富宇大境區分所有權人獨立分割正式提案申請書暨全體連署同意書.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 2: 附件一 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">附件一</div>
          <div class="dossier-texts">
            <h3>附件一：法定獨立分割可行性研究報告書</h3>
            <p>共 7 頁 ｜ 援引內政部 86/90 號權威函釋、三大核心王牌、28 萬公款清算試算、五大階段 SOP 及 5% 遲延利息清算協議書範本。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <a href="附件一_法定獨立分割可行性研究報告書.pdf" class="btn-pdf btn-preview" target="_blank">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </a>
          <a href="附件一_法定獨立分割可行性研究報告書.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 3: 附件二 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">附件二</div>
          <div class="dossier-texts">
            <h3>附件二：富宇大地全區地籍圖及出入證明</h3>
            <p>共 1 頁 ｜ 台中市地政事務所官方地籍套繪圖，白紙黑字證明 A2 大境 6 戶臨接龍社路公有計畫道路獨立出入，無袋地爭議。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <a href="附件二_富宇大地全區地籍圖及出入證明.pdf" class="btn-pdf btn-preview" target="_blank">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </a>
          <a href="附件二_富宇大地全區地籍圖及出入證明.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 4: 附件三 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">附件三</div>
          <div class="dossier-texts">
            <h3>附件三：會議記錄及新光銀行 A2 定存財報存根</h3>
            <p>共 1 頁 ｜ 檢附 115 年 5 月與 9 月例會官方財報，佐證新光銀行定存單第 2 筆獨立立卷「A2 大境定存單 $220,231 元」之專款產權憑證。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <a href="附件三_會議記錄及新光銀行A2定存財報存根.pdf" class="btn-pdf btn-preview" target="_blank">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </a>
          <a href="附件三_會議記錄及新光銀行A2定存財報存根.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>

      <!-- Item 5: 附件四 -->
      <div class="dossier-row">
        <div class="dossier-meta">
          <div class="dossier-badge">附件四</div>
          <div class="dossier-texts">
            <h3>附件四：富宇大境共用設施無依賴切結與生活垃圾自行清運承諾書</h3>
            <p>共 1 頁 ｜ 切結水電排污完全物理獨立、自願放棄大社區收費子母車、門前等免費公車型垃圾車，徹底瓦解「公設不可分」之藉口。</p>
          </div>
        </div>
        <div class="dossier-actions">
          <a href="附件四_富宇大境共用設施無依賴切結與生活垃圾自行清運承諾書.pdf" class="btn-pdf btn-preview" target="_blank">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
            在線預覽 PDF
          </a>
          <a href="附件四_富宇大境共用設施無依賴切結與生活垃圾自行清運承諾書.pdf" class="btn-pdf btn-download" download>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
            下載 PDF
          </a>
        </div>
      </div>
    </div>

    <!-- Notice Footer Box -->
    <div class="notice-box">
      <strong>【法定連署簽署說明】</strong><br>
      依據《公寓大廈管理條例》第 26 條第 1 項，本分割案只需我們 <strong>A2 大境 6 戶（龍社路 593～603 號）區權人 100% 簽署</strong> 即可具備完整法定效力。<br>
      紙本提案申請書正本備於受託召集人 廖倫豪 先生（龍社路 595 號 A17）處，隨時歡迎各位鄰居翻閱完整原件並簽章！
    </div>

    <div class="back-nav">
      <a href="index.html" class="back-link">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="15 18 9 12 15 6"/></svg>
        返回富宇大地社區線上戰情室總覽
      </a>
    </div>
  </div>
</body>
</html>
"""

out_path = '/Users/howardliao/Desktop/HermesAgent/PortFilio/fuyu/dajing.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated dajing.html: strictly PDF preview and download only, zero zip, zero docx, zero pptx!")
