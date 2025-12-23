<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-12-21T14:49:21+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pcm"
}
-->
# How you fit contribute

Dis project dey welcome contributions and suggestions. Most contributions go require say you agree to a Contributor License Agreement (CLA) wey dey declare say you get the right, and you really dey give us the rights to use your contribution. For details, visit [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

When you submit a pull request, one CLA bot go automatically check whether you need provide CLA and go mark the PR correct (for example, status check, comment). Just follow the instructions wey the bot give. You go only need do am one time for all repos wey dey use our CLA.

## Code of Conduct

This project don adopt the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more info read the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) if you get any extra questions or comments.

## Wetin to watch when you dey create issues

Abeg no dey open GitHub issues for general support questions because the GitHub list suppose dey for feature requests and bug reports. Na so we fit more easy track actual issues or bugs for the code and keep general discussion separate from the code.

## How you fit contribute

### How pull requests suppose be

When you dey submit pull request (PR) to the Phi-3 CookBook repository, abeg follow the guidelines wey dey below:

- **Fork the Repository**: Always fork the repository to your own account before you make your modifications.

- **Separate pull requests (PR)**:
  - Submit each kind of change for im own pull request. For example, bug fixes and documentation updates suppose dey submitted as separate PRs.
  - Typo fixes and small documentation updates fit join inside one PR when e make sense.

- **Handle merge conflicts**: If your pull request show merge conflicts, update your local `main` branch make e mirror the main repository before you make your modifications.

- **Translation submissions**: When you dey submit translation PR, make sure say the translation folder get translations for all files wey dey the original folder.

### Writing Guidelines

To make sure say everything consistent across all documents, abeg follow these guidelines:

- **URL formatting**: Put all URLs inside square brackets followed by parentheses, no extra spaces around or inside them. For example: `[example](https://www.microsoft.com)`.

- **Relative links**: Use `./` for relative links wey dey point to files or folders for the current directory, and `../` for those wey dey the parent directory. For example: `[example](../../path/to/file)` or `[example](../../../path/to/file)`.

- **Not Country-Specific locales**: Make sure say your links no get country-specific locales. For example, avoid `/en-us/` or `/en/`.

- **Image storage**: Put all images inside the `./imgs` folder.

- **Descriptive image names**: Give images descriptive names using English characters, numbers, and dashes. For example: `example-image.jpg`.

## GitHub Workflows

When you submit a pull request, these workflows go run to validate the changes. Follow the instructions below make sure say your pull request pass the workflow checks:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

This workflow dey make sure say all relative paths for your files correct.

1. To make sure say your links dey work well, do these tasks using VS Code:
    - Hover over any link for your files.
    - Press **Ctrl + Click** to waka go the link.
    - If you click the link and e no work locally, e go trigger the workflow and e no go work for GitHub.

1. To fix the problem, do these tasks using the path suggestions wey VS Code show:
    - Type `./` or `../`.
    - VS Code go suggest the options based on wetin you don type.
    - Follow the path by clicking the file or folder wey you want make sure say your path correct.

Once you don add the correct relative path, save and push your changes.

### Check URLs Don't Have Locale

This workflow dey make sure say any web URL no get country-specific locale. Because this repository dey available globally, e important make sure say URLs no contain your country locale.

1. To confirm say your URLs no get country locales, do these tasks:

    - Check for text like `/en-us/`, `/en/`, or any other language locale inside the URLs.
    - If none of these dey for your URLs, you go pass this check.

1. To fix the issue, do these tasks:
    - Open the file path wey the workflow highlight.
    - Remove the country locale from the URLs.

Once you remove the country locale, save and push your changes.

### Check Broken Urls

This workflow dey make sure say any web URL for your files dey work and dey return 200 status code.

1. To confirm say your URLs dey work, do these tasks:
    - Check the status of the URLs wey dey your files.

2. To fix any broken URLs, do these tasks:
    - Open the file wey get the broken URL.
    - Update the URL to the correct one.

Once you don fix the URLs, save and push your changes.

> [!NOTE]
>
> E fit be cases where the URL check go fail even though the link dey accessible. This fit happen for different reasons, including:
>
> - **Network restrictions:** GitHub actions servers fit get network restrictions wey go block access to some URLs.
> - **Timeout issues:** URLs wey dey take too long to respond fit cause timeout error for the workflow.
> - **Temporary server issues:** Sometimes server fit dey down or dem dey do maintenance, so the URL fit no dey available small time while validation dey happen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:

Dis document don translate wit AI translation service Co‑op Translator (https://github.com/Azure/co-op-translator). We dey try make everything correct, but abeg note say automatic translation fit get mistakes or wrong parts. Treat the original document for im own language as di correct, official source. If na important information, make una use professional human translator. We no dey responsible for any misunderstanding or wrong interpretation wey fit come from using dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->