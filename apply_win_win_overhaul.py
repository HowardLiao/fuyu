# -*- coding: utf-8 -*-
import re

path = '/Users/howardliao/Desktop/HermesAgent/PortFilio/fuyu/generate_dajing_interactive.py'

with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Title and Header
old_title_snippet = """  <title>富宇大境（A2 區・6 戶）法定獨立分割卷宗與專案報告下載專區</title>"""
new_title_snippet = """  <title>富宇大境（A2 區・6 戶）管理分流與資源重整雙贏方案下載專區</title>"""
code = code.replace(old_title_snippet, new_title_snippet)

old_header_block = """      <div class="tag-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        《公寓大廈管理條例》第 53 條、第 31 條管理分流程序 ｜ 專案編號：FY-SPLIT-2026-A2
      </div>
      <h1>富宇大境（A2 區・6 戶）<br><span>法定獨立分割卷宗與專案報告下載專區</span></h1>
      <p class="subtitle">台中市沙鹿區龍社路 593～603 號全體住戶專屬 ｜ 迎回 28 萬自有公款 ｜ 管理費自 $1,000 大降至 $400</p>
      <div class="reporter-bar">
        <span>專案受託召集人：<strong>廖倫豪</strong></span>
        <span>戶別門牌：<strong>A17 棟（沙鹿區龍社路 595 號）</strong></span>
        <span>推進程序：<strong>6 戶連署提請大會審議</strong></span>
      </div>"""

new_header_block = """      <div class="tag-badge">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        《公寓大廈管理條例》第 53 條、第 31 條合意分流程序 ｜ 專案編號：FY-SPLIT-2026-A2
      </div>
      <h1>富宇大境（A2 區・6 戶）<br><span>管理分流與資源重整雙贏方案下載專區</span></h1>
      <p class="subtitle">權責相符 ｜ 聚焦治理 ｜ 資源減負 ｜ 促進富宇大地全區長治久安與雙贏互惠</p>
      <div class="reporter-bar">
        <span>提案代表人：<strong>廖倫豪</strong></span>
        <span>戶別門牌：<strong>A17 棟（沙鹿區龍社路 595 號）</strong></span>
        <span>推進路徑：<strong>提請區分所有權人會議特別決議</strong></span>
      </div>"""

code = code.replace(old_header_block, new_header_block)

# 2. Update Bento Stats
old_bento_block = """    <!-- 4 Bento Stats -->
    <div class="bento-stats">
      <div class="bento-card">
        <div class="bento-label">專案標的建物</div>
        <div class="bento-val" style="text-align: right;"><span id="cntHouses">6</span> 戶別墅</div>
        <div class="bento-desc">龍社路 593～603 號全體住戶</div>
      </div>
      <div class="bento-card highlight">
        <div class="bento-label">依法迎回自有公款</div>
        <div class="bento-val" style="text-align: right;">$<span id="cntFunds">284,731</span></div>
        <div class="bento-desc">定存 22 萬 ＋ 交屋基金 6 萬 ＋ 結餘</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">每月管理費負擔</div>
        <div class="bento-val" style="text-align: right;">-<span id="cntDiscount">60</span>%</div>
        <div class="bento-desc">每戶由 $1,000 降至 $400（年省 $7,200）</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">年度常態滾存結餘</div>
        <div class="bento-val" style="text-align: right;">+$<span id="cntSurplus">21,600</span></div>
        <div class="bento-desc">扣除門前路燈公電後，老本越滾越多</div>
      </div>
    </div>"""

new_bento_block = """    <!-- 4 Bento Stats (Framed from Win-Win Perspective) -->
    <div class="bento-stats">
      <div class="bento-card">
        <div class="bento-label">全社區雙贏格局</div>
        <div class="bento-val" style="text-align: right;"><span id="cntHouses">235 + 6</span> 戶</div>
        <div class="bento-desc">內部 235 戶聚焦治理，外側 6 戶自理維護</div>
      </div>
      <div class="bento-card highlight">
        <div class="bento-label">大社區營運零衝擊</div>
        <div class="bento-val" style="text-align: right;">$<span id="cntFunds">0</span> 元</div>
        <div class="bento-desc">A2 專款專單立卷移交，不影響大社區營運老本</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">大社區物業管理減負</div>
        <div class="bento-val" style="text-align: right;"><span id="cntDiscount">100</span>% 責任聚焦</div>
        <div class="bento-desc">免除跨越龍社路外側巡查，管理範圍單純化</div>
      </div>
      <div class="bento-card">
        <div class="bento-label">內部公設資源釋放</div>
        <div class="bento-val" style="text-align: right;">+<span id="cntSurplus">100</span>% 空間</div>
        <div class="bento-desc">A2 垃圾門前自理，內部子母車全數留給 235 戶</div>
      </div>
    </div>"""

