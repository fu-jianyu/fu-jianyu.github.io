const { devices } = require("@playwright/test");
module.exports = {
  testDir: __dirname,
  testMatch: "academic.spec.js",
  timeout: 60000,
  use: {
    baseURL: process.env.SITE_URL || "http://127.0.0.1:4000",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
  },
  projects: [
    { name: "desktop", use: { viewport: { width: 1366, height: 900 } } },
    { name: "mobile", use: { ...devices["iPhone 12"], defaultBrowserType: "chromium" } },
  ],
  webServer: process.env.NO_WEBSERVER
    ? undefined
    : {
        cwd: require("path").resolve(__dirname, "../.."),
        command: "bundle exec jekyll serve --host 127.0.0.1 --port 4000 --quiet",
        url: "http://127.0.0.1:4000",
        reuseExistingServer: !process.env.CI,
        timeout: 300000,
      },
};
