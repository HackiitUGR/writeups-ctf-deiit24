#!/bin/sh
docker run -v `pwd`:/src -w /src ghcr.io/webassembly/wasi-sdk clang-16 --target=wasm32-wasi --sysroot=/wasi-sysroot reto.c -o reto.wasi.wasm