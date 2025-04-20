# Static Site Generator

This is a **static site generator** that converts Markdown files into fully functional HTML pages.

You can see the [website](https://h0dy.github.io/static-site-generator/)

## Features

- 📝 Converts Markdown files into HTML
- 📄 Supports generating multiple pages
- 🖼️ Handles images and links properly
- ✅ Includes unit tests to ensure functionality (my first time writing unit tests!)

## What I Learned from This Project

This project helped me gain hands-on experience with:

- Working with file systems and parsing Markdown content
- Generating and structuring dynamic HTML pages
- Writing and running unit tests to validate functionality

## To Run This Project On Your Local Machine

### 1. Clone The Repository

```bash
git clone https://github.com/h0dy/static-site-generator.git
```

### Providing Markdown Files

By default, the script looks for a folder named `content`. Inside this folder, you can place your Markdown files.

The generator supports multiple pages. If you'd like to organize content better, you can create a subfolder for each page within the `content` directory.

### Static Assets

If your pages include images or custom styles, place them in the `static` folder.

- For styles, use the `index.css` file located in the `static` folder.
- A default stylesheet is already provided, but feel free to customize or replace it to fit your design.
