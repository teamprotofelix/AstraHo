# ASTRA — The World Tree · Visual Edition 2

**하나의 세계수, 여섯 개의 우주.** 세계수의 여섯 개 열매와 고해상도 갤러리 카드로 아스트라호 관련 사이트를 연결하는 **순수 정적 GitHub Pages 사이트**입니다.

- 배포 저장소: https://github.com/teamprotofelix/AstraHo
- 사이트 DNS: `astra.moip.ai.kr`
- 프레임워크·외부 CDN·계정·API 키·쿠키 없이 작동합니다.
- **이 프로젝트는 ZIP 파일만 제공하며 실제 GitHub push, DNS 수정, 공개 배포는 수행하지 않았습니다.**

## 배포: 5단계

1. `ASTRA_World_Tree_V2_Deploy.zip`을 **압축 해제**합니다. `index.html`, `assets/`, `styles.css`, `app.js`, `.nojekyll`, `CNAME` 등이 **압축의 최상위(root)** 에 있습니다.
2. 압축을 해제한 **내용물 전체를** `teamprotofelix/AstraHo` 저장소 `main` 브랜치 루트에 업로드합니다. 상위 폴더째 업로드하면 페이지가 열리지 않습니다.
3. GitHub → **Settings → Pages → Build and deployment → Deploy from a branch**, 브랜치 `main`, 디렉터리 `/(root)`를 설정합니다.
4. DNS 제공업체에서 `astra`의 CNAME 대상이 `teamprotofelix.github.io`인지 확인합니다. GitHub Pages **Custom domain** 에 `astra.moip.ai.kr`을 지정합니다. ZIP에는 `CNAME` 파일이 포함됩니다.
5. 인증서 발급 후 **Enforce HTTPS**를 활성화하고 https://astra.moip.ai.kr/에서 PC·Android 화면, 여섯 외부 링크, 이미지와 카드 표시를 확인합니다.

## 여섯 목적지

| 번호 | 이름 | URL |
| --- | --- | --- |
| 01 | Marie World | https://marie.moip.ai.kr/ |
| 02 | AstraHo World | https://astraho.moip.ai.kr/ |
| 03 | Skuld Lab | https://skuldlab.moip.ai.kr/ |
| 04 | AstraHo Origin | https://protofelix.moip.ai.kr/astra/ |
| 05 | Serena Library | https://protofelix.moip.ai.kr/serena/ |
| 06 | The Observatory | https://protofelix.moip.ai.kr/observatory/ |

세계수 열매, 열매 아래 6개 바로가기 버튼, 갤러리 이미지 카드를 통해 동일한 목적지로 이동할 수 있습니다. 모든 외부 링크는 새 탭으로 열리고 `noopener noreferrer` 를 설정했습니다. JavaScript를 꺼도 이동 링크는 정상 동작합니다.

## 디자인 업데이트

- 세계수: 고해상도 오리지널 세계수 아트(1,254×1,254) WebP, 원본의 황금·사파이어색 세계수 문양을 현대적인 판타지 스타일로 재해석
- 열매: 각 세계를 표현한 고화질 아트 6개(1,254×1,254), 카드 이미지로 사용
- 투명 열매: 일러스트로부터 중앙 보석만 별도 추출한 WebP 6종(480×480), 세계수 위에 얹히는 **클릭 가능** 영역
- 배경: 가벼운 우주광 WebP + CSS 점광 및 궤도 반사광
- 갤러리: PC 3열, 태블릿 2열, 스마트폰 1열로 이미지 중심 레이아웃 변화
- UX: 열매 hover/focus/touch 시 설명 갱신, 목적지 방문 버튼과 바로가기 버튼 제공
- 접근성: 키보드 포커스, 건너뛰기 링크, 대체 텍스트, 동작 감소 설정(`prefers-reduced-motion`) 적용
- 성능: 런타임 이미지는 WebP, 상세 갤러리는 지연 로드, 세계수 이미지는 preload. HTML/CSS/JS는 의존성 없이 동작

## 구성

```
index.html               전체 정적 마크업과 6개 외부 링크
styles.css               2차 비주얼 디자인 및 반응형 스타일
app.js                   열매별 소개 문구 전환 (선택 사항)
assets/world-tree.webp   세계수
assets/fruit-*.webp      전체 크기 열매 작품 6종
assets/orb-*.webp        투명 열매 6종
assets/cosmos-ambient.webp  부드러운 우주광 배경
assets/original-emblem.webp / favicon.png / og-cover.jpg
CNAME, .nojekyll, site.webmanifest, sitemap.xml, robots.txt
README.md, tools/validate_site.py
```

**PNG 원본 7개는 배포 ZIP에 들어 있지 않습니다.** 편집용 `ASTRA_World_Tree_V2_Artwork_Sources.zip`에 저장되어 있습니다. PNG를 배포 저장소에 올릴 필요가 없으므로 크기와 전송량을 줄일 수 있습니다.

원본팩의 `tools/prepare_art.py`는 Pillow로 PNG→WebP와 보석 추출을 다시 실행하는 유틸리티입니다. 미리보기 PNG 파일은 디자인 참고용이고 운영에 필요하지 않습니다.

## 검사

```bash
python -m pip install pillow
python tools/validate_site.py
node --check app.js
```

Chrome 기반 엔진에 HTML/CSS/이미지를 주입한 레이아웃 검증에서 PC(1,440px), 태블릿(768px), 모바일(390px) 화면의 카드 이미지, 6개 열매 및 인터랙션을 확인했습니다. **GitHub Pages 실제 운영 환경·Android 실기기·Safari 실기기 검사는 별개로 필요합니다.**
