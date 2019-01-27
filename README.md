# macOS Sierra Dev Setup

This document describes how I set up my developer environment on macOS for web development.

The steps below were tested on **macOS Sierra**.

- [System setup](#system-setup)
- [System preferences](#system-preferences)
- [Consolas](#consolas)
- [Source Code Pro](#source-code-pro)
- [Beautiful terminal](#beautiful-terminal)
- [Projects folder](#projects-folder)
- [Apps Included](#apps-included)
- [Credits](#credits)

## TO-DO

- Add [bash-completions](http://blog.alextorres.me/2016/07/13/bash-completions-osx/)

## System setup

We're going to run a script to setup the basic software for development, plus some tweaks and tools.

First we need to install the xcode command line tools and then restart, so open a terminal and:

```shell
xcode-select --install
```

Restart and then:
```shell
/usr/bin/python -c "$(curl -fsSL https://raw.githubusercontent.com/AlexRex/mac-setup/master/setup.py)"
```

And just follow the instructions. :)

## System preferences

If this is a new computer, there are a couple tweaks I like to make to the System Preferences. Feel free to follow these, or to ignore them, depending on your personal preferences.

In **Apple Icon > System Preferences**:

- Trackpad > Tap to click
- Keyboard > Key Repeat > Fast (all the way to the right)
- Dock > Animation

## Consolas

I really like the Consolas font for coding. Being a Microsoft (!) font, it is not installed by default. Since we're going to be looking at a lot of terminal output and code, let's install it now.

There are two ways we can install it. If you bought **Microsoft Office for Mac**, install that and Consolas will be installed as well.

If you don't have Office, follow these steps:

    $ brew install cabextract
    $ cd ~/Downloads
    $ mkdir consolas
    $ cd consolas
    $ curl -O http://download.microsoft.com/download/f/5/a/f5a3df76-d856-4a61-a6bd-722f52a5be26/PowerPointViewer.exe
    $ cabextract PowerPointViewer.exe
    $ cabextract ppviewer.cab
    $ open CONSOLA*.TTF

And click **Install Font**. Thanks to Alexander Zhuravlev for his [post](http://blog.ikato.com/post/15675823000/how-to-install-consolas-font-on-mac-os-x).

## Source Code Pro

Another font very awesome.

Downoad it from its [repo](https://github.com/adobe-fonts/source-code-pro/releases).

Then in the folder OTF select all the *.otf files and open them. (Tip: Use <kbd>cmd</kbd> + <kbd> Enter </kbd> to open files).

## Beautiful terminal

Since we spend so much time in the terminal, we should try to make it a more pleasant and colorful place. What follows might seem like a lot of work, but trust me, it'll make the development experience so much better.

Let's go ahead and start by changing the font. In **iTerm > Preferences...**, under the tab **Profiles**.

Now let's add some color. I'm a big fan of the [Solarized](http://ethanschoonover.com/solarized) color scheme. It is supposed to be scientifically optimal for the eyes. I just find it pretty.

Scroll down the page and download the latest version. Unzip the archive. In it you will find the `iterm2-colors-solarized` folder with a `README.md` file, but I will just walk you through it here:

- In **iTerm2 Preferences**, under **Profiles** and **Colors**, go to **Load Presets... > Import...**, find and open the two **.itermcolors** files we downloaded.
- Go back to **Load Presets...** and select **Solarized Dark** to activate it. Voila!

**Note**: You don't have to do this, but there is one color in the **Solarized Dark** preset I don't agree with, which is *Bright Black*. You'll notice it's too close to *Black*. So I change it to be the same as *Bright Yellow*, i.e. **R 83 G 104 B 112**.

With that, open a new terminal tab (Cmd+T) and see the change! Try the list commands: `ls`, `ls -lh` (aliased to `ll`), `ls -lha` (aliased to `la`).

At this point you can also change your computer's name, which shows up in this terminal prompt. If you want to do so, go to **System Preferences** > **Sharing**. For example, I changed mine from "Nicolas's MacBook Air" to just "MacBook Air", so it shows up as `MacBook-Air` in the terminal.

Now we have a terminal we can work with!

(Thanks to Mathias Bynens for his awesome [dotfiles](https://github.com/mathiasbynens/dotfiles).)

## Projects folder

This really depends on how you want to organize your files, but I like to put all my version-controlled projects in `~/Dev`. Other documents I may have, or things not yet under version control, I like to put in `~/Dropbox` (if you have Dropbox installed), or `~/Documents`.

## Apps Included

Here is a quick list of some apps in the installer script:

### Software:

* Brew & Brew Cask with AutoUpdate
* Node.js, Ruby, Python, Git, Yeoman, NVM (node manager), own-ip.
* A bunch of Fonts.
* Essential Quicklook plugins (so you can view code, zip contents and other things)
* Essential Software: Chrome, Firefox, Skype, Slack, Spotify, iTerm2, VS Code (with configs), SourceTree and a few more.
* A lot of OSX tweaks, like disabling the annoying Mac startup sound.

### Options

* *Developer Tools*: Sequel Pro, Cyberduck, Docker, Kubectl.
* *Android Tools*: Java, Android Studio.
* *iOS Tools*: Cocoapods.
* *Web Developer Tools*: Imageoptim, WebStorm.
* *Designer Tools*: Invision Sync, Scala Preview.
* *Animations*: Makes all the Finder animations (Spaces, Exposé, Resizing) much faster.


## Credits

This is a tweaked guide original from [nicolashery](https://github.com/nicolashery/mac-dev-setup).
And the setup script is original from the [Aerloab team](https://github.com/Aerolab/setup).

Thank you so much to the both.
