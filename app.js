/* ASTRA — progressive enhancement only; every link works without JavaScript. */
(() => {
  'use strict';
  const realms = Object.freeze({
    marie:       { no:'01', category:'LIFE & VOYAGE', title:'Marie World', sub:'마리와 함께하는 작은 우주', desc:'마리의 항해일지와 우주선에서 시작되는 아늑한 별빛 여행.' },
    astraho:     { no:'02', category:'THE LIVING ARK', title:'AstraHo World', sub:'살아 있는 신의 방주', desc:'세계수를 중심으로 이어지는 공간과 승무원들의 특별한 일상.' },
    skuld:       { no:'03', category:'RESEARCH & INVENTION', title:'Skuld Lab', sub:'스쿨드의 차원 연구소', desc:'새로운 발명과 연구의 가능성이 반짝이는 신비로운 실험 공간.' },
    astra:       { no:'04', category:'ORIGIN & LORE', title:'AstraHo Origin', sub:'아스트라호 세계관의 시작', desc:'아스트라호와 네트워크 방주를 이해하는 세계관의 출발점.' },
    serena:      { no:'05', category:'LIBRARY & CREATION', title:'Serena Library', sub:'세레나의 영원의 서재', desc:'기억과 상상력, AI와 인간의 창작에 관한 이야기.' },
    observatory: { no:'06', category:'STARGAZING & REST', title:'The Observatory', sub:'별빛 전망대 레스토랑', desc:'우주를 바라보며 쉼을 얻는 고요하고 아름다운 별의 공간.' }
  });
  const category = document.getElementById('realm-category');
  const title = document.getElementById('realm-title');
  const desc = document.getElementById('realm-description');
  const visit = document.getElementById('realm-visit');
  const section = document.querySelector('.tree-section');
  const orbs = document.querySelectorAll('.orb[data-realm]');
  const indexLinks = document.querySelectorAll('.gate-index a[data-realm]');
  const all = [...orbs, ...indexLinks];
  const reset = () => { if(section) section.dataset.active = ''; };
  function activate(link) {
    const key = link.dataset.realm;
    if (!Object.prototype.hasOwnProperty.call(realms,key)) return;
    const realm = realms[key];
    category.textContent = `${realm.no} / 06 · ${realm.category}`;
    title.textContent = `${realm.title} · ${realm.sub}`;
    desc.textContent = realm.desc;
    visit.textContent = '이 세계로 떠나기 ↗';
    visit.href = link.href;
    visit.target = '_blank';
    visit.rel = 'noopener noreferrer';
    section.dataset.active = key;
  }
  for (const link of all) {
    link.addEventListener('pointerenter', () => activate(link));
    link.addEventListener('focus', () => activate(link));
    link.addEventListener('pointerdown', () => activate(link));
  }
  const stage = document.querySelector('.tree-stage');
  if (stage) stage.addEventListener('pointerleave', reset);
  for (const link of all) link.addEventListener('blur', () => {
    if (!all.includes(document.activeElement)) reset();
  });
})();
