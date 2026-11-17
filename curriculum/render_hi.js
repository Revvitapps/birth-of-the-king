const { chromium } = require('playwright');
(async () => {
  const [dir, html, out, shots] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 816, height: 1056 }, deviceScaleFactor: 2 });
  await p.goto('file://' + dir + '/' + html, { waitUntil: 'load' });
  await p.evaluate(async () => {
    await document.fonts.ready;
    const imgs = [...document.images];
    await Promise.all(imgs.map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })));
    const log = [];
    document.querySelectorAll('.fit').forEach((el) => {
      const over = () => el.scrollHeight > el.clientHeight + 1;
      let fs = parseFloat(getComputedStyle(el).fontSize);
      let lnH = 0.34, guard = 0;
      while (over() && guard++ < 80) {
        const fl = [...el.querySelectorAll('.drawbox.fill')].filter(x => parseFloat(x.style.height) > 1.3);
        if (fl.length) { fl.forEach(x => x.style.height = (parseFloat(x.style.height) - 0.05) + 'in'); guard--; continue; }
        if (el.classList.contains('wbody') && lnH > 0.27) { lnH -= 0.01; el.querySelectorAll('.ln').forEach(l => l.style.height = lnH + 'in'); continue; }
        const bx = [...el.querySelectorAll('.drawbox,.grid4')]; let shr = false;
        bx.forEach(x => { const h = parseFloat(x.style.height); if (h > 1.3) { x.style.height = (h - 0.1) + 'in'; shr = true; } });
        if (shr && el.classList.contains('wbody')) continue;
        if (fs <= 11.5) break;
        fs -= 0.25; el.style.fontSize = fs + 'px';
      }
      const pg = el.closest('.page');
      const title = (pg.querySelector('h1') || {}).innerText;
      if (over()) log.push('OVERFLOW: ' + title + ' by ' + (el.scrollHeight - el.clientHeight) + 'px');
      if (fs < 13.5) log.push('small font ' + fs.toFixed(2) + 'px: ' + title);
    });
    window.__log = log;
  });
  console.log((await p.evaluate(() => window.__log)).join('\n'));
  await p.pdf({ path: out, width: '8.5in', height: '11in', printBackground: true });
  if (shots) {
    const els = await p.$$('.page');
    for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: `${shots}/p${String(i + 1).padStart(3, '0')}.png` });
  }
  await b.close();
})();
