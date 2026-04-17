import { defineConfig } from "vite";
import { readdirSync, statSync } from "node:fs";
import { join, resolve } from "node:path";

function collectHtmlEntries(dir, entries = {}) {
  for (const name of readdirSync(dir)) {
    if (name === "node_modules" || name === "dist" || name === ".git") continue;
    const fullPath = join(dir, name);
    const stats = statSync(fullPath);
    if (stats.isDirectory()) {
      collectHtmlEntries(fullPath, entries);
    } else if (name.endsWith(".html")) {
      const key = fullPath
        .replace(resolve(__dirname), "")
        .replace(/^[\\/]+/, "")
        .replace(/\\/g, "/")
        .replace(/\.html$/, "");
      entries[key] = fullPath;
    }
  }
  return entries;
}

export default defineConfig({
  base: '/Mohammad-Abdulwahhab/',
  server: {
    port: 4173
  },
  build: {
    rollupOptions: {
      input: collectHtmlEntries(resolve(__dirname))
    }
  }
});
