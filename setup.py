#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-

import os
import json
import urllib2

print "Welcome... TO THE WORLD OF TOMORROW"

name = ''
email = ''
options = {
		'developer': '',
		'android': '',
		'ios': '',
		'designer': '',
		'web' : '',
		'vim': '',
		'animations': '',
		'showhiddenfiles': '',
		'autoupdate': '',
	}


# Sudo: Spectacle, OSX Settings

# Basic Info
while name == '':
  name = raw_input("What's your name?\n").strip()

while email == '' or '@' not in email:
  email = raw_input("What's your email?\n").strip()


# Setup Options
while options['developer'] not in ['y', 'n']:
  options['developer'] = raw_input("Do you want to install Developer Tools? (%s)  " % '|'.join(['y','n']))

if options['developer'] == 'y':
  while options['android'] not in ['y', 'n']:
    options['android'] = raw_input("Do you want to install Android Tools? (%s)  " % '|'.join(['y','n']))

  while options['ios'] not in ['y', 'n']:
    options['ios'] = raw_input("Do you want to install iOS Tools? (%s)  " % '|'.join(['y','n']))

  while options['web'] not in ['y', 'n']:
    options['web'] = raw_input("Do you want to install Web Developer Tools? (%s)  " % '|'.join(['y','n']))

while options['designer'] not in ['y', 'n']:
  options['designer'] = raw_input("Do you want to install Designer Tools? (%s)  " % '|'.join(['y','n']))

while options['vim'] not in ['y', 'n']:
  options['vim'] = raw_input("Do you want to install VIM with Awesome VIM? (%s)  " % '|'.join(['y','n']))

while options['animations'] not in ['y', 'n']:
  options['animations'] = raw_input("Do you want to accelerate OSX animations? (%s)  " % '|'.join(['y','n']))

while options['showhiddenfiles'] not in ['y', 'n']:
  options['showhiddenfiles'] = raw_input("Do you want to show hidden files? (%s)  " % '|'.join(['y','n']))

while options['autoupdate'] not in ['y', 'n']:
  options['autoupdate'] = raw_input("Do you want to update your computer automatically? (Recommended) (%s)  " % '|'.join(['y','n']))


print "Hi %s!" % name
print "You'll be asked for your password at a few points in the process"
print "*************************************"
print "Setting up your Mac..."
print "*************************************"


# Create a Private Key
if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
  print "Creating your Private Key"
  os.system('ssh-keygen')


# Set computer name (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName "%s"' % name)
os.system('sudo scutil --set HostName "%s"' % name)
os.system('sudo scutil --set LocalHostName "%s"' % name)
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s"' % name)


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
  print "Installing XCode Tools"
  os.system('xcode-select --install')
  print "*************************************"
  print "Restart your Mac to continue"
  print "*************************************"
  exit()


# Install Brew & Brew Cask
print "Installing Brew & Brew Cask"
os.system('touch ~/.bash_profile')
os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew tap caskroom/cask')
os.system('brew tap homebrew/services')
os.system('brew tap caskroom/versions')
os.system('brew tap caskroom/fonts')
os.system('brew tap homebrew/versions')
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')


# Install Languages
print "Installing Git+NodeJS+Python+Ruby"
os.system('brew install git node python python3 ruby')
os.system('brew link --overwrite git node python python3 ruby')

print "Installing Useful Stuff"
os.system('brew install graphicsmagick curl wget sqlite libpng libxml2 openssl')

print "Installing Command Line Tools"
os.system('npm install -g yo bower gulp-cli grunt-cli node-gyp n own-ip')


# OSX Tweaks & Essentials
print "Installing Quicklook Helpers"
os.system('brew cask install qlcolorcode qlmarkdown qlimagesize quicklook-csv quicklook-json webpquicklook suspicious-package epubquicklook qlstephen qlprettypatch betterzipql font-hack')

print "Installing Fonts"
os.system('brew cask install font-dosis font-droid-sans font-open-sans font-open-sans-condensed font-roboto font-roboto-mono font-roboto-condensed font-roboto-slab font-arial font-arial-black font-consolas-for-powerline font-dejavu-sans font-dejavu-sans-mono-for-powerline font-georgia font-inconsolata font-inconsolata-for-powerline font-lato font-menlo-for-powerline font-meslo-lg font-meslo-lg-for-powerline font-noto-sans font-noto-serif font-source-sans-pro font-source-serif-pro font-verdana font-times-new-roman font-ubuntu font-pt-mono font-pt-sans font-pt-serif font-fira-mono font-fira-mono-for-powerline font-fira-code font-fira-sans font-fontawesome font-source-code-pro font-anka-coder')

