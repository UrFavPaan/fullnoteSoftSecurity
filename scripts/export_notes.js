const fs = require("fs");

const source = fs.readFileSync("app.js", "utf8");
const start = source.indexOf("const chapters = ");
const end = source.indexOf("\n\nconst chapterNav");
if (start < 0 || end < 0) {
  throw new Error("Could not locate chapters data in app.js");
}

const dataCode = source.slice(start, end) + "\nreturn chapters;";
const chapters = new Function(dataCode)();

const lines = [
  "# Software Security Comprehensive Notes",
  "",
  "Source rule: These notes are based only on the provided CCSB5133 lecture PDFs. No outside sources were used.",
  "",
  "Memory aids are created from the lists and concepts in the slides.",
  ""
];

for (const chapter of chapters) {
  lines.push(`## ${chapter.number}. ${chapter.title}`, "");
  lines.push(`Source: ${chapter.source}`, "");
  lines.push(chapter.summary, "");

  for (const section of chapter.sections) {
    lines.push(`### ${section.heading}`, "");
    lines.push(`Source: ${section.source}`, "");
    for (const bullet of section.bullets) {
      lines.push(`- ${bullet}`);
    }
    lines.push("");
  }

  lines.push("### Memory Aids", "");
  for (const item of chapter.memory) {
    lines.push(`- ${item}`);
  }
  lines.push("");
}

fs.writeFileSync("COMPREHENSIVE_NOTES.md", lines.join("\n"), "utf8");
console.log("COMPREHENSIVE_NOTES.md");
