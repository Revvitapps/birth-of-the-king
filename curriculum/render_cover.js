// renders the letter-size front cover: node render_cover.js <bookdir>
const { chromium } = require('playwright'); const fs = require('fs');
(async () => {
  const dir = process.argv[2];
  const html = fs.readFileSync(dir + '/book.html', 'utf8');
  const head = html.slice(0, html.indexOf('<section')).replace('size: 7in 10in', 'size: 8.5in 11in');
  const sec = html.slice(html.indexOf('<section'), html.indexOf('</section>') + 10).replace('class="page cover"', 'class="page cover letter"');
  fs.writeFileSync(dir + '/cover_letter.html', head + sec + '</body></html>');
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 816, height: 1056 } });
  await p.goto('file://' + dir + '/cover_letter.html', { waitUntil: 'load' });
  await p.evaluate(async () => { await document.fonts.ready; });
  await p.pdf({ path: dir + '/cover_letter.pdf', width: '8.5in', height: '11in', printBackground: true, pageRanges: '1' });
  await p.screenshot({ path: dir + '/cover_letter.png' });
  await b.close();
})();