print "Installing Essential Apps"
os.system('brew cask install iterm2 spectacle the-unarchiver')
os.system('brew cask install google-chrome firefox sourcetree atom dropbox skype spotify slack vlc macdown cheatsheet trayplay')
os.system('ln -s /Applications/Atom.app/Contents/Resources/app/atom.sh /usr/local/bin/atom')

print "Creating Essential Dotfiles"
os.system('mkdir ~/.dotfiles')
os.system('curl -o ~/.bash_profile https://raw.githubusercontent.com/AlexRex/mac-setup/master/.dotfiles/.bash_profile')
os.system('curl -o ~/.gitconfig https://raw.githubusercontent.com/AlexRex/mac-setup/master/.dotfiles/.gitconfig')
os.system('curl -o ~/.dotfiles/.aliases https://raw.githubusercontent.com/AlexRex/mac-setup/master/.dotfiles/.aliases')
os.system('curl -o ~/.dotfiles/.bash_prompt https://raw.githubusercontent.com/AlexRex/mac-setup/master/.dotfiles/.bash_prompt')

print "Setting Git Credentials"
os.system('git config --global user.name "%s"' % name)
os.system('git config --global user.email "%s"' % email)
os.system('git config --global credential.helper osxkeychain')

# Appropriate Software
if options['developer'] == 'y':
  print "Installing Developer Tools"
  os.system('brew cask install ngrok sequel-pro cyberduck mysql mongodb redis robomongo')

if options['android'] == 'y':
  print "Installing Android Tools"
  os.system('brew cask install java')
  os.system('brew cask install android-studio')
  os.system('brew install android-platform-tools')

if options['ios'] == 'y':
  print "Installing iOS Tools"
  os.system('sudo gem install cocoapods')

if options['web'] == 'y':
  print "Installing Web Developer Tools"
  os.system('brew cask install imageoptim imagealpha webstorm')

if options['designer'] == 'y':
  print "Installing Designer Tools"
  os.system('brew cask install invisionsync iconjar skala-preview lingo')
  os.system('brew cask install sketch-tool principle framer-studio origami')

if options['vim'] == 'y':
  print "Installing VIM + Awesome VIM"

  os.system('brew install vim --override-system-vi')
  os.system('git clone https://github.com/amix/vimrc.git ~/.vim_runtime')
  os.system('sh ~/.vim_runtime/install_awesome_vimrc.sh')


# Random OSX Settings
print "Tweaking OSX Settings"

if options['showhiddenfiles'] == 'y':
  # Finder: show hidden files by default
  os.system('defaults write com.apple.finder AppleShowAllFiles -bool true')
  # Finder: show all filename extensions
  os.system('defaults write NSGlobalDomain AppleShowAllExtensions -bool true')


# Finder: allow text selection in Quick Look
os.system('defaults write com.apple.finder QLEnableTextSelection -bool true')
# Check for software updates daily
os.system('defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1')
# Disable auto-correct
#os.system('defaults write NSGlobalDomain NSAutomaticSpellingCorrectionEnabled -bool false')
# Require password immediately after sleep or screen saver begins
os.system('defaults write com.apple.screensaver askForPassword -int 1')
os.system('defaults write com.apple.screensaver askForPasswordDelay -int 0')
# Show the ~/Library folder
os.system('chflags nohidden ~/Library')
# Don’t automatically rearrange Spaces based on most recent use
os.system('defaults write com.apple.dock mru-spaces -bool false')
# Prevent Time Machine from prompting to use new hard drives as backup volume
os.system('defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true')
# Mute startup sound
os.system('sudo nvram SystemAudioVolume=", "')


if options['animations'] == 'y':
  print "Tweaking System Animations"
  os.system('defaults write NSGlobalDomain NSWindowResizeTime -float 0.1')
  os.system('defaults write com.apple.dock expose-animation-duration -float 0.15')
  os.system('defaults write com.apple.dock autohide-time-modifier -float 0.2')
  os.system('defaults write NSGlobalDomain com.apple.springing.delay -float 0.5')


if options['autoupdate'] == 'y':
  print "Enabling Automatic Brew Updates & Upgrades"
  os.system('brew tap domt4/autoupdate')
  os.system('brew autoupdate --start --upgrade')


# Make Google Chrome the default browser
os.system('open -a "Google Chrome" --args --make-default-browser')


# Clean Up
os.system('brew cleanup && brew cask cleanup')


print ""
print ""
print "*************************************"

print "*************************************"
print "Your SSH Public Key Is:"
with open(os.path.expanduser("~") + '/.ssh/id_rsa.pub', 'r') as f:
  print f.read()
print ""

print "*************************************"
print "Remember to restart your Mac"
print "*************************************"
