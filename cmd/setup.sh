#!/bin/sh

mkdir -p ~/.local/opt
cd ~/.local/opt
curl -L https://umbox.tophat2d.dev/dl/umbox_linux.zip -O
unzip umbox_linux.zip
mv umbox_linux umbox
export PATH=$PATH:~/.local/opt/umbox/bin
rm umbox_linux.zip
