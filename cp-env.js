const fs = require("fs");
const os = require("os");

const envFile = fs.readFileSync(".env", "utf-8");
const lines = envFile.toString().split(os.EOL);

let currentPackage = null;
const envsByPackages = {};
lines.forEach((line) => {
    if (line.trim() === "") return;
    if (line.startsWith("# ")) {
        currentPackage = line.replace("# ", "");
        envsByPackages[currentPackage] = [];
        return;
    }
    envsByPackages[currentPackage].push(line);
});

Object.entries(envsByPackages).forEach(([package, envs]) => {
    const envFileName = `./packages/${package}/.env`;
    fs.writeFile(envFileName, envs.join("\r\n"), function (err) {
        if (err) {
            console.error("Error happens");
        }
    });
});

console.log('.env created each dir.')
