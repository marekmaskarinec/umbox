#!/bin/sh

mkdir -p ~/.local/opt
cd ~/.local/opt
rm -rf umbox
curl -L https://umbox.tophat2d.dev/dl/umbox_linux.zip -O
unzip -q umbox_linux.zip
mv umbox_linux umbox
echo "$PATH" | grep "$HOME/.local/opt/umbox" || echo NOTE: Please make sure ~/.local/opt/umbox is in your PATH
export PATH="$PATH:~/.local/opt/umbox"
rm umbox_linux.zip