code = code.replace(old_bento_block, new_bento_block)

# 3. Update Simulator
old_sim_block = """    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><line x1="12" y1="6" x2="12" y2="18"/></svg>
      大境住戶專屬・自主財務效益試算模擬器
    </div>

    <div class="simulator-card">
      <div class="sim-header">
        <div>
          <h3>💡 點選您的門牌，即刻試算分家後的家庭與聚落實質利益</h3>
          <p>每戶每月自 $1,000 調降為 $400，一年實質省下 $7,200 元；且依法享有專屬定存老本儲備！</p>
        </div>
      </div>"""

new_sim_block = """    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"/><line x1="12" y1="6" x2="12" y2="18"/></svg>
      權責相符與管理效益試算模型
    </div>

    <div class="simulator-card">
      <div class="sim-header">
        <div>
          <h3>💡 權責相符與收支平衡模型：分流管理如何達成雙方財務最適化</h3>
          <p>A2 透天自理外側維護與水電排污，落實收支平衡；大社區管委會亦免除外側管理成本，實現財務權責對等！</p>
        </div>
      </div>"""

code = code.replace(old_sim_block, new_sim_block)

old_sim_res = """      <div class="sim-results">
        <div class="sim-res-box">
          <div class="sim-res-lbl">貴戶累計實質省下管理費</div>
          <div class="sim-res-val" id="resFamilySavings">$36,000</div>
          <div class="sim-res-sub">每戶每年實質節省 $7,200 元管理費負擔</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">貴戶享有之自有定存儲備份額</div>
          <div class="sim-res-val" id="resHouseholdReserve">$47,455</div>
          <div class="sim-res-sub">迎回 28 萬公款均分份額，生息有據</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">大境 6 戶全區累計安全老本</div>
          <div class="sim-res-val" id="resCommunityTotal">$392,731</div>
          <div class="sim-res-sub">迎回 28 萬 ＋ 每年淨結餘 $21,600</div>
        </div>
      </div>"""

new_sim_res = """      <div class="sim-results">
        <div class="sim-res-box">
          <div class="sim-res-lbl">A2 戶均收支平衡調整</div>
          <div class="sim-res-val" id="resFamilySavings">$36,000</div>
          <div class="sim-res-sub">按實際使用服務計費，免除未享用項目之超額分攤</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">A2 專款專戶專管儲備金</div>
          <div class="sim-res-val" id="resHouseholdReserve">$47,455</div>
          <div class="sim-res-sub">大境管委會專戶專款專管，自負門前維護盈虧</div>
        </div>
        <div class="sim-res-box">
          <div class="sim-res-lbl">A2 獨立運作儲備規模</div>
          <div class="sim-res-val" id="resCommunityTotal">$392,731</div>
          <div class="sim-res-sub">專案移交原款與自律結餘，完全獨立自籌</div>
        </div>
      </div>"""

code = code.replace(old_sim_res, new_sim_res)

# 4. Update Comparison Switcher Title & Tabs
old_cmp_nav = """    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10"/><path d="M12 20V4"/><path d="M6 20v-6"/></svg>
      現況「逆向補貼」困境 vs 獨立「自主掌權」對比矩陣
    </div>

    <div class="compare-nav">
      <div id="tabBefore" class="btn-tab active-tab-before" onclick="switchCompare('before')">
        ⚠️ 現況困境：被動合併大社區（241 戶體系）
      </div>
      <div id="tabAfter" class="btn-tab" onclick="switchCompare('after')">
        ✨ 破局方案：依法獨立分割（大境 6 戶自治）
      </div>
    </div>"""

