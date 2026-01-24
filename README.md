# Test Repository

[![Repo size](https://img.shields.io/github/repo-size/NNTin/test)](https://github.com/NNTin/test)
[![Last commit](https://img.shields.io/github/last-commit/NNTin/test)](https://github.com/NNTin/test/commits)
[![License](https://img.shields.io/github/license/NNTin/test)](LICENSE)

## Overview

This repository is used for testing and quick experiments (for example hosting or
previewing sample SVG files). It is not intended for production use.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua.

## Contents

- [SVG previews](#svg-previews)
- [RawGit migration](#rawgit-migration)

## SVG previews

### Local files

![](test/animateddiscord.svg)
[<img src="test/animateddiscord.svg">]()

### External links

![](https://my.mixtape.moe/xnaieq.svg)
![](https://cdn.jsdelivr.net/gh/NNTin/test@fbe3b4e3/test/animateddiscord.svg)
[<img src="https://cdn.jsdelivr.net/gh/NNTin/test@fbe3b4e3/test/animateddiscord.svg">]()

## RawGit migration

RawGit was shut down and now returns `410 Gone` responses, so the hosted SVG
previews were breaking. The CDN links have been updated to
[jsDelivr](https://www.jsdelivr.com/?docs=gh), which directly serves GitHub
content using the `cdn.jsdelivr.net/gh/<user>/<repo>@<commit>/path` pattern. If
you need to pin to a commit, replace `@fbe3b4e3` with your desired commit hash or
tag. The old RawGit links are no longer expected to work.
