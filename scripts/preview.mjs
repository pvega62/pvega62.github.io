import { spawn } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const middleware = path.join(siteRoot, "scripts", "clean-urls.js");
const host = process.env.HOST || "0.0.0.0";
const port = process.env.PORT || "8080";

const args = [
  "--yes",
  "live-server",
  `"${siteRoot}"`,
  `--host=${host}`,
  `--port=${port}`,
  `--middleware="${middleware}"`,
];

if (process.env.NO_OPEN === "1") {
  args.push("--no-browser");
}

const child = spawn(`npx ${args.join(" ")}`, {
  cwd: siteRoot,
  shell: true,
  stdio: "inherit",
});

child.on("exit", (code, signal) => {
  if (signal) {
    process.kill(process.pid, signal);
    return;
  }
  process.exit(code === null ? 1 : code);
});