new_cmp_nav = """    <div class="section-title">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 20V10"/><path d="M12 20V4"/><path d="M6 20v-6"/></svg>
      全區「強行綑綁」管理瓶頸 vs「合意分流」雙贏互惠對比矩陣
    </div>

    <div class="compare-nav">
      <div id="tabBefore" class="btn-tab active-tab-before" onclick="switchCompare('before')">
        ⚠️ 強行綑綁現況：管理跨區分散・權責不符
      </div>
      <div id="tabAfter" class="btn-tab" onclick="switchCompare('after')">
        ✨ 合意分流雙贏：聚焦內部治理・公設資源回饋
      </div>
    </div>"""

code = code.replace(old_cmp_nav, new_cmp_nav)

# 5. Update Dossier Descriptions
old_dossier_poa = """            <h3>富宇大境（A2 區）全體區分所有權人獨立分割全權委任授權書</h3>
            <p>共 1 頁 ｜ 依據《民法》第 528 條委任契約，全體 6 戶專案全權委任 廖倫豪 辦理提案、交涉、迎回 28 萬公款與公所報備；載明排除任何不動產私權處分，保障全體委任人權益。</p>"""

new_dossier_poa = """            <h3>富宇大境（A2 區）全體區分所有權人管理分流全權委任授權書</h3>
            <p>共 1 頁 ｜ 依據《民法》第 528 條委任契約，全體 6 戶專案委任 廖倫豪 辦理雙贏提案、大會協商、專案公款移交與主管機關報備；載明排除任何不動產私權處分，保障全體委任人權益。</p>"""

code = code.replace(old_dossier_poa, new_dossier_poa)

old_dossier_pet = """            <h3>富宇大境區分所有權人獨立分割正式提案申請書暨全體連署同意書</h3>
            <p>共 2 頁 ｜ 含主旨說明辦法、管委會提案條款、管理費代收提存共管及第二頁 6 戶親筆連署名冊簽章冊。</p>"""

new_dossier_pet = """            <h3>富宇大境區分所有權人獨立分割正式提案申請書暨全體連署同意書</h3>
            <p>共 2 頁 ｜ 含主旨說明辦法、雙贏分流提案條款、合意移交方案及第二頁 6 戶親筆連署立案簽章冊。</p>"""

code = code.replace(old_dossier_pet, new_dossier_pet)

old_dossier_att1 = """            <h3>附件一：法定獨立分割可行性研究報告書</h3>
            <p>共 7 頁 ｜ 援引內政部 86/90 號權威函釋、三大核心王牌、28 萬公款清算試算、五大階段 SOP 及 5% 遲延利息清算協議書範本。</p>"""

new_dossier_att1 = """            <h3>附件一：法定獨立分割可行性研究報告書</h3>
            <p>共 7 頁 ｜ 依法論證《條例》第 53 條集居分流準用與第 31 條大會議決路徑、全區雙贏效益分析、專案資產移交試算與合意分流協議書草案。</p>"""

code = code.replace(old_dossier_att1, new_dossier_att1)

old_dossier_att2 = """            <h3>附件二：富宇大地全區地籍圖及出入證明</h3>
            <p>共 1 頁 ｜ 台中市地政事務所官方地籍套繪圖，白紙黑字證明 A2 大境 6 戶臨接龍社路公有計畫道路獨立出入，無袋地爭議。</p>"""

new_dossier_att2 = """            <h3>附件二：富宇大地全區地籍圖及出入證明</h3>
            <p>共 1 頁 ｜ 檢附全區地籍與建築配置示意圖，客觀佐證 A2 臨接公有計畫道路龍社路獨立出入，具備獨立管理之物理要件。</p>"""

code = code.replace(old_dossier_att2, new_dossier_att2)

old_dossier_att3 = """            <h3>附件三：會議記錄及新光銀行 A2 定存財報存根</h3>
            <p>共 1 頁 ｜ 檢附 115 年 5 月與 9 月例會官方財報，佐證新光銀行定存單第 2 筆獨立立卷「A2 大境定存單 $220,231 元」之專款產權憑證。</p>"""

new_dossier_att3 = """            <h3>附件三：會議記錄及新光銀行 A2 定存財報存根</h3>
            <p>共 1 頁 ｜ 檢附 115 年 5 月與 9 月例會官方財報，佐證 A2 大境定存單 NT$ 220,231 元自始即獨立立卷專單保管之財務客觀事實。</p>"""

code = code.replace(old_dossier_att3, new_dossier_att3)

old_dossier_att4 = """            <h3>附件四：富宇大境共用設施無依賴切結與生活垃圾自行清運承諾書</h3>
            <p>共 1 頁 ｜ 切結水電排污完全物理獨立、自願放棄大社區收費子母車、門前等免費公車型垃圾車，徹底瓦解「公設不可分」之藉口。</p>"""

