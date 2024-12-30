#!/usr/bin/env zx

import "zx/globals";

// devlog-toc.mjs

const devLogPath = __dirname;

async function generateTOC() {
  //   // Get all markdown files in the devLog directory
  const files = await $`ls ${devLogPath}/*.md`;
  const fileList = files.stdout.trim().split("\n");
  console.log(fileList);

  let tocContent = `# DevLog Table of Contents\n\n`;

  //   // Sort files by date (assuming filename format DD-MM-YY-devLog.md)
  //   const sortedFiles = fileList
  //     .filter((file) => file.includes("-devLog.md")) // Only include devLog files
  //     .sort((a, b) => b.localeCompare(a)); // Sort in reverse chronological order

  //   for (const file of sortedFiles) {
  //     const fileName = path.basename(file);
  //     const fileContent = await fs.readFile(file, "utf-8");

  //     // Extract the first heading from the file content
  //     const firstHeading = fileContent.match(/^#\s+(.+)/m)?.[1] || fileName;

  //     // Create entry with link and title
  //     const entry = `- [${fileName.replace(".md", "")}](${fileName}) - ${firstHeading}\n`;
  //     tocContent += entry;
}

//   // Write the TOC to the devLog.md file
//   await fs.writeFile(path.join(devLogPath, "devLog.md"), tocContent);

//   console.log("Table of Contents generated successfully!");
// }

try {
  await generateTOC();
} catch (error) {
  console.error("Error generating TOC:", error);
}
