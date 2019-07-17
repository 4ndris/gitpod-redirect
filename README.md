# Gitpod Redirect
## Description
GitHub repositories can be opened in Gitpod by linking to `https://gitpod.io/#https://github.com/<username>/<repository>`.  The link to the GitHub repository has to be explicitly specified after the `#`.  Having to explicitly specify the GitHub repository information can be problematic when repository names change or when a repository is cloned.

This project allows for the GitHub repository link to be inferred through the request’s Referrer Header when linked from the Readme in the GitHub repository.  This prevents hardcoding of the user and repository name when linking to Gitpod.

## Usage
Add the following Markdown to your repository’s Readme file:

```[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect.herokuapp.com/)```

This will result in the display of a dynamic _Open in Gitpod_ button:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod-redirect.herokuapp.com/)