new_dossier_att4 = """            <h3>附件四：富宇大境共用設施無依賴切結與生活垃圾自行清運承諾書</h3>
            <p>共 1 頁 ｜ 切結水電排污完全物理獨立自理、自願放棄大社區收費子母車，生活垃圾門前等候市府免費清潔隊，徹底為大社區公設減負。</p>"""

code = code.replace(old_dossier_att4, new_dossier_att4)

# 6. Update FAQ Section
old_faqs = """    <div class="faq-list">
      <div class="faq-item open">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q1：我們大境才 6 戶透天，在法律程序上如何合法獨立成立管委會？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全合於法定程序！</strong>依據《公寓大廈管理條例》第 53 條規定，多數各自獨立使用之建築物，如設施使用無整體不可分性，準用本條例管理。<br>
          大境 6 戶出入臨公有計畫道路龍社路、水電排污自理、生活廢棄物自行等免費清潔隊，客觀上具備完整獨立性。實務上將依《條例》第 31 條特別決議程序，提請富宇大地全體區分所有權人會議審議變更規約第二條管理範圍（排除 A2），大會通過後即可向主管機關區公所申辦變更報備與大境獨立報備！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q2：這筆 NT$ 284,731 元的公款，如何向大社區辦理移交撥還？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>款項來源清楚，依審計公平原則專案協商撥還！</strong>管委會 5 月與 9 月例會官方財報已明確將台中市政府核退之公款獨立開立「A2 大境定存單 NT$ 220,231 元」專單保管；加上起造人富宇建設交屋管理基金（每戶 1 萬，大境 6 戶共 60,000 元）。本區建請大會同意於合意分割後專案撥還移交至大境公庫專戶專管專用。
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q3：獨立之後管理費降到 $400，真的夠用嗎？路燈電費會不會付不出來？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>綽綽有餘，甚至年年倒存老本！</strong>大境 6 戶是透天別墅，出門直接是龍社路，我們既沒有電梯維護費、也沒有內部巷道保全，更不用負擔每個月 4.8 萬元的垃圾子母車費用。6 戶月收 $2,400，扣除門前路燈與公電約 $400、行政雜支 $200，<strong>每月常態結餘高達 $1,800，一年還能穩定存下 $21,600 元儲備金</strong>！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q4：我們不使用大社區內部子母車，平日倒垃圾會不會變得很麻煩？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全不會，現況大家本來就是等門前垃圾車！</strong>龍社路本就是台中市環保局定時定點免費清運路線。大境 6 戶出門即投遞，簽訂《切結書》放棄內部子母車，不僅不影響生活，反而替每戶每年省下分攤內部垃圾清運費的冤枉錢！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q5：我們住戶簽了連署書之後，需要自己去跟管委會或公所交涉跑流程嗎？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全不需要！大家只需安心簽名，全權由召集人代辦。</strong>受託召集人 廖倫豪（A17 龍社路 595 號）承諾代表全體 6 戶出席管委會例會提案、與主委簽署分割協議書，並親赴台中市龍井區公所辦理變更備查與新光銀行開戶接收，大家免除一切繁瑣公務負擔！
        </div>
      </div>
    </div>"""

