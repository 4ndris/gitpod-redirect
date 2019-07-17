# Gitpod Redirect
## Description
GitHub repositories can be opened in Gitpod by linking to `https://gitpod.io/#https://github.com/<username>/<repository>`.  Note how the repository URL has to be explicitly specified after the `#`. 

This project allows for the GitHub repository URL to be inferred through the `referer` header when linked from the README file in the GitHub repository.  This is convenient because it avoids hard-coding the specific repository URL into the link, allowing forks and branches of the repository to work properly without a change to the link href.

## Usage
Add the following Markdown to your repository’s README file:

```[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect.herokuapp.com)```

Here’s the equivalent content as HTML if you’d prefer not to use Markdown:

```html
<a href="https://gitpod-redirect.herokuapp.com">
  <img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open in Gitpod">
</a>
```

This will result in the display of a dynamic _Open in Gitpod_ button:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect.herokuapp.com)
