#!/bin/sh

cd ~/.local/opt
curl -L https://umbox.tophat2d.dev/dl/umbox_portable.zip -O
unzip umbox_portable.zip
mv umbox_portable umbox
export PATH=$PATH:~/.local/opt/umbox/bin
rm umbox_portable.zip