new_faqs = """    <div class="faq-list">
      <div class="faq-item open">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q1：大境 6 戶透天在法律程序上如何合法推動管理分流？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全依循法定程序，保障全體住戶權益！</strong>依據《公寓大廈管理條例》第 53 條規定，各自獨立使用且共用設施無整體不可分性之集居地區，準用本條例管理。<br>
          A2 大境 6 戶出入直臨公有計畫道路龍社路、水電排污自理、生活垃圾門前等候免費公有清潔隊，具備完整獨立性。實務上將依《條例》第 31 條特別決議程序，正式提案請富宇大地全體區分所有權人會議審議變更規約管理範圍（排除 A2），大會審議通過後依法向主管機關區公所申辦變更報備與大境獨立報備，程序合法、公開透明！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q2：這項分流管理提案，對富宇大地其餘 235 戶住戶有哪些實質雙贏好處？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>全區資源減負、管理更聚焦！</strong><br>
          1. <strong>物業管理聚焦</strong>：解除物業與保全人員跨越公有道路龍社路照應外側住戶之奔波，管理責任單純化，專注封閉式社區 235 戶核心治理。<br>
          2. <strong>公設容量減負</strong>：A2 承諾門前等候市府垃圾車並簽署放棄子母車切結，內部環保室與收費子母車容量 100% 留給 235 戶使用，解決垃圾滿溢壓力。<br>
          3. <strong>消除長期制度隱患</strong>：消弭外側透天未享用內部公設卻需分攤維護費的矛盾，避免未來無休止之行政陳情與爭議，促進全區長治久安。<br>
          4. <strong>財務零衝擊</strong>：A2 定存原即獨立立卷保管，專案移交不侵蝕大社區任何營運公款與既有基金！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q3：A2 分流後，會不會造成大社區管委會財務短缺或需要向住戶調漲管理費？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>完全不會！大社區財務收支結構不受負面影響。</strong><br>
          A2 6 戶每月繳納之 $6,000 元，經審計按戶數分攤內部垃圾清運費（約 $1,195）與物業經理人事支出（約 $1,751）後，大社區管委會原本投入外側管理所剩無幾；分流後管委會免除了對外側路段的巡檢維護與公電支出，且 A2 原本就未使用內部任何休閒公設，大社區 235 戶之日常營運預算完全穩健自給，絕不需要因而調漲管理費！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q4：關於專案移交之 NT$ 284,731 元款項，如何確保大社區的資產權益不受損？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>帳目獨立清晰，純屬專款原單專案歸位！</strong><br>
          富宇大地管委會於 115 年 5 月與 9 月例會官方財報已明確載明：台中市政府核退之公款分別定存，其中第 2 筆即獨立立卷為「A2 大境定存單 NT$ 220,231 元」專單保管；加上起造人富宇建設交屋管理基金（每戶 1 萬，大境 6 戶共 60,000 元）。該專案款項自始即與大社區其他各區定存單分開保管，移交純屬原款專案歸位，富宇大地 235 戶所屬之悠境、澄境定存、起造人提撥款及日常營運帳戶分毫不受影響！
        </div>
      </div>

      <div class="faq-item">
        <div class="faq-question" onclick="toggleFaq(this)">
          <span>Q5：雙方在程序推動與大會決議期間，管理費與公共事務如何維持平穩運作？</span>
          <span class="faq-icon">+</span>
        </div>
        <div class="faq-answer">
          <strong>全程恪遵法規，平穩過渡零衝突！</strong><br>
          在大會特別決議生效前，A2 6 戶住戶全體照常依現制履行管理費繳納義務，絕不採取停繳或對抗手段；A2 住戶門前廢棄物亦維持自行等候市府垃圾車清運，絕不影響大社區內部日常安寧。本案以「協商與雙贏」為唯一準則，共同攜手完成合法合規的分流程序。
        </div>
      </div>
    </div>"""

code = code.replace(old_faqs, new_faqs)

# 7. Update Notice Footer Box
old_notice = """    <div class="notice-box">
      <strong>【法定連署與大會提案說明】</strong><br>
      依據《公寓大廈管理條例》第 53 條與第 31 條，本案由 <strong>A2 大境 6 戶（沙鹿區龍社路 593～603 號）全體區權人 100% 簽署連署書與授權書</strong>，正式向管委會提案並協助排入區分所有權人會議審議。<br>
      紙本提案申請書與全權委任授權書正本備於受託召集人 廖倫豪（龍社路 595 號 A17）處，隨時歡迎各位鄰居翻閱完整原件並簽章！
    </div>"""

new_notice = """    <div class="notice-box">
      <strong>【法定連署與大會提案說明】</strong><br>
      依據《公寓大廈管理條例》第 53 條與第 31 條，本案由 <strong>A2 大境 6 戶（沙鹿區龍社路 593～603 號）全體區權人 100% 簽署連署書與授權書</strong>，正式向管委會提案並協助排入區分所有權人會議審議，共創全社區權責相符之雙贏治理。<br>
      紙本提案申請書與全權委任授權書正本備於提案代表人 廖倫豪（龍社路 595 號 A17）處，隨時歡迎各位鄰居翻閱完整原件並簽章！
    </div>"""

code = code.replace(old_notice, new_notice)

