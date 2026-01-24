# Test Repository

[![Repo size](https://img.shields.io/github/repo-size/NNTin/test)](https://github.com/NNTin/test)
[![Last commit](https://img.shields.io/github/last-commit/NNTin/test)](https://github.com/NNTin/test/commits)
[![License](https://img.shields.io/github/license/NNTin/test)](LICENSE)

## Overview

This repository is used for testing and quick experiments (for example hosting or
previewing sample SVG files). It is not intended for production use.

## Contents

- [SVG previews](#svg-previews)
- [RawGit migration](#rawgit-migration)
- [Notes](#notes)

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

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum. Curabitur pretium
tincidunt lacus, nec feugiat odio bibendum sed. Praesent vitae eros eget tellus
tristique bibendum, sed posuere magna tempus. Nulla facilisi. Integer non neque
nec lorem placerat varius, sed laoreet purus sodales.
