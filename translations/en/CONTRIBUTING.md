<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:34:55+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "en"
}
-->
# Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) confirming that you have the rights to, and actually do, grant us permission to use your contribution. For details, visit [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

When you submit a pull request, a CLA bot will automatically check whether you need to provide a CLA and will update the PR accordingly (e.g., status check, comment). Just follow the instructions given by the bot. You only need to do this once for all repos using our CLA.

## Code of Conduct

This project follows the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
For more information, read the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any questions or feedback.

## Cautions for creating issues

Please do not open GitHub issues for general support questions, as the GitHub issue list is intended for feature requests and bug reports. This helps us better track actual issues or bugs in the code and keeps general discussions separate from code-related topics.

## How to Contribute

### Pull Requests Guidelines

When submitting a pull request (PR) to the Phi-3 CookBook repository, please follow these guidelines:

- **Fork the Repository**: Always fork the repository to your own account before making any changes.

- **Separate pull requests (PR)**:
  - Submit each type of change in its own pull request. For example, bug fixes and documentation updates should be submitted separately.
  - Typo fixes and minor documentation updates can be combined into a single PR when appropriate.

- **Handle merge conflicts**: If your pull request shows merge conflicts, update your local `main` branch to match the main repository before making your changes.

- **Translation submissions**: When submitting a translation PR, make sure the translation folder contains translations for all files in the original folder.

### Writing Guidelines

To keep documents consistent, please follow these guidelines:

- **URL formatting**: Wrap all URLs in square brackets followed by parentheses, with no extra spaces inside or around them. For example: `[example](https://www.microsoft.com)`.

- **Relative links**: Use `./` for relative links to files or folders in the current directory, and `../` for those in a parent directory. For example: `[example](../../path/to/file)` or `[example](../../../path/to/file)`.

- **Not Country-Specific locales**: Make sure your links do not include country-specific locales. For example, avoid `/en-us/` or `/en/`.

- **Image storage**: Store all images in the `./imgs` folder.

- **Descriptive image names**: Name images descriptively using English letters, numbers, and dashes. For example: `example-image.jpg`.

## GitHub Workflows

When you submit a pull request, the following workflows will run to validate your changes. Follow the instructions below to ensure your pull request passes these checks:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

This workflow verifies that all relative paths in your files are correct.

1. To ensure your links work properly, do the following in VS Code:
    - Hover over any link in your files.
    - Press **Ctrl + Click** to follow the link.
    - If a link doesn’t work locally, it will cause the workflow to fail and won’t work on GitHub either.

1. To fix this, use the path suggestions in VS Code:
    - Type `./` or `../`.
    - VS Code will suggest available options based on what you typed.
    - Click on the desired file or folder to select the correct path.

After updating the relative path, save and push your changes.

### Check URLs Don't Have Locale

This workflow checks that web URLs do not include country-specific locales. Since this repository is globally accessible, URLs should not contain your country’s locale.

1. To verify your URLs don’t include country locales:

    - Look for text like `/en-us/`, `/en/`, or any other language locale in URLs.
    - If none are present, you will pass this check.

1. To fix this, do the following:

    - Open the file path flagged by the workflow.
    - Remove the country locale from the URLs.

After removing the locale, save and push your changes.

### Check Broken Urls

This workflow checks that all web URLs in your files are working and return a 200 status code.

1. To verify your URLs are working:

    - Check the status of URLs in your files.

2. To fix broken URLs:

    - Open the file containing the broken URL.
    - Update the URL to the correct one.

After fixing the URLs, save and push your changes.

> [!NOTE]
>
> Sometimes the URL check may fail even if the link is accessible. This can happen due to:
>
> - **Network restrictions:** GitHub Actions servers may have network limitations blocking access to certain URLs.
> - **Timeout issues:** URLs that take too long to respond may cause a timeout error in the workflow.
> - **Temporary server issues:** Occasional downtime or maintenance can make a URL temporarily unavailable during validation.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.