# 8. Update compareData & stepsData in JavaScript
old_js_compare = """    const compareData = {
      before: [
        { topic: '話語權地位', title: '邊緣化 2.49% 弱勢', desc: '全社區 241 戶，大境僅 6 戶，在 12~18 席管委會中無實質席次，預算動支完全被內部大聚落主導。' },
        { topic: '管理費負擔', title: '每戶每年繳 12,000 元', desc: '6 戶每年繳交 7.2 萬元管理費，全數流入大水庫補貼內部深處巷道與管制作業，門前幾無回饋。' },
        { topic: '垃圾清運費', title: '替他人分攤 4.8 萬/月', desc: '大境位在龍社路自行等公車型垃圾車，卻月月幫內部 235 戶分攤每週兩次 6 桶之收費子母車清運費。' },
        { topic: '物業經理配置', title: '深居貨櫃屋服務歸零', desc: '物業經理（$70,350/月）常駐於內部貨櫃屋，大境郵件信件郵差直送門前，實質服務趨近於零。' }
      ],
      after: [
        { topic: '話語權地位', title: '100% 獨立自主掌權', desc: '成立專管委員會，6 戶全體均為主事核心，每筆預算動支 100% 自主決策，無需看他人臉色。' },
        { topic: '管理費負擔', title: '大幅減輕 60% 至 $400/月', desc: '每戶每年現省 7,200 元；6 戶年收 $28,800 扣除路燈公電後，每年還能穩健存入 $21,600 儲備金！' },
        { topic: '垃圾清運費', title: '費用 NT$ 0 元完全免花費', desc: '出門直接等候台中市環保局免費公有垃圾車，簽署放棄使用切結書，不再幫大社區付一毛清運費！' },
        { topic: '公款儲備掌控', title: '一次迎回 NT$ 284,731 元', desc: '新光銀行 A2 定存單 22 萬與富宇交屋基金 6 萬全額移交大境公庫，平均每戶享有約 4.75 萬老本儲備。' }
      ]
    };"""

new_js_compare = """    const compareData = {
      before: [
        { topic: '大社區管理負荷', title: '管轄跨區分散・行政負擔重', desc: '大境 6 戶位於龍社路外側，物業經理需跨越公有道路照應，巡查範圍分散且徒增管委會外側民事與安全責任。' },
        { topic: '公設與環保室負載', title: '垃圾容量受限・使用動線重疊', desc: '內部收費子母車每週清運 6 桶，若計入外側戶別容量更加緊繃，且衍生出入刷卡與動線維護成本。' },
        { topic: '財務分攤爭議風險', title: '費用與服務不對稱・潛在糾紛', desc: 'A2 為臨路透天，自理水電排污且未享有封閉社區公設，長期綑綁易滋生收費與服務對價不對等之管理陳情。' },
        { topic: '大會決策協調成本', title: '議題性質迥異・拖慢大會議程', desc: '內部封閉聚落與外側臨路透天需求完全不同，共同列入區權大會討論容易模糊焦點，增加溝通協調成本。' }
      ],
      after: [
        { topic: '大社區管理聚焦', title: '責任單純化・專注內部 235 戶', desc: '解除外側 6 戶跨路巡查責任，物業管理集中於封閉式社區核心，管委會治理動線更聚焦、行政效能顯著提升！' },
        { topic: '公設資源全數回饋', title: '子母車容量 100% 留給內部', desc: 'A2 承諾門前等市府免費垃圾車並立切結退出，內部子母車空間與清潔資源全額保留供 235 戶使用，免除超載壓力！' },
        { topic: '財務帳務獨立清楚', title: '大社區營運老本 0 衝擊', desc: 'A2 新光定存單本即專單獨立保管，移交原款純屬專戶歸位，大社區各區基金與日常營運公款分毫未損、完全不受影響！' },
        { topic: '促進鄰里長治久安', title: '各得其所・建立和諧友好共融', desc: '依《條例》第 53/31 條合意分流，消除權責不對等之制度隱患，富宇大地全區樹立理性自治與和睦治理之典範！' }
      ]
    };"""

code = code.replace(old_js_compare, new_js_compare)

