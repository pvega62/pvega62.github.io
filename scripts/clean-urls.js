"use strict";

// Connect middleware for live-server: resolves the extensionless URLs the site
// publishes (/uxwriting) to the HTML file on disk (uxwriting.html), matching how
// GitHub Pages serves the same paths.

const fs = require("fs");
const path = require("path");

const root = path.resolve(process.env.SITE_ROOT || process.cwd());

function isFile(candidate) {
  try {
    return fs.statSync(candidate).isFile();
  } catch (err) {
    return false;
  }
}

module.exports = function cleanUrls(req, res, next) {
  if (req.method !== "GET" && req.method !== "HEAD") {
    return next();
  }

  const queryIndex = req.url.indexOf("?");
  const pathname = queryIndex === -1 ? req.url : req.url.slice(0, queryIndex);
  const search = queryIndex === -1 ? "" : req.url.slice(queryIndex);

  if (pathname.endsWith("/") || path.extname(pathname)) {
    return next();
  }

  let decoded;
  try {
    decoded = decodeURIComponent(pathname);
  } catch (err) {
    return next();
  }

  const target = path.resolve(root, "." + decoded);
  if (target !== root && !target.startsWith(root + path.sep)) {
    return next();
  }

  if (isFile(target + ".html")) {
    req.url = pathname + ".html" + search;
  }

  return next();
};
