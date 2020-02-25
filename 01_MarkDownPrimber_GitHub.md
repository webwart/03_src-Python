# A quick primer on Markdown

## Paragraphs

Markdown aims to be a markup language that's natural to write and read, as if it were typed on a typewriter. You can write in Notepad, or whatever text editor you prefer, and copy/paste it into an e-mail, or save it as a .txt file and send it to us as an attachment if you like. **StackEdit isn't a necessary part of the process**; it just helps you see what the conversion to HTML will look like. It also gives you buttons for all the features.

For the most part, you just write as you normally would -- paragraphs are just blocks of text separated by two carriage returns, and the Markdown parser will turn them into HTML paragraph tags for you.

You can emphasize a bit of your text by wrapping it with asterisks: *one asterisk for emphasis (italic)*, and **two asterisks for heavy emphasis (bold)**. If you prefer, you can use _single_ or __double underlines__ instead of asterisks.

URLs can be typed plain, like this, and they'll be turned into links: http://cartanium.com/

Of course, links look better with some human-readable text. Wrap the link text in square brackets, and the URL in parentheses directly afterwards: [Check out our case studies!](http://cartanium.com/case-studies)

If you want to link to a page within the site, you can leave off the domain name: [Read about our features...](/features)

To create a divider, just put three hyphens on a line:

---

## Headings

As you might have noted, headings start with one or more pound signs. A top-level header (the SEO-friendly `<H1>` tag) has one pound sign, a subheader has two, a sub-sub-header has three, etc.

---

## Lists

* Bullet points
* are just as simple
* as an asterisk
- or a hyphen
- at the beginning of the line.

* You can even
    * create sub-lists
    * by indenting
    * four spaces.

---

1. Numbered lists
2. are simple
3. as well!

---

## Quotations

> A block quotation starts with a right-pointing angle bracket. You can use this for testimonials, and Amber was suggesting that you use them to indicate the synopsis under each bullet point too.

> You can have multiple paragraphs in a quotation, and as long as they're beside each other and they all start with a right-pointing angle bracket, they'll become part of the same quote.

> * You can even
> * put a list
> * in the quotation.

---

## Getting really fancy

You can even put quotations inside bullet points:

* URL rewriting
  > All product and category URLs are given friendly names. This helps your customer understand where the link is going to take them, and helps improve your SEO. [Read more...](/url-rewriting)

* Breadcrumb navigation
  > At the top of most pages, you'll see a breadcrumb trail that lets you know where you are on the site. This helps customers orient themselves, and provides links within your site so search engines can find all your pages. [Read more...](/breadcrumbs)

---

## Now, a bit about meta tags

Markdown doesn't have any way of creating meta tags; it's meant for the body of the document. But I don't see any reason you couldn't just put the meta tags at the top of your document, and then we could just copy/paste them into the HTML. You could mark them up as description lists, which are normally used for glossaries, but would be great for this sort of thing. The tag name is on its own line, and the content starts with a colon:

Title
: Single-Page Checkout

Description
: Cartanium features an effortless single-page checkout that will convert prospects into paying customers faster than you thought possible.

Keywords
: checkout, simple shopping cart checkout, streamlined shopping cart, single page checkout