old_js_steps = """    const stepsData = {
      1: {
        title: '階段一：A2 大境內部 100% 連署凝聚（共識準備）',
        badge: '進行中・現正發動',
        desc: '• 召開大境 6 戶客廳會，確認共同推選 廖倫豪 為受託召集人兼法定代理人。<br>• 簽署《正式提案申請書》與《專案全權委任授權書》，取得 6 戶區權人 100% 親筆簽章。<br>• 備齊地籍圖、會議記錄與切結書，完成全套法定卷宗立案。'
      },
      2: {
        title: '階段二：向富宇大地管委會正式提案（溝通與審議）',
        badge: '法定公文正式呈送',
        desc: '• 召集人以正式公文向富宇大地第二屆管委會例會提案。<br>• 採取雙贏溝通策略：證明大境定存 22 萬原本就是獨立存單，分割不會影響大社區 760 萬老本；大境退出子母車使用，大社區垃圾容量更充裕；物業經理減少巡護負擔。'
      },
      3: {
        title: '階段三：移交協議簽署與大境管委會成立（法律生效）',
        badge: '法律契約確立',
        desc: '• 管委會例會確認獨立分割，雙方簽署《資產分割清算協議書》，約定新光銀行定存與交屋基金移交條款與 5% 遲延利息保證。<br>• 大境 6 戶依法成立「富宇大境管理委員會」，訂立住戶自治規約，推選幹部。'
      },
      4: {
        title: '階段四：主管機關（台中市龍井區公所）行政報備（法人地位）',
        badge: '官方核發統編',
        desc: '• 檢具全體區權人簽章公文、修正規約、分割協議書、地籍圖向龍井區公所申辦變更備查。<br>• 同步申辦富宇大地變更為 235 戶，大境核發獨立 6 戶報備證明並取得新統一編號。'
      },
      5: {
        title: '階段五：新光銀行開戶接收、資產撥付與外包切割（獨立啟航）',
        badge: '公款撥付・自主營運',
        desc: '• 持公所公文與印鑑至新光銀行沙鹿分行開立「富宇大境管理委員會」專戶。<br>• 28 萬餘元公款一次性匯撥入專戶，終止大社區外包合約連帶責任，正式啟動每月 $400 自主治理！'
      }
    };"""

new_js_steps = """    const stepsData = {
      1: {
        title: '階段一：A2 大境內部連署凝聚（共識準備）',
        badge: '進行中・現正發動',
        desc: '• 召開大境 6 戶住戶交流會，推選 廖倫豪 為專案提案代表人。<br>• 簽署《正式提案申請書》與《全權委任授權書》，取得 6 戶區權人全體簽章立案。<br>• 備齊地籍圖、會議紀錄與公設自理切結書，完成全套法定合規卷宗。'
      },
      2: {
        title: '階段二：向富宇大地管委會正式提案（溝通與列入議程）',
        badge: '法定公文正式呈送',
        desc: '• 提案代表人以正式公文書向富宇大地管委會提案，建請列入例會議程審議。<br>• 闡明雙贏方案：A2 專款專單立卷移交零衝擊大社區營運；A2 切結退出內部子母車釋放環保空間；管委會免除跨路巡檢維護責任。'
      },
      3: {
        title: '階段三：區分所有權人會議特別決議（大會審議通過）',
        badge: '大會法定決議',
        desc: '• 富宇大地全體區分所有權人會議依法審議通過變更規約管理範圍（第 31 條特別決議）。<br>• 雙方簽署《管理分流與資產移交協議書》，約定新光銀行定存與交屋基金專案撥還。<br>• 大境 6 戶依法成立「富宇大境管理委員會」，訂立住戶自治規約，推選幹部。'
      },
      4: {
        title: '階段四：建物管轄區公所行政報備（組織立案備查）',
        badge: '官方核發統編',
        desc: '• 檢具全體區權大會決議公文、修正規約、分流協議書、地籍圖向管轄區公所申辦變更備查。<br>• 同步申辦富宇大地變更為 235 戶，大境核發獨立 6 戶報備證明並取得新統一編號。'
      },
      5: {
        title: '階段五：新光銀行專戶開立、資產移交與獨立營運（雙贏啟航）',
        badge: '專戶專款專用',
        desc: '• 持主管機關公文與印鑑至新光銀行沙鹿分行開立「富宇大境管理委員會」專戶。<br>• 專案款項匯撥入大境專戶專管專用，雙方正式啟動雙贏自治營運！'
      }
    };"""

code = code.replace(old_js_steps, new_js_steps)

with open(path, 'w', encoding='utf-8') as f:
    f.write(code)

print("generate_dajing_interactive.py successfully updated with Win-Win Overhaul!")
