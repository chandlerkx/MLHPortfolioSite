const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  try {
    await page.goto('http://127.0.0.1:5000', { waitUntil: 'networkidle0', timeout: 10000 });
    const content = await page.content();
    const fs = require('fs');
    fs.writeFileSync('dump.html', content);
    console.log("Dumped to dump.html");
  } catch (err) {
    console.log("Error:", err);
  }

  await browser.close();
})();
