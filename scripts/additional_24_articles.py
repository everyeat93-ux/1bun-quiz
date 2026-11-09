# -*- coding: utf-8 -*-
"""
24 New Comprehensive Knowledge Articles for 1bun-quiz.kr
Expands the encyclopedia from 26 to 50 in-depth articles (10 per category).
"""

NEW_ARTICLES = [
    # ==================== 1. 맞춤법 (Spelling & Grammar) - 4 New (Total 10) ====================
    {
        "slug": "spelling-bareum-vs-baram",
        "category": "맞춤법",
        "category_slug": "category-spelling.html",
        "category_icon": "📝",
        "title": "'바람'과 '바램' 올바른 맞춤법 - '네가 행복하길 바라' 종결형 공식",
        "description": "'바라다'와 '바래다'의 문법적 차이와 표준어 규정! '행복하길 바라'가 맞고 '바래'가 틀린 이유와 3초 판별법을 정리합니다.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 한국어 어문연구팀",
        "summary": [
            "생각이나 소원이 이루어지기를 원하는 기본 동사는 '바라다'입니다.",
            "'바라다'에 어미 '-아'가 결합하면 '바라'가 되며, '바래'는 표준어가 아닙니다.",
            "명사형 역시 '바람'이 표준어이며, '바램'은 색이 변질된다는 뜻의 '바래다'에서 온 말입니다."
        ],
        "content_html": """
        <p class="lead-text">
          가요 가사나 일상 대화, 연하장에서 가장 흔히 틀리는 표현 중 하나가 바로 <strong>"네가 행복하길 바래"</strong>입니다. 발음상 '바래'가 더 부드럽고 자연스럽게 느껴지지만, 한글 맞춤법 규정상 '바래'는 틀린 표기이며 <strong>'바라'</strong>가 표준어입니다.
        </p>

        <h2 class="article-h2">1. '바라다'와 '바래다'의 결정적 어간 차이</h2>
        <p>
          우리말에서 어떤 일이 이루어지기를 기대하고 소원하는 동사의 기본형은 <strong>'바라다'</strong>입니다. 반면, <strong>'바래다'</strong>는 "볕에 바래어 색이 하얗게 변하다"나 "배웅하여 보내다"라는 전혀 다른 의미를 지닙니다.
        </p>
        <p>
          '바라다'의 어간은 <strong>'바라-'</strong>이므로, 뒤에 어말 어미 <em>'-아'</em>가 결합하면 <strong>[바라- + -아 = 바라]</strong>로 활용됩니다. (예: 가다 → 가, 자다 → 자). 여기에 '바래'가 되려면 기본형이 '바래다'여야 하는데, 소망을 뜻하는 기본형은 '바래다'가 아니므로 '바래'는 문법적으로 성립할 수 없습니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>올바른 표준어</th>
                <th>비표준어 (오기)</th>
                <th>문법 근거</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>종결형 (구어)</strong></td>
                <td><span class="correct-text">합격하길 바라</span></td>
                <td><span class="wrong-text">합격하길 바래</span></td>
                <td>'바라-' + '-아' = '바라'</td>
              </tr>
              <tr>
                <td><strong>존칭 종결형</strong></td>
                <td><span class="correct-text">건강하시길 바라요</span></td>
                <td><span class="wrong-text">건강하시길 바래요</span></td>
                <td>'바라' 뒤에 보조사 '요' 결합</td>
              </tr>
              <tr>
                <td><strong>명사형 (소망)</strong></td>
                <td><span class="correct-text">나의 간절한 바람</span></td>
                <td><span class="wrong-text">나의 간절한 바램</span></td>
                <td>어간 '바라-'에 명사형 전미사 '-ㅁ' 결합</td>
              </tr>
              <tr>
                <td><strong>색상의 탈색</strong></td>
                <td><span class="correct-text">빛이 바래다</span></td>
                <td><span class="wrong-text">빛이 바라다</span></td>
                <td>변색/퇴색을 뜻하는 동사는 '바래다'</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 3초 직관 암기 공식: "자다→자! 가다→가! 바라다→바라!"</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 끝내는 판별법:</strong><br>
          '자다'가 '자'가 되고, '가다'가 '가'가 되듯이, <strong>'바라다'는 무조건 '바라'</strong>가 됩니다!<br>
          <em>(공식: 자다→자, 가다→가, 그러므로 바라다→바라!)</em>
        </div>

        <h2 class="article-h2">3. 실생활 올바른 문장 예시</h2>
        <ul class="example-list">
          <li>"새해에는 원하시는 모든 일이 술술 풀리길 <strong>바랍니다</strong>." (O)</li>
          <li>"이번 시험에서 부디 좋은 결과를 얻기를 <strong>바라</strong>." (O)</li>
          <li>"오랫동안 햇볕에 방치된 현수막이 붉은빛으로 <strong>바랬다</strong>." (O - 탈색)</li>
          <li>"모두가 평화롭게 공존하는 사회가 되기를 바라는 <strong>바람</strong>이 있다." (O)</li>
        </ul>
        """,
        "quiz": {
            "q": "친구에게 생일 축하 메시지를 보낼 때 '올 한 해도 건강하고 행복하길 [{A} / {B}]'라고 쓰는 것이 바른 표기이다.",
            "a": "바라",
            "b": "바래",
            "correct": "A",
            "exp": "소망을 나타내는 동사 기본형은 '바라다'이므로 어간 '바라-'에 어미 '-아'가 붙은 '바라'가 표준어입니다."
        },
        "faq": [
            {"q": "'바라요'가 어색한데 '바래요'를 쓰면 절대 안 되나요?", "a": "일상 구어체나 대중가요에서 '바래요'가 널리 쓰이지만, 국립국어원 표준 규범상 명백한 비표준어입니다. 격식 있는 작문이나 시험에서는 반드시 '바라요' 또는 '바랍니다'로 써야 합니다."},
            {"q": "'바람'과 공기의 흐름인 '바람(Wind)'은 동음이의어인가요?", "a": "네, 맞습니다. 소망을 뜻하는 명사 '바람'과 대기의 흐름을 뜻하는 '바람'은 형태만 같은 동음이의어입니다."}
        ]
    },
    {
        "slug": "spelling-yet-vs-yeot",
        "category": "맞춤법",
        "category_slug": "category-spelling.html",
        "category_icon": "📝",
        "title": "'예스럽다' vs '옛스럽다' - '옛'과 '예'의 구분 기준과 어원",
        "description": "'옛날', '옛 추억'은 '옛'인데 왜 '예스럽다', '예부터'는 '예'일까? 한글 맞춤법 제27항에 숨은 사이시옷과 파생어 법칙.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 한국어 어문연구팀",
        "summary": [
            "뒤에 명사가 오는 관형사는 시옷 받침이 있는 '옛'을 씁니다. (옛날, 옛 추억)",
            "접사 '-스럽다'나 조사 '부터'가 결합할 때는 명사 '예'를 씁니다. (예스럽다, 예부터)",
            "'옛스럽다'는 잘못된 조어로 국어사전에 등재되어 있지 않습니다."
        ],
        "content_html": """
        <p class="lead-text">
          전통 한옥이나 고즈넉한 사찰을 볼 때 <em>"분위기가 참 옛스럽다"</em>라고 표현하는 분들이 많습니다. '옛날', '옛사랑'처럼 '옛'이 익숙하다 보니 자연스레 '옛스럽다'로 쓰기 쉽지만, 표준 국어대사전에 따른 바른 표기는 <strong>'예스럽다'</strong>입니다.
        </p>

        <h2 class="article-h2">1. 관형사 '옛' vs 명사 '예'의 차이</h2>
        <p>
          우리말에서 <strong>'옛'</strong>은 뒤따르는 명사를 직접 꾸며주는 <strong>관형사</strong>입니다. 관형사는 뒤에 다른 단어가 올 때 띄어쓰거나 합성어를 만듭니다. (예: 옛 친구, 옛 건물, 옛날).
        </p>
        <p>
          반면 <strong>'예'</strong>는 "지나간 아득한 때"를 의미하는 독립된 <strong>명사</strong>입니다. 접미사 <em>'-스럽다'</em>는 명사 뒤에 붙어 형용사를 만드는 접사(예: 사랑스럽다, 어른스럽다)이므로, 관형사 '옛'이 아닌 명사 '예' 뒤에 붙어 <strong>'예스럽다'</strong>가 완성됩니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>품사 및 결합</th>
                <th>올바른 표준어</th>
                <th>틀린 표현</th>
                <th>판별 비결</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>접미사 '-스럽다' 결합</strong></td>
                <td><span class="correct-text">예스럽다</span></td>
                <td><span class="wrong-text">옛스럽다</span></td>
                <td>명사 '예' + '-스럽다'</td>
              </tr>
              <tr>
                <td><strong>조사 '부터/대로' 결합</strong></td>
                <td><span class="correct-text">예부터 전해 내려오다</span></td>
                <td><span class="wrong-text">옛부터 전해 내려오다</span></td>
                <td>조사는 명사 '예' 뒤에 결합</td>
              </tr>
              <tr>
                <td><strong>명사를 꾸미는 관형사</strong></td>
                <td><span class="correct-text">옛 친구 / 옛 추억</span></td>
                <td><span class="wrong-text">예 친구 / 예 추억</span></td>
                <td>뒤에 명사가 올 땐 '옛'</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 3초 암기 공식: "뒤에 명사 오면 '옛', 조사·접사 오면 '예'!"</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 외우는 공식:</strong><br>
          뒤에 <strong>명사(친구, 길, 날)</strong>가 오면 시옷 받침 <strong>'옛'</strong>!<br>
          뒤에 <strong>'~스럽다', '~부터'</strong>가 오면 받침 없는 <strong>'예'</strong>!
        </div>

        <h2 class="article-h2">3. 실생활 올바른 문장 예시</h2>
        <ul class="example-list">
          <li>"인사동 골목길에는 <strong>예스러운</strong> 멋을 간직한 전통 찻집이 많다." (O)</li>
          <li>"이 풍습은 <strong>예부터</strong> 조상들이 지켜온 미풍양속이다." (O)</li>
          <li>"오랜만에 만난 <strong>옛 동창</strong>들과 밤새 이야기꽃을 피웠다." (O)</li>
        </ul>
        """,
        "quiz": {
            "q": "골동품 가게에서 발견한 조선 시대 도자기는 은은하고 [{A} / {B}] 멋이 깃들어 있었다.",
            "a": "예스러운",
            "b": "옛스러운",
            "correct": "A",
            "exp": "접미사 '-스럽다'는 명사 '예' 뒤에 결합하므로 '예스럽다/예스러운'이 올바른 표준어입니다."
        },
        "faq": [
            {"q": "'옛부터'라는 말은 왜 문법적으로 틀린가요?", "a": "'부터'는 체언(명사) 뒤에 붙는 격조사입니다. 관형사인 '옛' 뒤에는 조사가 직접 결합할 수 없으므로 명사 '예'를 써서 '예부터'로 적어야 바릅니다."},
            {"q": "'예적'과 '옛적' 중에는 무엇이 맞나요?", "a": "'옛적'이 맞습니다. '적(때)'은 의존 명사이므로 관형사 '옛'이 수식하여 합성 명사 '옛적'이 됩니다."}
        ]
    },
    {
        "slug": "spelling-bucheo-vs-butyeo",
        "category": "맞춤법",
        "category_slug": "category-spelling.html",
        "category_icon": "📝",
        "title": "'부치다' vs '붙이다' 구별법 - 편지를 부치고 우표를 붙이는 원리",
        "description": "발음이 같아 헷갈리는 '부치다'와 '붙이다' 완벽 정리! 맞닿아 떨어지지 않게 하는 '붙다'의 사동사 '붙이다'와 나머지 '부치다'의 차이.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 한국어 어문연구팀",
        "summary": [
            "맞닿아 떨어지지 않게 하거나 불이 옮겨붙게 할 때는 사동사 '붙이다'를 씁니다.",
            "물리적 접촉과 무관한 송금, 부채질, 전 부치기, 힘에 겹다는 모두 '부치다'입니다.",
            "'우표를 붙이고 편지를 부친다' 한 문장으로 완벽하게 구별할 수 있습니다."
        ],
        "content_html": """
        <p class="lead-text">
          한국어 맞춤법에서 가장 혼란스러운 쌍 중 하나가 발음이 [부치다]로 똑같은 <strong>'부치다'</strong>와 <strong>'붙이다'</strong>입니다. "조건을 붙이다/부치다?", "회의에 부치다/붙이다?" 등 상황마다 헷갈리기 십상입니다.
        </p>

        <h2 class="article-h2">1. 판별의 핵심: '붙다'의 의미가 살아있는가?</h2>
        <p>
          한글 맞춤법 제22항과 제57항에 따르면, <strong>'붙다'의 의미(물리적 접촉, 점착, 착수)가 살아있는 경우</strong>에는 어간 '붙-'을 밝혀 적어 <strong>'붙이다'</strong>로 표기합니다.
        </p>
        <p>
          반면, '붙다'의 고유 의미가 사라졌거나 전혀 다른 뜻을 가진 단어들은 소리 나는 대로 <strong>'부치다'</strong>로 적습니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>'붙이다' (접착·밀착·접촉)</th>
                <th>'부치다' (발송·위탁·요리 등)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>물리적 접촉</strong></td>
                <td><span class="correct-text">벽에 포스터를 붙이다</span></td>
                <td><span class="wrong-text">벽에 포스터를 부치다 (X)</span></td>
              </tr>
              <tr>
                <td><strong>우편 / 송금</strong></td>
                <td><span class="wrong-text">고향에 생활비를 붙이다 (X)</span></td>
                <td><span class="correct-text">고향에 생활비를 부치다</span></td>
              </tr>
              <tr>
                <td><strong>바람 / 조리</strong></td>
                <td><span class="wrong-text">김치전을 붙이다 (X)</span></td>
                <td><span class="correct-text">부채를 부치다 / 전을 부치다</span></td>
              </tr>
              <tr>
                <td><strong>안건 / 의사결정</strong></td>
                <td><span class="wrong-text">표결에 붙이다 (X)</span></td>
                <td><span class="correct-text">안건을 표결에 부치다</span></td>
              </tr>
              <tr>
                <td><strong>승부 / 흥미</strong></td>
                <td><span class="correct-text">승부를 붙이다 / 취미를 붙이다</span></td>
                <td><span class="wrong-text">승부를 부치다 (X)</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 3초 암기 공식: "풀칠이나 접착이 필요하면 '붙이다'!"</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 끝내는 치트키:</strong><br>
          테이프나 풀로 <strong>물리적으로 맞닿게 하는 것</strong>은 <strong>'붙이다'</strong>!<br>
          나머지(편지 보내기, 전 부치기, 부채질, 표결, 비밀)는 100% <strong>'부치다'</strong>!
        </div>

        <h2 class="article-h2">3. 실생활 올바른 문장 예시</h2>
        <ul class="example-list">
          <li>"봉투에 우표를 <strong>붙여서</strong> 우체통에 편지를 <strong>부쳤다</strong>." (O - 최고의 예문)</li>
          <li>"새로운 프로젝트를 기획하느라 이번 주는 힘에 <strong>부치는</strong> 일정이었다." (O)</li>
          <li>"이 사건의 전말은 국가 안보상 극비에 <strong>부치기로</strong> 결정했다." (O)</li>
          <li>"책상 모서리에 안전 보호대를 단단히 <strong>붙였다</strong>." (O)</li>
        </ul>
        """,
        "quiz": {
            "q": "해외로 유학 간 자녀에게 매달 학비와 생활비를 계좌로 [{A} / {B}] 준다.",
            "a": "부쳐",
            "b": "붙여",
            "correct": "A",
            "exp": "돈이나 물건을 보내는 행위는 '붙다'의 의미가 없으므로 '부치다(부쳐)'가 표준어입니다."
        },
        "faq": [
            {"q": "'불을 부치다'와 '불을 붙이다' 중 무엇이 맞나요?", "a": "'불을 붙이다'가 맞습니다. 불이 닿아 타기 시작하는 것은 '붙다'의 사동사이므로 '붙이다'로 표기합니다."},
            {"q": "'취미를 붙이다'는 왜 '붙이다'인가요?", "a": "마음이 어떤 대상에 착 달라붙어 정을 들인다는 의미이므로 '붙다'의 뜻이 유지되어 '붙이다'로 적습니다."}
        ]
    },
    {
        "slug": "spelling-eotteokdeun-vs-eotteoke",
        "category": "맞춤법",
        "category_slug": "category-spelling.html",
        "category_icon": "📝",
        "title": "'어떻든' vs '어떡든' - '어떻게 하든'의 올바른 축약형과 '어쨌든'의 관계",
        "description": "'어떻든 간에'일까 '어떡든 간에'일까? 형용사 '어떻다'의 어간에 어미 '-든'이 붙은 '어떻든'과 '어찌 되었든'의 준말 '어쨌든' 완벽 정리.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 한국어 어문연구팀",
        "summary": [
            "'어떠하든'의 준말은 히읗 받침이 있는 '어떻든'입니다.",
            "'어떡든'이라는 표기는 표준국어대사전에 존재하지 않는 비표준어입니다.",
            "'어떻든(상태 무관)'과 '어쨌든(어찌 되었든/결과 중심)'의 쓰임새를 구분해야 합니다."
        ],
        "content_html": """
        <p class="lead-text">
          "결과가 어떡든 최선을 다하자"처럼 무심코 '어떡든'을 사용하는 경우가 많습니다. '어떡해'라는 표현이 익숙해서 '어떡든'도 표준어라고 착각하기 쉽지만, 올바른 표준어는 <strong>'어떻든'</strong>입니다.
        </p>

        <h2 class="article-h2">1. 문법적 원리: '어떠하든'의 줄임말</h2>
        <p>
          '어떻든'은 형용사 <strong>'어떠하다'</strong>의 줄임말인 <strong>'어떻다'</strong>의 어간 <em>'어떻-'</em>에 선택이나 조건을 나타내는 연결어미 <em>'-든'</em>이 결합한 말입니다.
        </p>
        <p>
          반면 <strong>'어떡해'</strong>는 '어떻게 해'라는 구(Phrase)가 줄어든 서술어입니다. 따라서 '-든'이라는 어미 앞에는 동사구가 축약된 '어떡-'이 올 수 없으며, 형용사 어간 '어떻-'이 와서 <strong>'어떻든'</strong>이 되어야 합니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>원말</th>
                <th>올바른 줄임말</th>
                <th>틀린 표현</th>
                <th>예문</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>어떠하든</strong></td>
                <td><span class="correct-text">어떻든</span></td>
                <td><span class="wrong-text">어떡든</span></td>
                <td>이유가 어떻든 간에</td>
              </tr>
              <tr>
                <td><strong>어떠하여도</strong></td>
                <td><span class="correct-text">어떻든가</span></td>
                <td><span class="wrong-text">어떡든가</span></td>
                <td>형편이 어떻든가 상관없이</td>
              </tr>
              <tr>
                <td><strong>어찌 되었든</strong></td>
                <td><span class="correct-text">어쨌든</span></td>
                <td><span class="wrong-text">어째든</span></td>
                <td>어쨌든 결론을 내야 한다</td>
              </tr>
              <tr>
                <td><strong>어떻게 해</strong></td>
                <td><span class="correct-text">어떡해</span></td>
                <td><span class="wrong-text">어떻해</span></td>
                <td>지갑을 잃어버렸는데 어떡해</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 3초 직관 암기 공식: "조건을 고를 땐 '어떻든'!"</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 끝내는 공식:</strong><br>
          "세상에 <strong>'어떡든'</strong>이란 단어는 없다!"<br>
          ~든(선택)이 붙을 때는 히읗 받침 <strong>'어떻든'</strong>만 존재합니다.
        </div>

        <h2 class="article-h2">3. 실생활 올바른 문장 예시</h2>
        <ul class="example-list">
          <li>"상황이 <strong>어떻든</strong> 간에 약속 시간은 엄수해야 합니다." (O)</li>
          <li>"남들이 뭐라고 평가하든 내 생각이 <strong>어떻든</strong> 그게 중요해." (O)</li>
          <li>"<strong>어쨌든</strong> 우리는 이번 분기 목표를 100% 달성했습니다." (O)</li>
        </ul>
        """,
        "quiz": {
            "q": "주변 여건이 [{A} / {B}] 우리는 끝까지 포기하지 않고 완주해야 한다.",
            "a": "어떻든",
            "b": "어떡든",
            "correct": "A",
            "exp": "'어떠하든'의 올바른 준말은 히읗 받침이 있는 '어떻든'입니다. '어떡든'은 비표준어입니다."
        },
        "faq": [
            {"q": "'어쨌든'과 '어떻든'은 같은 뜻인가요?", "a": "'어쨌든'은 '어찌 되었든(과거/기정 사실 무시)'의 준말이며, '어떻든'은 '어떠하든(어떤 조건/상태이든)'의 준말입니다. 뉘앙스는 비슷하지만 문법적 구성이 다릅니다."},
            {"q": "'어떻튼'으로 쓰는 것은 맞나요?", "a": "'어떻튼'은 틀린 표기입니다. 선택을 나타내는 어미는 '-든'이므로 '어떻든'으로 적어야 합니다."}
        ]
    },

    # ==================== 2. 시사·경제 (Economy & Current Affairs) - 5 New (Total 10) ====================
    {
        "slug": "economy-shrinkflation-greedflation",
        "category": "시사·경제",
        "category_slug": "category-economy.html",
        "category_icon": "💡",
        "title": "슈링크플레이션과 그리드플레이션 - 양을 줄여 가격을 올리는 기업의 꼼수",
        "description": "'줄어들다(Shrink)'와 '인플레이션'의 합성어 슈링크플레이션! 가격은 그대로 두고 용량을 줄이는 스텔스 인플레이션의 메커니즘과 소비자 권리.",
        "read_time": "4분",
        "date": "2026-10-15",
        "author": "딱1분 시사경제 분석팀",
        "summary": [
            "슈링크플레이션은 제품 가격은 동결한 채 중량이나 용량을 줄여 실질 가격을 인상하는 전략입니다.",
            "그리드플레이션은 원자재 가격 상승을 핑계로 기업이 과도한 이윤(탐욕)을 추구하며 폭리를 취하는 현상입니다.",
            "정부는 포장지에 용량 변경 사실 표기를 의무화하는 등 소비자 기만 방지 규제를 강화하고 있습니다."
        ],
        "content_html": """
        <p class="lead-text">
          평소 사 먹던 과자의 가격은 그대로인데, 봉지를 뜯어보니 양이 부쩍 줄어든 느낌을 받은 적이 있으신가요? 단순한 기분 탓이 아닙니다. 원자재 가격 상승 압박 속에서 소비자의 가격 저항을 피하고자 기업들이 애용하는 <strong>'슈링크플레이션(Shrinkflation)'</strong>의 전형적인 사례입니다.
        </p>

        <h2 class="article-h2">1. 슈링크플레이션(Shrinkflation)의 작동 원리</h2>
        <p>
          슈링크플레이션은 '줄어들다'라는 뜻의 영어 단어 <strong>Shrink</strong>와 <strong>Inflation</strong>의 합성어입니다. 가격표에 적힌 소비자가격을 올리면 소비자들이 즉각적으로 지갑을 닫기 때문에, 가격은 그대로 유지하면서 내용물의 용량이나 개수를 5~10% 줄이는 <em>'스텔스(Stealth) 가격 인상'</em> 수법입니다.
        </p>
        <p>
          예를 들어, 1,000원에 100g이던 초콜릿을 가격은 1,000원으로 유지한 채 80g으로 줄인다면, 10g당 가격은 100원에서 125원으로 사실상 <strong>25% 급등</strong>한 셈입니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>용어</th>
                <th>어원</th>
                <th>핵심 특징 및 기업 수법</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>슈링크플레이션</strong></td>
                <td>Shrink + Inflation</td>
                <td>가격 동결 후 용량·중량 축소 (실질 단가 인상)</td>
              </tr>
              <tr>
                <td><strong>스킴플레이션</strong></td>
                <td>Skimp(아끼다) + Inflation</td>
                <td>원재료 품질 저하 (예: 버터 대신 저가 팜유 대체)</td>
              </tr>
              <tr>
                <td><strong>그리드플레이션</strong></td>
                <td>Greed(탐욕) + Inflation</td>
                <td>물가 상승을 핑계로 원가 인상분 이상의 과도한 이익 편취</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 소비자 대응법과 단위가격 표시제</h2>
        <p>
          슈링크플레이션의 함정에 빠지지 않기 위해서는 대형마트나 온라인 쇼핑몰에서 총 결제액이 아닌 <strong>'단위당 가격(10g당 가격, 100ml당 가격)'</strong>을 꼼꼼히 확인하는 습관이 필수적입니다.
        </p>
        <p>
          공정거래위원회는 소비자의 알 권리를 보장하기 위해 주요 생필품 및 가공식품의 용량이 줄어들 경우 제조사가 포장지나 공식 홈페이지에 의무적으로 고지하도록 규정을 신설했습니다.
        </p>

        <h2 class="article-h2">3. 3초 경제 상식 팁</h2>
        <div class="tip-box-article">
          <strong>💡 핵심 요약:</strong><br>
          가격은 그대로인데 과자 봉지의 질소만 늘어났다면? ➔ <strong>슈링크플레이션!</strong><br>
          원료를 싸구려로 몰래 바꿨다면? ➔ <strong>스킴플레이션!</strong>
        </div>
        """,
        "quiz": {
            "q": "제조사가 과자의 판매 가격은 2,000원으로 유지하면서 중량을 100g에서 80g으로 줄여 실질적 가격 인상을 꾀하는 현상은 [{A} / {B}]이다.",
            "a": "슈링크플레이션",
            "b": "디플레이션",
            "correct": "A",
            "exp": "제품의 가격을 올리지 않는 대신 용량을 줄여 간접적으로 단위당 가격을 인상하는 수법을 슈링크플레이션이라고 합니다."
        },
        "faq": [
            {"q": "슈링크플레이션은 법적으로 불법인가요?", "a": "용량을 줄이는 자체는 기업의 자유이므로 불법이 아닙니다. 하지만 용량 변경 사실을 소비자에게 알리지 않고 속여 판매하는 행위는 표시광고법 위반 및 과태료 부과 대상이 될 수 있습니다."},
            {"q": "그리드플레이션이란 구체적으로 어떤 사례인가요?", "a": "원자재 가격이 10% 올랐을 때, 기업이 이를 핑계 삼아 제품 가격을 30% 인상하여 사상 최대 영업이익을 챙기는 기업의 탐욕적 인플레이션을 의미합니다."}
        ]
    },
    {
        "slug": "economy-short-selling-mechanism",
        "category": "시사·경제",
        "category_slug": "category-economy.html",
        "category_icon": "💡",
        "title": "공매도(Short Selling)의 원리와 시장 영향 - 주가 하락에 베팅하는 투자의 구조",
        "description": "없는 주식을 빌려 파는 '공매도'란 무엇일까? 주가 거품 제거라는 순기능과 개미 투자자들의 불만 사이의 경제적 쟁점을 쉽게 해설합니다.",
        "read_time": "4분",
        "date": "2026-10-15",
        "author": "딱1분 시사경제 분석팀",
        "summary": [
            "공매도는 주식을 보유하지 않은 상태에서 빌려 먼저 판 뒤, 주가가 떨어지면 사서 갚는 투자 기법입니다.",
            "주가 하락 시 수익을 얻으므로 하락장에서도 이익을 낼 수 있지만, 주가 상승 시 이론상 손실이 무한대입니다.",
            "시장 과열 억제와 유동성 공급이라는 순기능과 시세 조종 및 불공정 논란이라는 역기능이 공존합니다."
        ],
        "content_html": """
        <p class="lead-text">
          뉴스에서 주식 시장 관련 소식을 접할 때마다 뜨거운 감자로 떠오르는 단어가 바로 <strong>'공매도(Short Selling)'</strong>입니다. 주가가 내려가야 돈을 버는 이 독특한 매매 기법은 왜 존재하며 금융 시장에서 어떤 역할을 할까요?
        </p>

        <h2 class="article-h2">1. 공매도의 기본 매커니즘: 빌려서 팔고, 싸게 사서 갚는다</h2>
        <p>
          공매도(空賣渡)의 '공(空)'은 '빌 공' 자로, 글자 그대로 <em>'없는 것을 판다'</em>는 뜻입니다. 일반적인 투자는 [싸게 사서 → 비싸게 파는] 구조지만, 공매도는 순서가 정반대입니다:
        </p>
        <ol class="step-list">
          <li><strong>주식 대여:</strong> 주가가 10만 원인 A기업의 주식을 기관이나 타인에게서 빌립니다.</li>
          <li><strong>시장 매도:</strong> 빌린 주식을 즉시 시장에 10만 원에 팔아 현금 10만 원을 확보합니다.</li>
          <li><strong>주가 하락:</strong> 예상대로 A기업의 주가가 6만 원으로 폭락합니다.</li>
          <li><strong>쇼트커버링(되사서 갚기):</strong> 시장에서 6만 원에 주식을 다시 사서 원래 주인에게 갚습니다.</li>
          <li><strong>차익 실현:</strong> 10만 원에 팔고 6만 원에 되샀으므로 주당 <strong>4만 원의 순수익</strong>을 거둡니다.</li>
        </ol>

        <h2 class="article-h2">2. 공매도의 장단점 비교</h2>
        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>순기능 (장점)</th>
                <th>역기능 및 위험 (단점)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>가격 발견</strong></td>
                <td>기업 가치 대비 과도한 버블(거품) 방지</td>
                <td>악의적인 악성 루머 유포로 주가 인위적 폭락 유도 가능</td>
              </tr>
              <tr>
                <td><strong>시장 효율성</strong></td>
                <td>거래 유동성을 풍부하게 공급</td>
                <td>기관·외국인 대비 개인 투자자의 접근성 불평등 (기울어진 운동장)</td>
              </tr>
              <tr>
                <td><strong>투자 위험</strong></td>
                <td>하락장에서도 헤지(위험 분산) 수단 활용</td>
                <td>주가가 폭등할 경우 <strong>손실액이 무한대(∞)</strong>로 확대 위험</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 한 줄 정리:</strong><br>
          일반 투자자: "주가야 올라라! (매수)" ➔ <strong>롱(Long) 포지션</strong><br>
          공매도 투자자: "주가야 떨어져라! (빌려 팔기)" ➔ <strong>숏(Short) 포지션</strong>
        </div>
        """,
        "quiz": {
            "q": "주식을 보유하지 않은 상태에서 빌려 먼저 매도한 뒤, 나중에 주가가 하락하면 싼값에 되사서 차익을 노리는 투자 기법은 [{A} / {B}]이다.",
            "a": "공매도",
            "b": "유상증자",
            "correct": "A",
            "exp": "주가 하락에 베팅하여 주식을 빌려 팔고 다시 사서 갚는 방식을 공매도(Short Selling)라고 합니다."
        },
        "faq": [
            {"q": "주식을 빌리지 않고 파는 무차입 공매도는 합법인가요?", "a": "한국 자본시장법상 주식을 빌리지 않고 매도 주문을 내는 '무차입 공매도(Naked Short Selling)'는 불법이며 엄중한 형사 처벌과 과징금 부과 대상입니다."},
            {"q": "'숏 스퀴즈(Short Squeeze)'란 무엇인가요?", "a": "공매도 세력의 예상과 달리 주가가 급등할 때, 더 큰 손실을 막기 위해 공매도 투자자들이 패닉에 빠져 주식을 앞다투어 사들이며 주가가 폭등하는 현상입니다."}
        ]
    },
    {
        "slug": "economy-circuit-breaker-sidecar",
        "category": "시사·경제",
        "category_slug": "category-economy.html",
        "category_icon": "💡",
        "title": "서킷브레이커와 사이드카 - 주식 시장 폭락 시 거래를 멈추는 안전장치",
        "description": "코스피·코스닥 급변동 시 발동되는 서킷브레이커(1·2·3단계)와 선물 시장의 사이드카의 발동 조건 및 냉각 효과를 명쾌하게 비교합니다.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 시사경제 분석팀",
        "summary": [
            "서킷브레이커는 현물 지수가 8%, 15%, 20% 폭락할 때 모든 주식 매매를 강제 중단하는 제도입니다.",
            "사이드카는 선물 시장 가격이 급변할 때 프로그램 매매 호가 효력을 5분간 일시 정지시킵니다.",
            "전기 회로의 과열을 막는 두꺼비집처럼 시장의 집단 패닉을 진정시키는 '쿨링 타임' 역할을 합니다."
        ],
        "content_html": """
        <p class="lead-text">
          세계적인 경제 위기나 전쟁, 팬데믹이 터지면 증시가 패닉에 빠지며 지수가 수직 낙하합니다. 이때 증권거래소는 전광판을 멈추고 거래를 일시 중단시키는 비상조치를 발동하는데, 이것이 바로 <strong>'서킷브레이커(Circuit Breakers)'</strong>와 <strong>'사이드카(Sidecar)'</strong>입니다.
        </p>

        <h2 class="article-h2">1. 서킷브레이커(Circuit Breaker): 주식 매매의 전면 중단</h2>
        <p>
          전기 회로에서 과전류가 흐르면 두꺼비집(차단기)이 내려가 화재를 막듯, 주가가 비정상적으로 폭락할 때 투자자들에게 냉정을 찾을 시간을 주기 위해 매매를 전면 중단하는 제도입니다. 1987년 미국 뉴욕증시의 '블랙 먼데이' 폭락 이후 도입되었습니다.
        </p>
        <p>
          한국 증시(코스피, 코스닥)의 서킷브레이커는 전일 대비 하락률에 따라 3단계로 운영됩니다:
        </p>
        <ul class="step-list">
          <li><strong>1단계 (8% 이상 하락):</strong> 1분 이상 지속 시 모든 주식 매매 20분간 전면 중단 (이후 10분 단일가 매매)</li>
          <li><strong>2단계 (15% 이상 하락 및 1단계 대비 1%p 추가 하락):</strong> 20분간 전면 중단</li>
          <li><strong>3단계 (20% 이상 하락 및 2단계 대비 1%p 추가 하락):</strong> 당일 정규장 <strong>즉시 조기 종료(장 마감)</strong></li>
        </ul>

        <h2 class="article-h2">2. 사이드카(Sidecar): 프로그램 매매 일시 정지</h2>
        <p>
          오토바이 옆에 달린 보조 의자(Sidecar)처럼 본체(현물)의 충격을 완화하기 위해 선물 시장의 급등락이 현물 시장으로 전이되는 것을 막는 완충 장치입니다.
        </p>
        <p>
          선물 가격이 5% 이상(코스피) 변동하여 1분간 지속될 때 발동되며, 컴퓨터 알고리즘에 의한 <strong>프로그램 매매의 호가 효력을 5분간 정지</strong>시킵니다. 서킷브레이커와 달리 일반인의 개별 주식 주문은 계속 체결됩니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>서킷브레이커 (CB)</th>
                <th>사이드카 (Sidecar)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>대상 시장</strong></td>
                <td>현물 주식 시장 (코스피, 코스닥)</td>
                <td>선물 시장 변동에 따른 프로그램 매매</td>
              </tr>
              <tr>
                <td><strong>발동 조건</strong></td>
                <td>지수 8%, 15%, 20% 폭락 시</td>
                <td>선물 가격 5%(코스피) / 6%(코스닥) 급변동</td>
              </tr>
              <tr>
                <td><strong>조치 강도</strong></td>
                <td><strong>모든 매매 전면 정지 (20분간)</strong></td>
                <td><strong>프로그램 매매 호가만 5분간 유예</strong></td>
              </tr>
              <tr>
                <td><strong>발동 방향</strong></td>
                <td>오직 <strong>하락(폭락)</strong> 시에만 발동</td>
                <td><strong>상승/하락</strong> 양방향 모두 발동</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 끝내는 구분법:</strong><br>
          모든 거래를 아예 셧다운시키는 메인 스위치 ➔ <strong>서킷브레이커!</strong><br>
          컴퓨터 대량 주문만 5분 쉬어가게 하는 보조 장치 ➔ <strong>사이드카!</strong>
        </div>
        """,
        "quiz": {
            "q": "주식 시장 지수가 전일 대비 8% 이상 급락하여 발동되며, 모든 주식 매매를 20분간 전면 중단시키는 제도는 [{A} / {B}]이다.",
            "a": "서킷브레이커",
            "b": "사이드카",
            "correct": "A",
            "exp": "지수 급락 시 전 종목의 매매를 20분간 올스톱시키는 시장 냉각 제도는 서킷브레이커입니다."
        },
        "faq": [
            {"q": "서킷브레이커는 하루에 여러 번 발동될 수 있나요?", "a": "각 단계별로 하루에 단 1회씩만 발동될 수 있습니다. 또한 장 마감 40분 전(오후 2시 50분) 이후에는 1·2단계 서킷브레이커를 발동하지 않습니다 (3단계는 장 마감 발동 가능)."},
            {"q": "주가가 폭등할 때도 서킷브레이커가 켜지나요?", "a": "아닙니다. 한국 증시에서 서킷브레이커는 시장 붕괴 방지를 위해 오직 지수가 '폭락'할 때만 작동합니다. 반면 사이드카는 급등 시에도 발동됩니다."}
        ]
    },
    {
        "slug": "economy-etf-fund-difference",
        "category": "시사·경제",
        "category_slug": "category-economy.html",
        "category_icon": "💡",
        "title": "ETF와 일반 펀드의 결정적 차이 - 실시간 주식 매매와 운용보수의 경제학",
        "description": "상장지수펀드(ETF)와 공모 펀드는 무엇이 다를까? 장중 실시간 거래, 저렴한 수수료, 분산 투자 효과까지 초보 투자자를 위한 비교 총정리.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 시사경제 분석팀",
        "summary": [
            "ETF는 주식 시장에 상장되어 주식처럼 실시간으로 1주 단위 매매가 가능한 펀드입니다.",
            "일반 펀드 대비 운용보수(수수료)가 매우 저렴하며 포트폴리오 편입 종목이 투명하게 공개됩니다.",
            "소액으로도 코스피200, S&P500, 반도체, 2차전지 등 시장 전체에 분산 투자할 수 있습니다."
        ],
        "content_html": """
        <p class="lead-text">
          재테크에 관심을 갖기 시작하면 가장 먼저 마주치는 단어가 바로 <strong>ETF(상장지수펀드)</strong>입니다. 은행이나 증권사에서 가입하던 전통적인 펀드와 ETF는 도대체 무엇이 다르기에 전 세계 투자자들의 자금을 블랙홀처럼 빨아들이고 있을까요?
        </p>

        <h2 class="article-h2">1. ETF(Exchange Traded Fund)의 정체</h2>
        <p>
          ETF는 <strong>펀드(Fund)를 주식 시장(Exchange)에 상장시켜 주식처럼 사고팔 수 있게 만든 금융상품</strong>입니다.
        </p>
        <p>
          예를 들어 삼성전자, SK하이닉스 등 국내 우량 반도체 기업 20개에 골고루 투자하고 싶다면, 예전에는 수천만 원의 종잣돈이 필요하거나 은행 펀드 창구에 가야 했습니다. 하지만 'KODEX 반도체' 같은 ETF 1주(약 3만 원)만 사면, 그 1주 안에 20개 반도체 회사의 주식이 지분율대로 쪼개져 담겨있는 효과를 누릴 수 있습니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>비교 항목</th>
                <th>상장지수펀드 (ETF)</th>
                <th>전통 공모 펀드</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>매매 방식</strong></td>
                <td>스마트폰 앱(MTS)으로 장중 <strong>실시간 매매</strong></td>
                <td>은행/증권사 창구 또는 앱 신청 후 며칠 뒤 기준가 환매</td>
              </tr>
              <tr>
                <td><strong>총보수 (수수료)</strong></td>
                <td><strong>연 0.05% ~ 0.5% (매우 저렴)</strong></td>
                <td>연 1.0% ~ 2.5% (상대적 고비용)</td>
              </tr>
              <tr>
                <td><strong>포트폴리오 투명성</strong></td>
                <td>매일 담긴 주식 내역 실시간 공개(PDF)</td>
                <td>분기별 운용보고서로 사후 확인</td>
              </tr>
              <tr>
                <td><strong>최소 투자 금액</strong></td>
                <td>1주 가격 (수천 원 ~ 수만 원대)</td>
                <td>자유 적립 또는 일정 금액 이상</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 초보자를 위한 3초 투자 팁</h2>
        <div class="tip-box-article">
          <strong>💡 핵심 공식:</strong><br>
          "펀드의 분산 투자 장점 + 주식의 실시간 매매 편리함 + 반값 수수료"<br>
          = <strong>ETF(상장지수펀드)!</strong>
        </div>

        <h2 class="article-h2">3. 대표적인 ETF 기초 지수</h2>
        <ul class="example-list">
          <li><strong>시장 대표 지수:</strong> KOSPI 200, 미국 S&P 500, 나스닥 100 추종 ETF</li>
          <li><strong>섹터/테마형:</strong> 2차전지, 인공지능(AI), 바이오, 조선업 ETF</li>
          <li><strong>자산 배분형:</strong> 미국 국채, 금(Gold), 원유, 배당성장주 ETF</li>
        </ul>
        """,
        "quiz": {
            "q": "특정 지수를 추종하며 증권거래소에 상장되어 주식처럼 실시간으로 자유롭게 사고팔 수 있는 펀드는 [{A} / {B}]이다.",
            "a": "ETF",
            "b": "적금",
            "correct": "A",
            "exp": "상장지수펀드(ETF)는 펀드의 분산 투자 특성과 주식의 실시간 거래 편의성을 결합한 상품입니다."
        },
        "faq": [
            {"q": "ETF도 일반 주식처럼 배당금을 주나요?", "a": "네, ETF가 담고 있는 종목들에서 발생하는 배당금과 이자를 모아 투자자들에게 '분배금'이라는 명칭으로 정기적으로 지급합니다."},
            {"q": "ETF 이름 앞에 붙는 TIGER, KODEX, ACE는 무엇인가요?", "a": "각 자산운용사의 고유 브랜드명입니다. TIGER는 미래에셋, KODEX는 삼성, ACE는 한국투자신탁운용의 브랜드입니다."}
        ]
    },
    {
        "slug": "economy-greenwashing-esg",
        "category": "시사·경제",
        "category_slug": "category-economy.html",
        "category_icon": "💡",
        "title": "그린워싱(Greenwashing) 판별법 - 무늬만 친환경인 위장 환경주의와 ESG",
        "description": "실제로는 탄소를 배출하면서 친환경인 척 포장하는 '그린워싱'의 7대 죄악과 기업들의 ESG 마케팅을 감별하는 기준을 제시합니다.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 시사경제 분석팀",
        "summary": [
            "그린워싱은 실제 친환경 활동보다 친환경 홍보에 치중하는 '위장 환경주의'를 뜻합니다.",
            "친환경 종이 빨대, 무라벨 생수통 등 마케팅 이면에 숨은 전 과정 탄소 배출을 살펴야 합니다.",
            "ESG 평가의 신뢰성을 높이기 위해 공정위와 금융당국이 공시 기준을 강화하고 있습니다."
        ],
        "content_html": """
        <p class="lead-text">
          카페에 가면 제공되는 종이 빨대, 초록색 잎사귀 로고가 박힌 화장품 용기, '에코(Eco)'라는 단어가 붙은 생필품들. 요즘 기업 마케팅의 대세는 단연 친환경입니다. 하지만 이 중 상당수가 소비자를 현혹하기 위한 <strong>'그린워싱(Greenwashing, 위장 환경주의)'</strong>이라는 사실을 알고 계셨나요?
        </p>

        <h2 class="article-h2">1. 그린워싱의 정의와 유래</h2>
        <p>
          그린워싱은 <strong>녹색(Green)</strong>과 세탁을 뜻하는 <strong>화이트워싱(White washing)</strong>의 합성어입니다. 기업이 실질적으로는 환경 보호나 탄소 저감에 기여하지 않으면서, 광고나 라벨링을 통해 마치 친환경적인 기업인 것처럼 위장하는 마케팅 행태를 꼬집는 경제 용어입니다.
        </p>

        <h2 class="article-h2">2. 대표적인 그린워싱 사례</h2>
        <ul class="example-list">
          <li><strong>종이컵의 배신:</strong> 플라스틱 대신 종이컵을 쓴다고 홍보하지만, 방수를 위해 내부에 코팅된 폴리에틸렌(PE) 때문에 재활용이 불가능하고 일반 쓰레기로 소각되는 경우.</li>
          <li><strong>가짜 에코백 프로모션:</strong> 환경을 보호하자며 텀블러와 에코백을 시즌마다 수백만 개씩 한정판으로 제작·판매하여 오히려 자원을 낭비하는 역설.</li>
          <li><strong>증거 없는 친환경 인증:</strong> 공인된 환경부 친환경 마크가 아닌 자체적으로 만든 녹색 나뭇잎 스티커를 부착해 소비자를 오인하게 만드는 행위.</li>
        </ul>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>진짜 친환경 (Eco-Friendly)</th>
                <th>그린워싱 (Greenwashing)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>인증 여부</strong></td>
                <td>환경부 공인 친환경 표지 인증 획득</td>
                <td>공인 기관 검증 없는 자체 도안·문구 사용</td>
              </tr>
              <tr>
                <td><strong>전 과정 평가</strong></td>
                <td>생산·유통·폐기 전 과정에서 탄소 저감</td>
                <td>일부 홍보용 부품만 교체 후 전체 친환경 둔갑</td>
              </tr>
              <tr>
                <td><strong>정보 공개</strong></td>
                <td>탄소 배출 데이터와 감축 실적 투명 공시</td>
                <td>모호한 친환경 이미지와 감성 마케팅에 의존</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 한 줄 정의:</strong><br>
          "실제 행동은 공해 유발, 포장지만 녹색으로 세탁하는 꼼수!"<br>
          ➔ <strong>그린워싱(위장 환경주의)</strong>
        </div>
        """,
        "quiz": {
            "q": "실제로는 친환경적이지 않으면서 상품의 친환경적 특성만을 과장하거나 홍보하여 소비자를 속이는 행위를 가리키는 용어는 [{A} / {B}]이다.",
            "a": "그린워싱",
            "b": "어닝쇼크",
            "correct": "A",
            "exp": "녹색(Green)과 돈세탁(Whitewash)의 합성어로 위장 환경주의를 뜻하는 용어는 그린워싱입니다."
        },
        "faq": [
            {"q": "친환경 마크를 위조하면 어떤 처벌을 받나요?", "a": "환경산업기술원의 인증 없이 임의로 환경표지 마크를 무단 도용하거나 허위 과장 광고를 할 경우 환경기술산업법에 따라 형사 고발 및 2년 이하의 징역형을 받을 수 있습니다."},
            {"q": "소비자가 쉽게 진짜 친환경 제품을 찾는 방법은?", "a": "한국환경산업기술원의 '녹색제품정보시스템'에서 환경부 공식 환경표지(에코마크) 인증을 받은 제품인지 모델명으로 조회할 수 있습니다."}
        ]
    },

    # ==================== 3. 역사·문화 (History & Culture) - 5 New (Total 10) ====================
    {
        "slug": "history-gwanggaeto-jangsu-king",
        "category": "역사·문화",
        "category_slug": "category-history.html",
        "category_icon": "🏛️",
        "title": "광개토대왕과 장수왕의 남진 정책 - 5세기 고구려 전성기의 영토 확장사",
        "description": "북진 정책으로 만주를 호령한 광개토대왕과 427년 평양 천도로 한강 유역을 장악한 장수왕의 남진 정책! 고구려 최전성기의 역사적 의의.",
        "read_time": "4분",
        "date": "2026-10-15",
        "author": "딱1분 역사문화 연구팀",
        "summary": [
            "광개토대왕은 북쪽으로 요동과 만주 벌판을 개척하며 '영락'이라는 독자적 연호를 사용했습니다.",
            "장수왕은 427년 평양으로 수도를 옮기고 적극적인 남진 정책을 추진해 한강 유역을 차지했습니다.",
            "충주고구려비와 광개토대왕릉비는 5세기 동아시아 강국 고구려의 위상을 증명하는 국보급 유물입니다."
        ],
        "content_html": """
        <p class="lead-text">
          삼국시대의 지도에서 한반도의 절반과 광활한 만주 벌판이 고구려의 영토로 붉게 칠해진 시기가 바로 <strong>5세기 고구려의 최전성기</strong>입니다. 아버지 광개토대왕의 웅대한 북방 개척과 아들 장수왕의 치밀한 남진 정책이 빚어낸 역사적 대업을 살펴봅니다.
        </p>

        <h2 class="article-h2">1. 광개토대왕의 대륙 경영: '영락(永樂)'의 시대</h2>
        <p>
          18세의 나이로 즉위한 광개토대왕(재위 391~412)은 우리나라 역사상 최초로 독자적인 연호인 <strong>'영락(永樂)'</strong>을 사용하여 고구려가 중국과 대등한 천하의 중심임을 선포했습니다.
        </p>
        <p>
          후연을 격파하여 요동반도를 완전히 고구려 영토로 복속시켰으며, 북쪽으로 숙신과 비려를 굴복시켜 광활한 만주 영토를 확보했습니다. 또한 왜구의 침략을 받은 신라 내물왕의 구원 요청을 받고 5만 대군을 보내 왜구를 낙동강 유역에서 궤멸시켰습니다.
        </p>

        <h2 class="article-h2">2. 장수왕의 평양 천도와 남진 정책(427년)</h2>
        <p>
          광개토대왕의 뒤를 이은 장수왕(재위 413~491)은 무려 79년 동안 재위하며 98세까지 장수한 군주입니다. 그는 국내성 귀족들의 권력을 억누르고 한반도 중심부로 진출하기 위해 <strong>427년 수도를 평양으로 전격 이전</strong>했습니다.
        </p>
        <p>
          이에 위협을 느낀 백제와 신라는 '나제동맹(433년)'을 맺어 맞섰으나, 장수왕은 475년 백제의 수도 한성(위례성)을 함락하고 개로왕을 전사시키며 <strong>한강 유역 전체를 차지</strong>했습니다. 남한강 상류의 충주에 세워진 '충주고구려비'는 고구려의 영토가 남양만에서 영일만에 이르렀음을 보여주는 생생한 증거입니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>광개토대왕 (4세기 말~5세기 초)</th>
                <th>장수왕 (5세기)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>주요 전략</strong></td>
                <td>북진 정책 (요동·만주 경영)</td>
                <td>남진 정책 (평양 천도, 한강 장악)</td>
              </tr>
              <tr>
                <td><strong>독자 연호</strong></td>
                <td>영락(永樂) - 고구려 천하관</td>
                <td>중국 남북조와의 다각 외교 전개</td>
              </tr>
              <tr>
                <td><strong>핵심 유물</strong></td>
                <td>광개토대왕릉비 (지린성 집안)</td>
                <td>충주고구려비 (국내 유일 고구려비)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 역사 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 외우는 공식:</strong><br>
          만주 벌판 북쪽으로 넓힌 왕 ➔ <strong>광개토대왕!</strong><br>
          평양 천도하고 한강 남쪽으로 진격한 왕 ➔ <strong>장수왕!</strong>
        </div>
        """,
        "quiz": {
            "q": "수도를 국내성에서 평양으로 천도(427년)하고 적극적인 남진 정책을 추진하여 한강 유역을 차지한 고구려 전성기 군주는 [{A} / {B}]이다.",
            "a": "장수왕",
            "b": "근초고왕",
            "correct": "A",
            "exp": "평양 천도와 한성 함락을 통해 5세기 고구려의 최대 남진 판도를 완성한 왕은 장수왕입니다."
        },
        "faq": [
            {"q": "삼국의 전성기는 어떤 순서로 진행되었나요?", "a": "한강 유역을 차지한 순서와 일치합니다: 4세기 백제(근초고왕) → 5세기 고구려(장수왕) → 6세기 신라(진흥왕) 순서로 전성기를 맞이했습니다."},
            {"q": "장수왕이라는 시호는 왜 붙었나요?", "a": "기록상 기원전후 동아시아 군주 중 가장 긴 79년간 재위하였고 98세까지 천수를 누렸기 때문에 오래 살았다는 뜻의 '장수(長壽)'왕으로 추증되었습니다."}
        ]
    },
    {
        "slug": "history-muryeong-brick-tomb",
        "category": "역사·문화",
        "category_slug": "category-history.html",
        "category_icon": "🏛️",
        "title": "무령왕릉과 백제 벽돌무덤 - 1,440년 만에 온전히 발굴된 유일한 삼국 왕릉",
        "description": "1971년 공주 송산리 고분군에서 도굴되지 않고 발굴된 무령왕릉의 기적! 중국 남조 양나라 양식의 연화문 벽돌무덤과 지석이 밝힌 역사.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 역사문화 연구팀",
        "summary": [
            "삼국시대 왕릉 중 무덤의 주인공과 매장 연대가 명확히 확인된 유일한 왕릉입니다.",
            "중국 남조 양나라의 영향을 받은 정교한 아치형 연화문 벽돌무덤(전축분) 양식입니다.",
            "토지신에게 땅을 샀다는 '매지권'이 적힌 지석과 금제관장식 등 4,600여 점의 유물이 출토되었습니다."
        ],
        "content_html": """
        <p class="lead-text">
          1971년 7월 충남 공주 송산리 6호분 배수로 공사 도중, 인부의 삽 끝에 단단한 벽돌이 걸렸습니다. 조심스레 흙을 걷어내자 1,440여 년 동안 한 번도 도굴되지 않은 채 봉인되어 있던 백제 제25대 <strong>'무령왕릉'</strong>의 입구가 기적처럼 모습을 드러냈습니다.
        </p>

        <h2 class="article-h2">1. 주인이 밝혀진 유일무이한 삼국시대 왕릉</h2>
        <p>
          경주의 천마총이나 황남대총처럼 주인을 몰라 '총(塚)'으로 불리는 신라 고분들과 달리, 무령왕릉이 당당하게 <strong>'릉(陵)'</strong>으로 명명된 이유는 널길 입구에 놓여 있던 <strong>국보 지석(誌石, 묘지석)</strong> 덕분입니다.
        </p>
        <blockquote class="quote-box">
          "영동대장군 백제 사마왕(무령왕)은 나이가 62세 되던 계묘년(523년) 5월에 붕어하시고..."
        </blockquote>
        <p>
          이 묘지석으로 인해 피장자가 무령왕과 왕비임이 완벽하게 증명되었으며, 삼국사기 기록의 정확성이 고고학적으로 입증된 한국 고고학 역사상 최고의 발견이었습니다.
        </p>

        <h2 class="article-h2">2. 국제성이 돋보이는 벽돌무덤(전축분) 양식</h2>
        <p>
          무령왕릉은 돌을 쌓아 만든 전통적인 백제 석실분이 아니라, 연꽃무늬(연화문)가 새겨진 벽돌을 아치형 돔으로 정교하게 쌓아 올린 <strong>벽돌무덤(전축분)</strong>입니다. 이는 당시 백제가 중국 남조의 양(梁)나라와 활발하게 문물을 교류했음을 보여주는 결정적 증거입니다.
        </p>
        <p>
          또한 무덤의 목관은 일본 열도에서만 자생하는 '금송(金松)'으로 제작되어, 백제-중국-일본을 잇는 활발한 해상 교류의 흔적을 생생하게 증언합니다.
        </p>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 핵심 포인트:</strong><br>
          도굴되지 않고 묘지석이 발견된 백제의 벽돌무덤 ➔ <strong>공주 무령왕릉!</strong>
        </div>
        """,
        "quiz": {
            "q": "1971년 공주에서 온전한 상태로 발굴되어 묘지석을 통해 피장자가 완벽히 확인된 백제의 벽돌무덤은 [{A} / {B}]이다.",
            "a": "무령왕릉",
            "b": "장군총",
            "correct": "A",
            "exp": "백제 제25대 무령왕과 왕비의 무덤으로 지석을 통해 축조 연대와 주인이 명확히 밝혀진 무덤은 무령왕릉입니다."
        },
        "faq": [
            {"q": "무령왕릉 발굴이 왜 비판을 받기도 하나요?", "a": "발굴 당시 언론과 대중의 지나친 관심 속에 단 17시간 만에 유물을 서둘러 수습하는 바람에 귀중한 고고학적 맥락과 층위 기록을 놓친 '최악의 졸속 발굴'이라는 뼈아픈 교훈을 남겼습니다."},
            {"q": "무령왕릉에서 출토된 국보는 몇 점인가요?", "a": "왕과 왕비의 금제관장식, 금귀걸이, 지석, 청동거울 등 무려 12건 17점의 유물이 국보로 지정되어 국립공주박물관에 소장되어 있습니다."}
        ]
    },
    {
        "slug": "history-salsu-eulji-mundeok",
        "category": "역사·문화",
        "category_slug": "category-history.html",
        "category_icon": "🏛️",
        "title": "살수대첩과 을지문덕 - 수나라 30만 대군을 수장시킨 청천강의 유인 작전",
        "description": "612년 고구려-수 전쟁의 분수령 살수대첩! 을지문덕 장군의 '여수장우중문시'와 거짓 후퇴, 청천강 물막이 둑 전술의 진실을 파헤칩니다.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 역사문화 연구팀",
        "summary": [
            "612년 수나라 양제의 113만 대군 침략에 맞서 고구려가 거둔 역사적인 대승리입니다.",
            "을지문덕 장군은 거짓 후퇴로 적의 별동대 30만 5천 명을 살수(청천강) 깊숙이 유인했습니다.",
            "살수에서 건너는 적을 맹공하여 살아서 돌아간 수나라 병사가 겨우 2,700명에 불과했습니다."
        ],
        "content_html": """
        <p class="lead-text">
          중국 대륙을 300년 만에 통일한 거대 제국 수나라는 113만 대군이라는 전무후무한 병력을 이끌고 고구려를 침략했습니다. 하지만 고구려에는 적장의 심리를 꿰뚫어 본 지략가 <strong>을지문덕(乙支文德)</strong> 장군이 있었습니다.
        </p>

        <h2 class="article-h2">1. 청야전술과 적의 피로를 유도한 거짓 후퇴</h2>
        <p>
          수나라 양제는 고구려의 요동성이 완강하게 버티자, 30만 5천 명의 최정예 별동대를 편성해 고구려의 수도 평양성을 직접 타격하려 했습니다.
        </p>
        <p>
          을지문덕 장군은 들판의 곡식을 모두 불태우고 우물을 메우는 <strong>'청야(淸野) 전술'</strong>을 펼치며 하루에 일곱 번 싸워 일곱 번 모두 져주는 거짓 후퇴로 적군을 평양성 인근까지 유인했습니다. 보급로가 끊긴 수나라 군대는 굶주림과 극심한 피로에 지쳐 전투력을 완전히 상실했습니다.
        </p>

        <h2 class="article-h2">2. 적장을 조롱한 '여수장우중문시'와 살수 결전</h2>
        <p>
          평양성 앞까지 다다른 수나라 장수 우중문에게 을지문덕은 유명한 한시를 보내 적의 퇴로를 열어주며 심리적 타격을 가했습니다:
        </p>
        <blockquote class="quote-box">
          "신통한 계책은 하늘의 이치를 다했고, 묘한 꾀는 땅의 이치를 꿰뚫었도다.<br>
          전쟁에서 이겨 공이 이미 높으니, 만족함을 알고 그만 돌아감이 어떠한가."
        </blockquote>
        <p>
          전의를 잃고 퇴각하던 수나라 군대가 <strong>살수(현재의 청천강)</strong>를 반쯤 건넜을 때, 매복해 있던 고구려군이 강둑을 터뜨리며 총공격을 감행했습니다. 30만 5천 명 중 압록강을 넘어 살아 돌아간 자는 고작 <strong>2,700명</strong>에 불과했습니다.
        </p>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 정리하는 키워드:</strong><br>
          수나라 격퇴 + 살수(청천강) + 여수장우중문시 ➔ <strong>을지문덕 장군!</strong><br>
          <em>(주의: 거란을 귀주에서 물리친 장군은 강감찬!)</em>
        </div>
        """,
        "quiz": {
            "q": "612년 수나라의 30만 별동대를 거짓 후퇴로 유인한 뒤 살수(청천강)에서 궤멸시킨 고구려의 명장은 [{A} / {B}]이다.",
            "a": "을지문덕",
            "b": "강감찬",
            "correct": "A",
            "exp": "살수대첩에서 수나라 군대를 물리친 장군은 고구려의 을지문덕입니다. 강감찬 장군은 고려 시대 귀주대첩의 영웅입니다."
        },
        "faq": [
            {"q": "살수대첩이 중국 역사에 미친 영향은 무엇인가요?", "a": "무리한 고구려 원정 실패로 막대한 국력을 탕진한 수나라는 각지에서 농민 반란이 일어나며 건국 37년 만에 멸망하고 당나라로 교체되었습니다."},
            {"q": "살수는 현재의 어느 강인가요?", "a": "평안남북도 경계를 흐르는 '청천강'으로 비정되고 있습니다."}
        ]
    },
    {
        "slug": "history-wonhyo-unification-buddhism",
        "category": "역사·문화",
        "category_slug": "category-history.html",
        "category_icon": "🏛️",
        "title": "원효대사의 일체유심조와 해골물 일화 - 모든 것은 마음이 지어낸다는 가르침",
        "description": "당나라 유학길 동굴에서 마신 바가지 물이 해골물이었음을 깨닫고 유학을 포기한 원효대사! 대승기신론소와 화쟁사상으로 민중 불교를 연 발자취.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 역사문화 연구팀",
        "summary": [
            "밤새 달게 마신 물이 아침에 보니 해골에 괸 썩은 물임을 알고 큰 깨달음을 얻었습니다.",
            "'모든 것은 오직 마음먹기에 달렸다'는 일체유심조(一切唯心造)의 화두를 남겼습니다.",
            "귀족 중심의 불교를 '나무아미타불' 염불을 통해 가난한 민중 불교로 대중화했습니다."
        ],
        "content_html": """
        <p class="lead-text">
          어두운 동굴에서 잠결에 마신 시원하고 달콤한 물이, 날이 밝아 확인해보니 시체 썩은 물이 고인 해골바가지였다면 여러분은 어떻게 반응하시겠습니까? 신라 최고의 고승 <strong>원효대사(元曉, 617~686)</strong>는 이 충격적인 경험을 통해 동아시아 불교사를 뒤흔든 위대한 깨달음을 얻었습니다.
        </p>

        <h2 class="article-h2">1. 해골물에서 피어난 '일체유심조(一切唯心造)'</h2>
        <p>
          661년, 원효는 동료 의상대사와 함께 불교의 심오한 진리를 배우기 위해 당나라 유학길에 올랐습니다. 밤중에 심한 비바람을 만나 토굴에서 하룻밤을 묵게 되었는데, 몹시 목이 말랐던 원효는 어둠 속에서 손에 잡힌 바가지의 물을 달게 마시고 단잠에 들었습니다.
        </p>
        <p>
          그러나 아침에 눈을 떠보니 토굴은 오래된 무덤이었고, 자신이 마신 것은 구더기가 끓는 해골에 고인 썩은 빗물이었습니다. 심한 구역질을 하던 원효는 문득 엄청난 진리를 깨달았습니다:
        </p>
        <blockquote class="quote-box">
          "마음이 생겨나면 온갖 법(사물)이 생겨나고, 마음이 사라지면 해골물도 사라진다.<br>
          세상 모든 진리가 내 마음속에 있는데 어찌 다른 나라로 진리를 찾아 떠나겠는가!"
        </blockquote>
        <p>
          원효는 그 길로 유학을 포기하고 신라로 발길을 돌렸습니다. (함께했던 의상대사는 유학길을 계속하여 화엄종의 시조가 되었습니다.)
        </p>

        <h2 class="article-h2">2. 민중 속으로 들어간 파계승의 대중 불교</h2>
        <p>
          깨달음을 얻은 원효는 왕실과 귀족만의 전유물이었던 어려운 교리 불교의 울타리를 과감히 부수었습니다.
        </p>
        <p>
          바가지로 만든 악기인 '무애박'을 두드리며 전국 방방곡곡의 광대, 거지, 노비들을 찾아가 <strong>"나무아미타불"</strong>만 외우면 누구나 극락정토에 갈 수 있다는 '정토종'을 설파했습니다. 또한 서로 다른 불교 종파 간의 다툼을 조화롭게 통합하는 <strong>'화쟁(和諍) 사상'</strong>을 정립했습니다.
        </p>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 핵심 포인트:</strong><br>
          해골물 깨달음 + 일체유심조 + 화쟁사상 + 불교 대중화 ➔ <strong>원효대사!</strong><br>
          <em>(당나라 유학 완주 + 부석사 창건 + 화엄사상 ➔ 의상대사)</em>
        </div>
        """,
        "quiz": {
            "q": "당나라 유학길에 해골물을 마시고 '모든 것은 마음이 지어낸다(일체유심조)'는 깨달음을 얻어 불교 대중화에 앞장선 신라의 승려는 [{A} / {B}]이다.",
            "a": "원효",
            "b": "의상",
            "correct": "A",
            "exp": "해골물 일화와 무애가를 지어 민중 불교를 전파한 인물은 원효대사입니다."
        },
        "faq": [
            {"q": "원효대사의 아들은 누구인가요?", "a": "신라 3대 문장가이자 이두를 집대성한 대학자 '설총'이 바로 원효대사와 요석공주 사이에서 태어난 아들입니다."},
            {"q": "원효대사가 지은 대표적인 저서는?", "a": "불교 종파 간의 갈등을 화해시킨 《십문화쟁론》과 불교 사상의 핵심을 집대성한 《대승기신론소》 등이 있습니다."}
        ]
    },
    {
        "slug": "history-king-sejong-scientific-inventions",
        "category": "역사·문화",
        "category_slug": "category-history.html",
        "category_icon": "🏛️",
        "title": "세종대왕과 장영실의 과학 발명품 - 자격루·측우기·앙부일구의 과학사",
        "description": "노비 출신 장영실을 중용한 세종대왕의 실용 과학주의! 세계 최초의 표준 우량계 측우기, 자동 물시계 자격루, 해시계 앙부일구의 원리.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 역사문화 연구팀",
        "summary": [
            "세종대왕은 신분제를 뛰어넘어 관노 출신 장영실을 등용하여 자주적 과학 문화를 꽃피웠습니다.",
            "측우기는 이탈리아 카스텔리의 우량계보다 200여 년 앞선 세계 최초의 표준 강우량 측정기입니다.",
            "백성들이 시간을 쉽게 읽을 수 있도록 12지신 그림을 새긴 오목 해시계 앙부일구를 보급했습니다."
        ],
        "content_html": """
        <p class="lead-text">
          조선 제4대 임금 세종대왕의 치적은 훈민정음 창제에만 머무르지 않습니다. 농본국가 조선의 백성들이 자연재해를 극복하고 풍년을 누릴 수 있도록 당대 세계 최고 수준의 천문학과 계측 과학 기술을 발전시켰습니다.
        </p>

        <h2 class="article-h2">1. 장영실의 천재성과 세종의 파격 인사</h2>
        <p>
          동래현의 관노(관청의 노비) 출신이었던 <strong>장영실</strong>의 비범한 재능을 알아본 세종대왕은 신하들의 거센 반대를 무릅쓰고 그를 종3품 대호군이라는 고위 관직에 제수했습니다.
        </p>

        <h2 class="article-h2">2. 세종 시대의 대표적인 3대 과학 발명품</h2>
        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>발명품</th>
                <th>과학적 원리 및 특징</th>
                <th>역사적 의의</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>자격루 (1434년)</strong></td>
                <td>물이 차오르면 쇠구슬이 굴러 종과 북을 자동으로 치는 자동 시보 물시계</td>
                <td>인력에 의존하던 시간 측정의 완전 자동화 달성</td>
              </tr>
              <tr>
                <td><strong>측우기 (1441년)</strong></td>
                <td>일정한 규격의 원통에 빗물을 받아 깊이를 측정하는 표준 우량계</td>
                <td><strong>서양보다 200년 앞선</strong> 세계 최초의 전국 강우량 관측망</td>
              </tr>
              <tr>
                <td><strong>앙부일구 (1434년)</strong></td>
                <td>오목한 솥 모양의 해시계로 시각선과 24절기선이 교차 표시됨</td>
                <td>글자를 모르는 백성을 위해 12간지 동물 그림으로 시각 표기</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 외우는 공식:</strong><br>
          자동으로 종을 치는 물시계 ➔ <strong>자격루!</strong><br>
          솥 모양의 공중 해시계 ➔ <strong>앙부일구!</strong><br>
          세계 최초의 빗물 측정 통 ➔ <strong>측우기!</strong>
        </div>
        """,
        "quiz": {
            "q": "조선 세종 대에 장영실 등이 제작한 세계 최초의 표준 강우량 측정 기구는 [{A} / {B}]이다.",
            "a": "측우기",
            "b": "혼천의",
            "correct": "A",
            "exp": "1441년 세종대왕 때 세자(문종)와 장영실 등이 창안한 원통형 빗물 측정 기구는 측우기입니다."
        },
        "faq": [
            {"q": "측우기는 장영실 혼자 만든 것인가요?", "a": "조선왕조실록에 따르면 세종의 맏아들이었던 세자(훗날 문종)가 구리 그릇에 빗물을 재는 아이디어를 먼저 냈고, 이를 장영실 등이 정밀한 국가 표준 기구로 완성했습니다."},
            {"q": "앙부일구는 밤이나 흐린 날에는 어떻게 시간을 알았나요?", "a": "해시계인 앙부일구는 햇빛이 없으면 작동할 수 없으므로, 흐린 날이나 밤에는 물시계인 자격루를 통해 시간을 확인했습니다."}
        ]
    },

    # ==================== 4. 과학·IT (Science & IT) - 5 New (Total 10) ====================
    {
        "slug": "science-jupiter-great-red-spot",
        "category": "과학·IT",
        "category_slug": "category-science.html",
        "category_icon": "🔬",
        "title": "목성의 거대한 크기와 대적점 - 태양계 최대 가스 행성의 신비",
        "description": "지구 1,300개가 들어가는 거대 가스 행성 목성! 350년 넘게 불고 있는 초대형 폭풍 대적점(대적반)과 갈릴레이 4대 위성의 비밀을 탐구합니다.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 과학IT 학술팀",
        "summary": [
            "목성은 태양계 모든 행성의 질량을 합친 것보다 2.5배 무거운 태양계 5번째 행성입니다.",
            "표면에 보이는 거대한 붉은 점 '대적점(Great Red Spot)'은 지구보다 큰 초대형 고기압 폭풍입니다.",
            "갈릴레오 갈릴레이가 발견한 4대 위성(이오, 유로파, 가니메데, 칼리스토)을 거느리고 있습니다."
        ],
        "content_html": """
        <p class="lead-text">
          밤하늘에서 달과 금성 다음으로 밝게 빛나는 목성(Jupiter)은 태양계의 '맏형'이자 행성들의 왕입니다. 수소와 헬륨으로 가득 찬 이 거대한 가스 행성은 지구와는 비교조차 할 수 없는 경이로운 스케일을 자랑합니다.
        </p>

        <h2 class="article-h2">1. 태양계 행성 서열 1위의 위엄</h2>
        <p>
          목성의 부피는 지구의 약 <strong>1,300배</strong>에 달하며, 질량은 지구의 약 318배입니다. 태양계를 돌고 있는 나머지 7개 행성(토성, 천왕성, 해왕성, 지구 등)의 무게를 전부 합쳐도 목성 하나의 40%에 불과합니다.
        </p>
        <p>
          만약 목성의 질량이 지금보다 약 80배 정도 더 무거웠다면, 중심부에서 수소 핵융합 반응이 일어나 태양처럼 스스로 빛을 내는 '항성(별)'이 되었을 것입니다.
        </p>

        <h2 class="article-h2">2. 350년 넘게 회전하는 '대적점(Great Red Spot)'</h2>
        <p>
          목성 남반구 표면에 선명하게 보이는 붉은 타원형 무늬를 <strong>대적점(대적반)</strong>이라고 부릅니다. 이는 단순한 점이 아니라, 시속 400~600km의 맹렬한 바람이 소용돌이치는 <strong>초대형 고기압 폭풍</strong>입니다.
        </p>
        <p>
          대적점의 가로 직경은 약 16,000km로 <strong>지구 하나가 통째로 쏙 들어가고도 남는 크기</strong>입니다. 1665년 카시니가 망원경으로 관측한 이래 350년이 넘도록 한 번도 꺼지지 않고 지속되고 있습니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>갈릴레이 위성</th>
                <th>주요 특징 및 생명체 거주 가능성</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>이오 (Io)</strong></td>
                <td>목성의 조석력으로 인해 수백 개의 활화산이 용암을 뿜는 화산 천체</td>
              </tr>
              <tr>
                <td><strong>유로파 (Europa)</strong></td>
                <td>두꺼운 얼음 지각 아래 <strong>거대한 지하 바다</strong> 존재 (외계 생명체 탐사 1순위)</td>
              </tr>
              <tr>
                <td><strong>가니메데 (Ganymede)</strong></td>
                <td><strong>태양계에서 가장 큰 위성</strong> (수성이나 명왕성보다 큼)</td>
              </tr>
              <tr>
                <td><strong>칼리스토 (Callisto)</strong></td>
                <td>수많은 운석 충돌 구덩이(크레이터)가 보존된 고대 얼음 위성</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 과학 상식 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 핵심 요약:</strong><br>
          태양계에서 가장 거대한 행성 + 지구보다 큰 350년 된 붉은 폭풍 ➔ <strong>목성(대적점)!</strong>
        </div>
        """,
        "quiz": {
            "q": "태양계 행성 중 질량과 부피가 가장 크며, 지구보다 큰 초대형 고기압 폭풍인 '대적점'을 지닌 행성은 [{A} / {B}]이다.",
            "a": "목성",
            "b": "토성",
            "correct": "A",
            "exp": "태양계 최대 행성이자 붉은 대적점을 가진 가스 행성은 목성(Jupiter)입니다. 토성은 거대한 고리로 유명합니다."
        },
        "faq": [
            {"q": "목성 표면에 발을 딛고 서 있을 수 있나요?", "a": "불가능합니다. 목성은 단단한 암석 지표면이 없는 '가스 행성'이므로, 착륙하려 하면 수천 킬로미터 깊이의 고온 고압 수소 대기 속으로 끝없이 추락하게 됩니다."},
            {"q": "목성에도 고리가 있나요?", "a": "네, 토성처럼 화려하지는 않지만 목성 역시 희미한 먼지 입자로 이루어진 미세한 고리를 가지고 있습니다."}
        ]
    },
    {
        "slug": "science-stratosphere-ozone-layer",
        "category": "과학·IT",
        "category_slug": "category-science.html",
        "category_icon": "🔬",
        "title": "성층권과 오존층의 자외선 차단 원리 - 몬트리올 의정서와 오존홀 회복",
        "description": "지상 15~35km 성층권에 위치한 오존(O3)층이 태양의 유해 자외선(UV-C, UV-B)을 흡수하는 화학적 메커니즘과 프레온가스(CFCs) 퇴출 역사.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 과학IT 학술팀",
        "summary": [
            "지구 대기권 중 지상 10~50km 구간인 성층권에 오존(O3)이 집중된 오존층이 존재합니다.",
            "오존층은 피부암과 돌연변이를 일으키는 태양의 치명적인 자외선(UV-C, UV-B)을 99% 차단합니다.",
            "1987년 몬트리올 의정서를 통해 프레온가스(CFCs)를 전 세계적으로 금지하여 환경 협약의 모범이 되었습니다."
        ],
        "content_html": """
        <p class="lead-text">
          지구상에 생명체가 바다를 벗어나 육지로 올라올 수 있었던 결정적인 계기는 무엇이었을까요? 바로 하늘 높이 성층권에 <strong>'오존층(Ozone Layer)'</strong>이라는 천연 자외선 방패가 형성되었기 때문입니다.
        </p>

        <h2 class="article-h2">1. 지구 대기권의 구조와 성층권(Stratosphere)</h2>
        <p>
          지구를 둘러싼 공기층은 고도와 온도 변화에 따라 4개 층으로 구분됩니다:
        </p>
        <ul class="step-list">
          <li><strong>대류권 (0~10km):</strong> 우리가 숨 쉬는 공간이자 비, 눈, 구름 등 기상 현상이 일어나는 층.</li>
          <li><strong>성층권 (10~50km):</strong> 공기가 안정되어 여객기의 항로로 쓰이며, <strong>오존층(20~30km 부근)</strong>이 존재하는 층. 고도가 높아질수록 기온이 상승합니다.</li>
          <li><strong>중간권 (50~80km):</strong> 유성(별똥별)이 타는 층.</li>
          <li><strong>열권 (80km 이상):</strong> 오로라가 발생하며 인공위성이 궤도를 도는 층.</li>
        </ul>

        <h2 class="article-h2">2. 오존(O3)의 자외선 차단 화학 반응</h2>
        <p>
          산소 원자 3개가 결합한 오존 분자는 태양 복사에너지 중 파장이 짧고 에너지가 치명적인 <strong>자외선(UV)</strong>을 흡수하여 산소 분자(O2)와 산소 원자(O)로 분해되었다가 다시 결합하는 순환 과정을 끊임없이 반복합니다:
        </p>
        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>자외선 종류</th>
                <th>파장</th>
                <th>생체 영향 및 오존층 차단율</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>UV-C</strong></td>
                <td>100~280nm</td>
                <td>생명체 세포를 파괴하는 극독성 ➔ <strong>오존층이 100% 완전 흡수</strong></td>
              </tr>
              <tr>
                <td><strong>UV-B</strong></td>
                <td>280~315nm</td>
                <td>피부 화상, 백내장, 피부암 유발 ➔ <strong>오존층이 약 90% 이상 차단</strong></td>
              </tr>
              <tr>
                <td><strong>UV-A</strong></td>
                <td>315~400nm</td>
                <td>피부 노화 촉진 ➔ 오존층을 통과하여 지표면에 대부분 도달</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 인류의 위대한 결단: 몬트리올 의정서</h2>
        <p>
          1980년대 냉장고 냉매와 헤어스프레이로 쓰이던 <strong>프레온가스(염화불화탄소, CFCs)</strong>가 남극 상공의 오존층을 파괴해 거대한 구멍(오존홀)을 냈다는 사실이 밝혀졌습니다.
        </p>
        <p>
          전 세계는 1987년 <strong>'몬트리올 의정서'</strong>를 체결하여 CFCs의 생산과 사용을 전면 금지했습니다. 그 결과 오존홀은 점진적으로 회복되고 있으며, 2060년대에는 1980년대 수준으로 완전 복원될 전망입니다.
        </p>

        <h2 class="article-h2">4. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 외우는 공식:</strong><br>
          비·눈 내리는 곳 ➔ <strong>대류권!</strong><br>
          자외선 막아주는 오존층 있는 곳 ➔ <strong>성층권!</strong>
        </div>
        """,
        "quiz": {
            "q": "태양의 유해 자외선(UV)을 흡수하여 지구 생명체를 보호하는 '오존층'이 위치한 대기권은 [{A} / {B}]이다.",
            "a": "성층권",
            "b": "대류권",
            "correct": "A",
            "exp": "오존층은 지상 약 20~30km 상공인 성층권에 집중적으로 분포하고 있습니다."
        },
        "faq": [
            {"q": "지표면 근처에 생기는 오존도 좋은 것인가요?", "a": "아닙니다. 성층권의 오존은 착한 방패지만, 지표면 근처에서 자동차 매연 등에 의해 발생하는 오존은 눈과 호흡기를 자극하는 유해한 대기오염 물질(오존 경보제 대상)입니다."},
            {"q": "오존 분자 하나는 프레온가스에 얼마나 파괴되나요?", "a": "프레온가스에서 나온 염소(Cl) 원자 1개는 연쇄 반응을 통해 무려 10만 개 이상의 오존 분자를 파괴합니다."}
        ]
    },
    {
        "slug": "science-ring-of-fire-plate-tectonics",
        "category": "과학·IT",
        "category_slug": "category-science.html",
        "category_icon": "🔬",
        "title": "불의 고리와 판구조론 - 전 세계 지진과 화산의 80%가 집중되는 이유",
        "description": "태평양을 둘러싼 말발굽 모양의 환태평양 조산대 '불의 고리'! 대륙판과 해양판이 충돌하고 섭입하며 일어나는 지진과 화산 분화의 원리.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 과학IT 학술팀",
        "summary": [
            "환태평양 조산대(불의 고리)는 태평양 연안을 따라 말발굽 모양으로 뻗어있는 지진·화산대입니다.",
            "전 세계 활화산의 75%와 지진 발생의 약 80~90%가 이 구역에 집중됩니다.",
            "판구조론에 따라 태평양판이 유라시아판, 북미판 등 인접 판 아래로 파고드는 섭입대에서 발생합니다."
        ],
        "content_html": """
        <p class="lead-text">
          일본, 대만, 인도네시아, 칠레 등에서 규모 7.0 이상의 강진이나 화산 폭발 소식이 들릴 때마다 뉴스 헤드라인에 등장하는 용어가 바로 <strong>'불의 고리(Ring of Fire)'</strong>입니다. 왜 유독 이 지역에만 지구의 지각 변동이 집중되는 것일까요?
        </p>

        <h2 class="article-h2">1. 불의 고리(환태평양 조산대)의 위치와 규모</h2>
        <p>
          공식 명칭은 <strong>환태평양 조산대(Circum-Pacific Belt)</strong>로, 태평양 바다의 가장자리를 따라 뉴질랜드, 인도네시아, 필리핀, 일본, 캄차카반도, 알래스카, 미국 서부, 칠레로 이어지는 길이 약 <strong>40,000km</strong>의 말발굽 모양 지대입니다.
        </p>
        <p>
          이 지역에는 450개 이상의 활화산이 밀집해 있으며, 전 세계 지진 에너지의 약 <strong>80% 이상</strong>이 방출되는 지구상에서 가장 지질학적으로 역동적인 구역입니다.
        </p>

        <h2 class="article-h2">2. 판구조론(Plate Tectonics)이 밝힌 메커니즘</h2>
        <p>
          지구의 껍데기(지각)는 하나의 통짜 암석이 아니라, 퍼즐 조각처럼 10여 개의 거대한 암석 덩어리인 <strong>'판(Plate)'</strong>으로 쪼개져 맨틀의 대류를 타고 서서히 움직입니다.
        </p>
        <p>
          불의 고리는 밀도가 높고 무거운 <strong>태평양 해양판</strong>이 상대적으로 가벼운 유라시아 대륙판이나 북아메리카 대륙판과 정면으로 부딪치며 아래로 미끄러져 들어가는 <strong>'섭입대(Subduction Zone)'</strong>에 형성되어 있습니다. 판이 땅속 깊은 곳으로 밀려 들어가면서 엄청난 마찰열과 압력으로 암석이 녹아 마그마가 되고, 응축된 에너지가 단숨에 튕겨 나가며 대지진을 일으키는 것입니다.
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>세계 2대 지진·화산대</th>
                <th>주요 위치</th>
                <th>지진 발생 비율</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>환태평양 조산대 (불의 고리)</strong></td>
                <td>태평양 연안 (일본, 필리핀, 칠레 등)</td>
                <td><strong>전 세계 지진의 약 80%</strong></td>
              </tr>
              <tr>
                <td><strong>알프스-히말라야 조산대</strong></td>
                <td>지중해, 튀르키예, 히말라야, 인도네시아</td>
                <td>전 세계 지진의 약 15%</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 핵심 요약:</strong><br>
          태평양을 빙 둘러 지진·화산이 터지는 말발굽 지대 ➔ <strong>환태평양 조산대(불의 고리)!</strong>
        </div>
        """,
        "quiz": {
            "q": "태평양 연안을 따라 전 세계 지진의 80%와 활화산이 집중되어 있어 '불의 고리'라 불리는 조산대는 [{A} / {B}]이다.",
            "a": "환태평양 조산대",
            "b": "알프스-히말라야 조산대",
            "correct": "A",
            "exp": "태평양을 둘러싼 말발굽 모양의 환태평양 조산대를 일명 '불의 고리(Ring of Fire)'라고 부릅니다."
        },
        "faq": [
            {"q": "한국은 불의 고리에 속해 있나요?", "a": "한국은 유라시아판의 안쪽에 위치해 있어 불의 고리(판 경계)에서 약간 비껴나 있습니다. 하지만 일본 열도가 인접해 있어 간접적인 여진과 지진해일(쓰나미)의 영향을 받습니다."},
            {"q": "역대 가장 강력했던 지진은 어디서 일어났나요?", "a": "1960년 불의 고리에 속한 칠레 남부에서 발생한 발디비아 대지진(규모 9.5)으로, 인류 관측 사상 역대 최대 규모의 지진이었습니다."}
        ]
    },
    {
        "slug": "science-ram-vs-cpu-memory",
        "category": "과학·IT",
        "category_slug": "category-science.html",
        "category_icon": "🔬",
        "title": "CPU와 RAM의 차이와 컴퓨터 연산 원리 - 두뇌(연산)와 작업대(주기억장치)",
        "description": "컴퓨터를 살 때 왜 CPU 속도와 RAM 용량을 따질까? 두뇌에 해당하는 중앙처리장치와 책상 크기에 해당하는 주기억장치의 역할 분담 완벽 정리.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 과학IT 학술팀",
        "summary": [
            "CPU(중앙처리장치)는 명령어 해석과 연산을 담당하는 컴퓨터의 핵심 '두뇌'입니다.",
            "RAM(주기억장치)은 CPU가 작업 중인 데이터를 올려놓는 고속 '작업대(책상)'입니다.",
            "SSD/HDD(보조기억장치)는 컴퓨터가 꺼져도 파일이 보존되는 영구 '책장(서랍장)'에 비유됩니다."
        ],
        "content_html": """
        <p class="lead-text">
          새 노트북이나 스마트폰을 구매할 때 사양표에 적힌 <em>"인텔 i7 CPU, 16GB RAM, 512GB SSD"</em> 같은 문구를 보며 고개를 갸우뚱했던 경험이 누구나 있을 것입니다. 컴퓨터 하드웨어의 3대 핵심 부품은 각각 어떤 역할을 할까요?
        </p>

        <h2 class="article-h2">1. 사무실 비유로 단숨에 끝내는 3대 부품</h2>
        <p>
          컴퓨터의 데이터 처리 구조는 회사원의 업무 공간과 놀랍도록 똑같습니다:
        </p>
        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>부품명</th>
                <th>비유</th>
                <th>핵심 기능 및 특징</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>CPU (중앙처리장치)</strong></td>
                <td><strong>일하는 사람의 두뇌</strong></td>
                <td>수학 계산, 논리 판단, 프로그램 실행 명령 총괄</td>
              </tr>
              <tr>
                <td><strong>RAM (주기억장치)</strong></td>
                <td><strong>작업 책상의 넓이</strong></td>
                <td>현재 실행 중인 앱을 올려놓는 고속 임시 메모리 (전원 끄면 삭제)</td>
              </tr>
              <tr>
                <td><strong>SSD / HDD (보조기억장치)</strong></td>
                <td><strong>자료 보관 서랍장</strong></td>
                <td>사진, 영화, 문서를 영구 보관 (속도는 느리지만 용량 큼)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 왜 RAM이 크면 컴퓨터가 빨라질까?</h2>
        <p>
          작업 책상(RAM)이 좁으면(예: 4GB), 책장(SSD)에서 서류를 하나 꺼내 펼쳤을 때 다른 서류를 둘 공간이 없어 다시 서랍에 넣었다 뺐다를 반복해야 합니다. 이로 인해 컴퓨터가 버벅대는 현상(병목 현상)이 생깁니다.
        </p>
        <p>
          하지만 책상이 넓으면(예: 16GB, 32GB) 웹 브라우저 탭 30개를 띄우고, 포토샵을 켜고, 고사양 게임을 동시에 돌려도 모든 작업을 책상 위에 바로 올려두고 즉시 처리할 수 있어 쾌적한 멀티태스킹이 가능해집니다.
        </p>

        <h2 class="article-h2">3. 3초 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 외우는 공식:</strong><br>
          CPU ➔ <strong>머리가 얼마나 똑똑한가 (두뇌)</strong><br>
          RAM ➔ <strong>책상이 얼마나 넓은가 (작업대)</strong><br>
          SSD ➔ <strong>책장이 얼마나 큰가 (창고)</strong>
        </div>
        """,
        "quiz": {
            "q": "컴퓨터에서 실행 중인 프로그램의 데이터를 임시로 보관하여 CPU가 빠르게 접근할 수 있도록 돕는 주기억장치는 [{A} / {B}]이다.",
            "a": "RAM",
            "b": "CPU",
            "correct": "A",
            "exp": "주기억장치는 RAM(Random Access Memory)이며, 연산과 명령 제어를 담당하는 두뇌는 CPU입니다."
        },
        "faq": [
            {"q": "RAM과 SSD의 가장 큰 기술적 차이는 무엇인가요?", "a": "RAM은 전원이 꺼지면 저장된 내용이 모두 날아가는 '휘발성 메모리'인 반면, SSD는 전원이 꺼져도 데이터가 영구 보존되는 '비휘발성 메모리'입니다."},
            {"q": "게임 속도를 올리려면 CPU와 RAM 중 무엇을 업그레이드해야 하나요?", "a": "게임의 연산과 그래픽 처리를 위해선 CPU(및 그래픽카드 GPU)의 성능이 우선이지만, 최소 권장 사양(보통 16GB) 이상의 RAM이 뒷받침되어야 렉 없이 부드럽게 구동됩니다."}
        ]
    },
    {
        "slug": "science-turing-test-artificial-intelligence",
        "category": "과학·IT",
        "category_slug": "category-science.html",
        "category_icon": "🔬",
        "title": "앨런 튜링과 튜링 테스트 - 기계가 인간처럼 생각할 수 있는가에 대한 시험",
        "description": "1950년 컴퓨터 과학의 아버지 앨런 튜링이 제안한 모방 게임! 인간 판정관이 대화만으로 인간과 기계를 구분하지 못할 때 지능이 있다고 보는 원리.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 과학IT 학술팀",
        "summary": [
            "컴퓨터 과학의 개척자 앨런 튜링이 '기계도 생각할 수 있는가?'라는 질문에 답하기 위해 고안했습니다.",
            "심사위원이 텍스트 대화만으로 컴퓨터와 진짜 사람을 구분하지 못하면 통과하는 모방 게임입니다.",
            "최근 ChatGPT, 클로드 등 거대언어모델(LLM)이 등장하면서 튜링 테스트를 뛰어넘는 새로운 지능 평가가 요구되고 있습니다."
        ],
        "content_html": """
        <p class="lead-text">
          오늘날 우리는 ChatGPT와 인공지능(AI)이 시를 짓고 코딩을 하며 사람과 자연스럽게 농담을 주고받는 시대를 살아가고 있습니다. 컴퓨터가 막 태동하던 1950년, <em>"기계도 생각할 수 있을까?"</em>라는 파격적인 질문을 던지고 인공지능의 기준을 세운 인물이 바로 천재 수학자 <strong>앨런 튜링(Alan Turing)</strong>입니다.
        </p>

        <h2 class="article-h2">1. 튜링 테스트(Turing Test, 이미테이션 게임)의 원리</h2>
        <p>
          앨런 튜링은 "생각이란 무엇인가?"라는 복잡하고 추상적인 철학적 논쟁 대신, 실용적인 <strong>행동주의적 판별법</strong>을 제시했습니다:
        </p>
        <ol class="step-list">
          <li>인간 심사위원(C)은 분리된 다른 방에 있는 두 대상(A, B)과 키보드 및 화면(텍스트)으로만 자유롭게 대화를 나눕니다.</li>
          <li>A와 B 중 한쪽은 <strong>진짜 인간</strong>이고, 다른 한쪽은 <strong>컴퓨터 인공지능</strong>입니다.</li>
          <li>일정 시간 대화를 나눈 뒤, 심사위원이 어느 쪽이 인간이고 어느 쪽이 컴퓨터인지 <strong>구별하지 못하거나 컴퓨터를 인간으로 착각한다면</strong>, 그 컴퓨터는 '지능이 있다(생각한다)'고 인정합니다.</li>
        </ol>

        <h2 class="article-h2">2. 튜링 테스트의 의의와 한계</h2>
        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>주요 내용</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>역사적 의의</strong></td>
                <td>기계 지능(AI)을 객관적이고 실험 가능한 관찰 행동으로 규정</td>
              </tr>
              <tr>
                <td><strong>철학적 비판 (중국어 방)</strong></td>
                <td>규칙표에 따라 대답을 흉내 낼 뿐(모방), 기계가 <strong>실제 의미를 '이해'하는 것은 아니라는 반론</strong></td>
              </tr>
              <tr>
                <td><strong>현대적 위상</strong></td>
                <td>최신 LLM(생성형 AI)이 튜링 테스트를 쉽게 통과함에 따라, 진정한 인공일반지능(AGI) 평가를 위한 새 기준 필요</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 과학 상식 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 핵심 포인트:</strong><br>
          "대화해 보고 사람인지 기계인지 구별 못 하면 합격!"<br>
          ➔ <strong>튜링 테스트 (고안자: 앨런 튜링)</strong>
        </div>
        """,
        "quiz": {
            "q": "기계가 인간과 구별할 수 없을 정도로 자연스럽게 대화할 수 있는지를 평가하여 지능의 유무를 판별하는 시험은 [{A} / {B}]이다.",
            "a": "튜링 테스트",
            "b": "블라인드 테스트",
            "correct": "A",
            "exp": "앨런 튜링이 1950년에 고안한 인공지능 판별 실험은 튜링 테스트(Turing Test)입니다."
        },
        "faq": [
            {"q": "앨런 튜링의 삶을 다룬 유명한 영화는?", "a": "베네딕트 컴버배치 주연의 영화 《이미테이션 게임(The Imitation Game)》으로, 제2차 세계대전 당시 독일군의 암호기 에니그마를 해독한 튜링의 활약을 그렸습니다."},
            {"q": "스마트폰 캡차(CAPTCHA)도 튜링 테스트와 관련이 있나요?", "a": "네, 맞습니다. 캡차의 정식 명칭은 '사람과 컴퓨터를 구별하기 위한 완전 자동화된 공공 튜링 테스트(Completely Automated Public Turing test)'로, 거꾸로 컴퓨터가 사람을 판별하는 '역 튜링 테스트'입니다."}
        ]
    },

    # ==================== 5. 생활·상식 (Life & Common Sense) - 5 New (Total 10) ====================
    {
        "slug": "life-smartphone-battery-charge-tips",
        "category": "생활·상식",
        "category_slug": "category-life.html",
        "category_icon": "☕",
        "title": "스마트폰 배터리 수명 늘리는 20-80 충전법 - 리튬이온 배터리 관리 상식",
        "description": "100% 완충이나 0% 방전이 왜 배터리에 해로울까? 리튬이온 배터리의 특성과 고온 노출 방지, 배터리 수명을 2배 늘리는 실전 관리 꿀팁.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 생활상식 검수팀",
        "summary": [
            "현대 스마트폰에 쓰이는 리튬이온 배터리는 '메모리 효과'가 없어 수시로 충전해도 무방합니다.",
            "완전 방전(0%)이나 100% 장시간 완충 상태 유지는 배터리 내부 전극에 스트레스를 줍니다.",
            "배터리 잔량을 20%~80% 사이로 유지하는 것이 수명을 가장 길게 연장하는 비결입니다."
        ],
        "content_html": """
        <p class="lead-text">
          스마트폰을 구매한 지 1년 반만 지나면 배터리가 반나절 만에 광탈하는 현상을 누구나 겪어보셨을 것입니다. 과거 휴대폰 시절의 잘못된 충전 상식(완전 방전 후 완전 충전)을 아직도 고수하고 있다면, 지금 당신의 스마트폰 배터리는 빠르게 노화되고 있습니다.
        </p>

        <h2 class="article-h2">1. 리튬이온 배터리의 골든 룰: 20-80 법칙</h2>
        <p>
          스마트폰, 무선 이어폰, 노트북에 탑재되는 <strong>리튬이온 배터리</strong>는 양극과 음극 사이를 리튬 이온이 오가며 충·방전이 이루어집니다.
        </p>
        <p>
          배터리 전압이 너무 낮거나(0% 방전) 너무 높은 상태(100% 과충전)가 지속되면 전극 물질이 영구적으로 손상되어 충전 용량이 급감합니다. 따라서 배터리 잔량이 <strong>20% 아래로 떨어지기 전에 충전을 시작하고, 80~85% 수준에서 충전을 마치는 것</strong>이 배터리 노화를 막는 최적의 관리법입니다. (최신 갤럭시와 아이폰의 '배터리 보호 모드' 역시 80% 또는 85%에서 충전을 멈추도록 설계되어 있습니다.)
        </p>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>좋은 충전 습관 (수명 연장)</th>
                <th>나쁜 충전 습관 (수명 단축)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>충전 타이밍</strong></td>
                <td>잔량 20~80% 구간에서 <strong>수시로 충전</strong></td>
                <td>0% 꺼질 때까지 쓰다가 밤새 100% 방치</td>
              </tr>
              <tr>
                <td><strong>온도 관리</strong></td>
                <td>서늘한 상온에서 케이스 벗겨서 충전</td>
                <td><strong>충전기 꽂은 채 고사양 게임</strong> (치명적 고열 발생)</td>
              </tr>
              <tr>
                <td><strong>충전기 선택</strong></td>
                <td>정품 또는 공식 안전 규격 인증 충전기</td>
                <td>출처 불명의 초저가 미인증 고속 충전기</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 배터리의 가장 큰 적은 '열(Heat)'</h2>
        <p>
          배터리 수명을 갉아먹는 최악의 요인은 <strong>고온</strong>입니다. 자동차 대시보드나 전기장판 위에 스마트폰을 둔 채 충전하거나, 고속 충전 중 발열이 심한 상태에서 게임을 플레이하면 배터리 내부 온도가 40도를 넘어가며 화학적 열화가 가속됩니다.
        </p>

        <h2 class="article-h2">3. 3초 생활 상식 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 외우는 배터리 상식:</strong><br>
          "바닥(0%)까지 쓰지 말고, 꽉(100%) 채워 방치하지 말자!"<br>
          ➔ <strong>배터리는 20~80% 사이 수시 충전이 정답!</strong>
        </div>
        """,
        "quiz": {
            "q": "스마트폰 리튬이온 배터리의 수명을 가장 오래 유지하기에 이상적인 일상 배터리 잔량 구간은 [{A} / {B}]이다.",
            "a": "20% ~ 80%",
            "b": "0% ~ 100%",
            "correct": "A",
            "exp": "완전 방전과 과충전을 피해 20%에서 80% 사이로 수시 충전하는 것이 리튬이온 배터리의 수명을 최대로 보존하는 방법입니다."
        },
        "faq": [
            {"q": "밤새 충전기에 꽂아두면 배터리가 폭발하나요?", "a": "최신 스마트폰에는 과충전 방지 스마트 회로가 탑재되어 있어 폭발하지는 않습니다. 다만 100% 고전압 상태가 장시간 유지되는 것 자체가 배터리 수명에는 부정적 영향을 줍니다."},
            {"q": "과거 배터리처럼 '완전 방전 후 완충'해야 기억 효과가 없나요?", "a": "그것은 과거 니켈-카드뮴 배터리 시절의 이야기입니다. 현대의 리튬이온 배터리는 메모리 효과가 아예 없으므로 완전 방전시키면 오히려 수명이 급격히 줄어듭니다."}
        ]
    },
    {
        "slug": "life-fine-dust-kf94-mask",
        "category": "생활·상식",
        "category_slug": "category-life.html",
        "category_icon": "☕",
        "title": "미세먼지와 초미세먼지의 차이 - PM10과 PM2.5 및 올바른 KF94 착용법",
        "description": "머리카락 굵기보다 작은 미세먼지(PM10)와 폐포까지 침투하는 초미세먼지(PM2.5)의 유해성! KF80, KF94, KF99 마스크 등급의 의미와 밀착 착용법.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 생활상식 검수팀",
        "summary": [
            "미세먼지(PM10)는 지름 10㎛ 이하, 초미세먼지(PM2.5)는 지름 2.5㎛ 이하의 입자입니다.",
            "초미세먼지는 코털이나 기관지에서 걸러지지 않고 폐포와 혈관 속으로 직접 침투합니다.",
            "KF94는 평균 0.4㎛ 크기의 미세 입자를 94% 이상 차단하며, 코편 밀착이 핵심입니다."
        ],
        "content_html": """
        <p class="lead-text">
          봄철 황사와 겨울철 스모그가 찾아오면 일기예보에서 가장 먼저 확인하는 수치가 바로 '미세먼지'와 '초미세먼지' 농도입니다. 눈에 보이지도 않는 이 작은 먼지들은 우리 몸에 어떤 영향을 미치며, 마스크의 'KF' 숫자는 무엇을 의미할까요?
        </p>

        <h2 class="article-h2">1. 미세먼지(PM10) vs 초미세먼지(PM2.5) 크기 비교</h2>
        <p>
          미세먼지 단위인 <strong>PM(Particulate Matter)</strong>은 공기 중 먼지 입자의 지름을 뜻합니다:
        </p>
        <ul class="step-list">
          <li><strong>사람 머리카락:</strong> 지름 약 50~70㎛ (마이크로미터)</li>
          <li><strong>미세먼지 (PM10):</strong> 지름 10㎛ 이하 (머리카락 굵기의 1/7 수준). 기관지 점막과 코털에서 어느 정도 걸러집니다.</li>
          <li><strong>초미세먼지 (PM2.5):</strong> 지름 2.5㎛ 이하 (머리카락 굵기의 1/30 수준). 너무 작아 코나 기관지에서 걸러지지 않고 <strong>폐포(허파꽈리) 깊숙이 침투하여 혈관을 타고 온몸으로 순환</strong>하며 심혈관 질환을 유발합니다. (WHO 1군 발암물질 지정)</li>
        </ul>

        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>마스크 등급</th>
                <th>입자 차단율</th>
                <th>호흡 편의성 및 용도</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>KF80</strong></td>
                <td>평균 0.6㎛ 미세 입자 <strong>80% 이상 차단</strong></td>
                <td>숨쉬기가 비교적 편안하며 황사·미세먼지 방어용</td>
              </tr>
              <tr>
                <td><strong>KF94</strong></td>
                <td>평균 0.4㎛ 미세 입자 <strong>94% 이상 차단</strong></td>
                <td>초미세먼지 및 감염병 비말(침방울) 방역 차단</td>
              </tr>
              <tr>
                <td><strong>KF99</strong></td>
                <td>평균 0.4㎛ 미세 입자 <strong>99% 이상 차단</strong></td>
                <td>차단력 최고 수준이나 호흡 저항이 커 일상용으로는 답답함</td>
              </tr>
              <tr>
                <td><strong>일반 비말/면마스크</strong></td>
                <td>침방울 차단 가능</td>
                <td><strong>미세먼지 정전기 필터가 없어 미세먼지 차단 불가</strong></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">2. 3초 올바른 마스크 착용법</h2>
        <div class="tip-box-article">
          <strong>💡 틈새 방지 3초 수칙:</strong><br>
          1. 코 지지대(와이어)를 콧등에 대고 꾹 눌러 틈을 없앤다.<br>
          2. 숨을 들이마셨을 때 마스크가 안쪽으로 오므라드는지 확인한다.<br>
          <em>(코 옆으로 바람이 새면 아무리 KF94라도 차단 효과가 절반 이하로 떨어집니다!)</em>
        </div>
        """,
        "quiz": {
            "q": "입자 지름이 2.5㎛ 이하로 매우 작아 코털에서 걸러지지 않고 폐포 깊숙이 직접 침투하는 위험 먼지는 [{A} / {B}]이다.",
            "a": "초미세먼지",
            "b": "황사",
            "correct": "A",
            "exp": "지름 2.5㎛ 이하의 극미세 먼지를 초미세먼지(PM2.5)라고 하며 1군 발암물질로 분류됩니다."
        },
        "faq": [
            {"q": "KF94 마스크를 빨아서 재사용해도 되나요?", "a": "절대 안 됩니다. 보건용 마스크는 정전기 필터 원리로 미세먼지를 흡착하는데, 물에 닿거나 세탁하면 정전기 필터가 파괴되어 차단율이 50% 이하로 급감합니다."},
            {"q": "KF는 무슨 뜻인가요?", "a": "'Korea Filter'의 약자로, 한국 식품의약품안전처가 보건용 마스크의 미세 입자 차단 성능을 검증하여 부여하는 공식 인증 마크입니다."}
        ]
    },
    {
        "slug": "life-antibiotics-completion-rule",
        "category": "생활·상식",
        "category_slug": "category-life.html",
        "category_icon": "☕",
        "title": "항생제는 증상이 나아져도 끝까지 복용해야 할까? - 내성균 발생의 위험성",
        "description": "열이 내렸다고 항생제 복용을 중단하면 왜 위험할까? 살아남은 세균이 돌연변이를 일으켜 슈퍼박테리아가 되는 과정과 올바른 처방 준수 원칙.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 생활상식 검수팀",
        "summary": [
            "항생제는 바이러스가 아닌 '세균(박테리아)'에 의한 감염증을 치료하는 약입니다.",
            "증상이 호전되었다고 복용을 조기 중단하면 완전히 사멸하지 않은 세균이 내성을 획득합니다.",
            "내성균(슈퍼박테리아)이 번식하면 동일한 항생제로 더 이상 치료되지 않는 위험에 처합니다."
        ],
        "content_html": """
        <p class="lead-text">
          감기나 염증으로 병원에서 처방받은 약을 먹다가, 이틀 정도 지나 열이 내리고 통증이 사라지면 <em>"약 많이 먹어서 좋을 것 없지"</em> 하며 스스로 복용을 중단한 경험이 있으신가요? 하지만 처방약에 <strong>'항생제'</strong>가 포함되어 있다면, 이는 매우 위험천만한 행동입니다.
        </p>

        <h2 class="article-h2">1. 항생제(Antibiotics)의 작동 방식</h2>
        <p>
          항생제는 인체 세포는 공격하지 않고, 침투한 <strong>세균(박테리아)의 세포벽이나 단백질 합성을 차단하여 사멸시키는 약물</strong>입니다.
        </p>
        <p>
          복용 후 하루이틀이 지나면 몸속 세균의 90% 이상이 죽어 증상이 눈에 띄게 호전됩니다. 하지만 가장 독하고 저항력이 강한 <strong>나머지 5~10%의 세균</strong>은 아직 체내에 살아남아 있습니다.
        </p>

        <h2 class="article-h2">2. 임의 중단이 불러오는 '슈퍼박테리아'의 비극</h2>
        <p>
          이때 약 복용을 중단해 버리면, 간신히 살아남은 끈질긴 세균들이 약물의 작용 기전을 학습하여 <strong>유전자 돌연변이(내성)</strong>를 일으킵니다.
        </p>
        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>구분</th>
                <th>처방 일수 끝까지 완복</th>
                <th>증상 호전 후 조기 임의 중단</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>세균 사멸도</strong></td>
                <td>약한 균부터 강한 균까지 <strong>100% 완전 박멸</strong></td>
                <td>강한 균이 살아남아 다시 증식</td>
              </tr>
              <tr>
                <td><strong>재발 여부</strong></td>
                <td>완치 및 감염 종결</td>
                <td>며칠 뒤 더 강한 증상으로 <strong>재발 위험</strong></td>
              </tr>
              <tr>
                <td><strong>항생제 내성</strong></td>
                <td>내성균 발생 억제</td>
                <td><strong>기존 항생제가 듣지 않는 내성균 획득</strong></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 건강 상식 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 기억하는 약 복용 원칙:</strong><br>
          진통제나 해열제는 증상 완화 시 끊어도 되지만,<br>
          <strong>항생제는 증상이 나아도 의사가 처방한 일수(3일/5일/7일)를 반드시 끝까지 다 먹는다!</strong>
        </div>
        """,
        "quiz": {
            "q": "병원에서 처방받은 항생제는 복용 후 이틀 만에 열이 내리고 증상이 사라져도 처방 일수를 끝까지 복용해야 하는 주된 이유는 [{A} / {B}] 때문이다.",
            "a": "세균의 항생제 내성 발생을 방지하기",
            "b": "약효를 천천히 낮추기",
            "correct": "A",
            "exp": "항생제를 조기 중단하면 살아남은 잔여 세균이 돌연변이를 일으켜 해당 항생제에 내성을 갖는 슈퍼박테리아로 진화하기 때문입니다."
        },
        "faq": [
            {"q": "일반 감기에도 항생제를 먹어야 하나요?", "a": "아닙니다. 일반 감기는 80~90%가 '바이러스'에 의해 발생하므로 세균을 죽이는 항생제는 효과가 없습니다. 2차 세균 감염(부비동염, 중이염, 세균성 폐렴 등)이 동반될 때만 전문의 판단하에 항생제를 씁니다."},
            {"q": "남은 항생제를 다음에 아플 때 보관해 뒀다 먹어도 되나요?", "a": "절대 안 됩니다. 질환마다 원인균과 필요한 항생제 계열이 다르며, 임의 복용은 내성균만 키우는 지름길입니다."}
        ]
    },
    {
        "slug": "life-burn-first-aid-cooling",
        "category": "생활·상식",
        "category_slug": "category-life.html",
        "category_icon": "☕",
        "title": "화상 응급처치 시 얼음 대신 흐르는 미온수를 써야 하는 이유",
        "description": "뜨거운 기름이나 냄비에 데었을 때 얼음을 대면 피부 조직이 괴사할 수 있다? 화상 1도·2도 구분법과 15분간 흐르는 물로 식히는 올바른 대처법.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 생활상식 검수팀",
        "summary": [
            "화상을 입었을 때 얼음을 직접 대면 혈관이 급격히 수축하여 피부 조직 괴사(동상)를 유발합니다.",
            "가장 올바른 응급처치는 10~20도 정도의 흐르는 수돗물로 15~20분간 환부 열기를 식히는 것입니다.",
            "물집(수포)은 감염을 막아주는 천연 보호막이므로 절대로 일부러 터뜨리면 안 됩니다."
        ],
        "content_html": """
        <p class="lead-text">
          요리를 하다가 뜨거운 기름이 튀거나 뜨거운 냄비를 무심코 만져 화상을 입었을 때, 많은 분이 냉동실에서 얼음을 꺼내 상처 부위에 직접 문지르곤 합니다. 하지만 이는 화상 입은 피부를 두 번 죽이는 매우 위험한 잘못된 민간요법입니다.
        </p>

        <h2 class="article-h2">1. 얼음이나 얼음물이 화상에 해로운 의학적 이유</h2>
        <p>
          뜨거운 열에 노출된 피부 세포는 심한 자극을 받아 손상된 상태입니다. 여기에 영하의 얼음을 직접 대면 피부 표면의 모세혈관이 급격하게 수축하면서 혈액 순환이 차단됩니다.
        </p>
        <p>
          그 결과 화상으로 약해진 피부 조직에 <strong>2차 손상(동상 및 조직 괴사)</strong>이 발생하여 상처가 더욱 깊어지고 심각한 흉터가 남게 됩니다. 또한 감염 위험이 큰 소주, 된장, 치약을 바르는 행위 역시 절대로 금기시해야 합니다.
        </p>

        <h2 class="article-h2">2. 화상 응급처치 표준 가이드라인</h2>
        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>단계</th>
                <th>올바른 대처 요령</th>
                <th>절대 금기 사항</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1단계: 열기 식히기</strong></td>
                <td><strong>10~20℃의 흐르는 미온수</strong>로 15~20분간 지속 냉각</td>
                <td>얼음 직접 접촉, 알코올 붓기 금지</td>
              </tr>
              <tr>
                <td><strong>2단계: 장신구 제거</strong></td>
                <td>환부가 부어오르기 전에 반지, 시계, 팔찌 즉시 제거</td>
                <td>피부에 달라붙은 옷을 강제로 뜯어내기 금지</td>
              </tr>
              <tr>
                <td><strong>3단계: 수포 보호</strong></td>
                <td>생성된 물집은 터뜨리지 말고 깨끗한 거즈로 보호</td>
                <td>바늘로 물집 터뜨리기 금지 (세균 감염 주원인)</td>
              </tr>
              <tr>
                <td><strong>4단계: 병원 이송</strong></td>
                <td>물집이 잡히거나 손바닥 이상 넓은 화상은 전문병원 방문</td>
                <td>연고나 기름을 바른 채 병원 방문 금지</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. 3초 응급처치 암기 팁</h2>
        <div class="tip-box-article">
          <strong>💡 화상 응급처치 골든 룰:</strong><br>
          얼음 X, 된장 X, 소주 X!<br>
          ➔ <strong>흐르는 수돗물에 15분간 열기 빼기!</strong>
        </div>
        """,
        "quiz": {
            "q": "뜨거운 물이나 냄비에 화상을 입었을 때 가장 올바르고 안전한 응급처치 행동은 [{A} / {B}]이다.",
            "a": "흐르는 미온수에 15분간 열기 식히기",
            "b": "얼음을 상처에 직접 문지르기",
            "correct": "A",
            "exp": "얼음을 직접 대면 모세혈관 수축으로 인한 피부 괴사 위험이 있으므로, 10~20도의 흐르는 물에 15분간 열기를 식혀야 합니다."
        },
        "faq": [
            {"q": "화상 연고는 언제 발라야 하나요?", "a": "물로 열기를 충분히(15~20분) 식힌 후, 가벼운 1도 화상(물집 없이 붉기만 한 상태)에 발라주는 것이 좋습니다. 물집이 잡힌 2도 화상은 연고를 바르지 말고 병원 처치를 받아야 합니다."},
            {"q": "물집이 실수로 터졌을 때는 어떻게 하나요?", "a": "소독된 거즈로 진물을 살짝 닦아낸 뒤, 껍질을 억지로 떼어내지 말고 항생제 연고를 바른 후 폼 드레싱(메디폼 등)을 붙여 감염을 예방해야 합니다."}
        ]
    },
    {
        "slug": "life-traffic-roundabout-right-of-way",
        "category": "생활·상식",
        "category_slug": "category-life.html",
        "category_icon": "☕",
        "title": "회전교차로 올바른 통행법 - 회전 차량 우선과 깜빡이 작동 원칙",
        "description": "진입 차량과 이미 돌고 있는 차량 중 누가 우선일까? 회전교차로 3대 안전 수칙(회전차량 우선, 진입 시 좌회전 깜빡이, 진출 시 우회전 깜빡이) 총정리.",
        "read_time": "3분",
        "date": "2026-10-15",
        "author": "딱1분 생활상식 검수팀",
        "summary": [
            "회전교차로에서는 이미 원 안을 돌고 있는 '회전 차량'이 100% 통행 우선권을 갖습니다.",
            "진입하려는 차량은 서행하며 정지선에 멈춰 서서 회전 차량이 지나갈 때까지 양보해야 합니다.",
            "진입할 때는 좌회전 깜빡이(방향지시등), 빠져나갈 때는 우회전 깜빡이를 켜는 것이 도로교통법 의무입니다."
        ],
        "content_html": """
        <p class="lead-text">
          교통 흐름을 원활하게 하고 신호 대기 시간을 줄이기 위해 전국의 교차로가 <strong>'회전교차로(Roundabout)'</strong>로 빠르게 바뀌고 있습니다. 하지만 정작 통행 우선권과 깜빡이 작동법을 제대로 아는 운전자는 의외로 많지 않아 접촉 사고가 빈번하게 발생합니다.
        </p>

        <h2 class="article-h2">1. 절대 법칙: 회전 차량이 무조건 왕이다!</h2>
        <p>
          회전교차로 통행의 제1원칙은 <strong>'회전 차량 우선, 진입 차량 양보'</strong>입니다.
        </p>
        <p>
          교차로 안에서 이미 돌고 있는 차량의 주행을 방해해서는 안 되며, 교차로에 진입하려는 차량은 진입 직전 정지선에 <strong>일시 정지하거나 서행</strong>하며 회전 중인 차가 다 지나갈 때까지 기다린 후 진입해야 합니다. (진입 차량이 무리하게 끼어들다 사고가 나면 진입 차량 과실이 70~80% 이상 책정됩니다.)
        </p>

        <h2 class="article-h2">2. 방향지시등(깜빡이) 점등의 2단계 원칙</h2>
        <div class="compare-table-wrapper">
          <table class="compare-table">
            <thead>
              <tr>
                <th>상황</th>
                <th>점등 방향</th>
                <th>이유</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>교차로에 진입할 때</strong></td>
                <td><span class="correct-text">좌측(←) 방향지시등</span></td>
                <td>원 안을 돌고 있는 차량들에게 "내가 합류한다"는 신호 전달</td>
              </tr>
              <tr>
                <td><strong>교차로에서 빠져나갈 때</strong></td>
                <td><span class="correct-text">우측(→) 방향지시등</span></td>
                <td>뒤따르는 회전 차량과 진입 대기 차량에게 "내가 나간다"는 퇴출 예고</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 class="article-h2">3. '로터리'와 '회전교차로'는 완전히 다르다!</h2>
        <p>
          과거의 <strong>'로터리(Rotary)'</strong>는 진입 차량이 우선이었고 차량들이 고속으로 진입하여 사고가 잦았습니다. 이를 개선하여 원 안의 회전 차량에 우선권을 주고 진입 속도를 30km/h 이하로 낮추도록 설계한 현대적 교통 시스템이 바로 <strong>'회전교차로(Roundabout)'</strong>입니다.
        </p>

        <h2 class="article-h2">4. 3초 운전 상식 팁</h2>
        <div class="tip-box-article">
          <strong>💡 3초 만에 외우는 공식:</strong><br>
          "돌고 있는 차가 먼저 지나가고 나서 들어간다!"<br>
          ➔ <strong>들어갈 땐 좌측 깜빡이(←), 나갈 땐 우측 깜빡이(→)!</strong>
        </div>
        """,
        "quiz": {
            "q": "회전교차로를 통행할 때 통행 우선권을 갖는 차량은 [{A} / {B}]이다.",
            "a": "이미 교차로 안을 돌고 있는 회전 차량",
            "b": "교차로에 먼저 진입하려는 진입 차량",
            "correct": "A",
            "exp": "도로교통법상 회전교차로는 이미 회전 중인 차량에 통행 우선권이 있으며, 진입하려는 차량은 양보해야 합니다."
        },
        "faq": [
            {"q": "회전교차로에서 깜빡이를 켜지 않으면 범칙금이 부과되나요?", "a": "도로교통법 제38조(차의 신호) 위반에 해당하여 승용차 기준 3만 원의 범칙금이 부과될 수 있습니다."},
            {"q": "회전교차로 내부의 흰색 화살표는 어느 방향으로 돌아야 하나요?", "a": "대한민국의 모든 회전교차로는 중앙 교통섬을 중심으로 '반시계 방향'으로 회전해야 하며, 시계 방향 역주행은 대형 사고로 이어지는 중과실입니다."}
        ]
    }
]
