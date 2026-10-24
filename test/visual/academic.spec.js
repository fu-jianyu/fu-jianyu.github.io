const { test, expect } = require("@playwright/test");

for (const route of ["/", "/publications/", "/projects/", "/blog/", "/cv/", "/blog/2026/hku-research-visit/", "/blog/2026/lup-paper-accepted/"]) {
  test(`academic page ${route}`, async ({ page }, testInfo) => {
    const response = await page.goto(route);
    expect(response.status()).toBe(200);
    await expect(page.locator("h1")).toHaveCount(1);
    await expect(page.locator("body")).not.toContainText(/REPLACE_WITH_|Albert Einstein|A simple inline announcement/);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBe(true);
    await expect(page.locator('link[rel="canonical"]')).toHaveAttribute("href", `https://fu-jianyu.github.io${route}`);
    await page.screenshot({ path: testInfo.outputPath("page.png"), fullPage: true });
  });
}

test("CV download and new announcements are reachable", async ({ page, request }) => {
  await page.goto("/");
  await expect(page.getByRole("link", { name: "Brief announcement and graphical abstract" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Visit highlights and photos" })).toBeVisible();
  const pdf = await request.get("/assets/pdf/Jianyu_Fu_CV.pdf");
  expect(pdf.status()).toBe(200);
  expect((await pdf.body()).subarray(0, 5).toString()).toBe("%PDF-");
});

test("HKU visit has exactly the four supplied photos", async ({ page }) => {
  await page.goto("/blog/2026/hku-research-visit/");
  const photos = page.locator('article img[src*="/hku-2026/"]');
  await expect(photos).toHaveCount(4);
  await expect(photos.first()).toHaveAttribute("src", /group-photo\.jpg$/);
  for (const img of await photos.all()) {
    await img.scrollIntoViewIfNeeded();
    await expect.poll(() => img.evaluate((el) => el.complete && el.naturalWidth > 0)).toBe(true);
  }
});

test("publication filtering finds the accepted paper", async ({ page }) => {
  await page.goto("/publications/");
  const search = page.locator("#bibsearch");
  await search.fill("R-ECoT");
  await expect(page.locator(".publications")).toContainText("Accepted 23 October 2026");
  await expect(page.locator(".publications")).toContainText("JCR Q1");
});
