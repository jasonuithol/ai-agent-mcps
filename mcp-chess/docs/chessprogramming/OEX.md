# OEX

Source: https://www.chessprogramming.org/OEX

# Android Open Exchange format

This OEX allows you to put chess program binaries in an Android phone so that applications like Aart Bik's Chess for Android and Chess for All by Karl Schreiner can use it.

Previously one could just place the binary on the SD-card and import it into the chess board application. That no longer works due to tightened security measures.

The idea is to create a wrapper in Java/Kotlin and store the chess-program binary in the .apk of that Java-application (as a native binary). Instead of just as-is, you must rename it to as if it was a shared library. E.g. stockfish.exe becomes libstockfish.so.

## References

- <https://www.aartbik.com/MISC/uchess.html>

- <https://code.google.com/archive/p/chessenginesupport-androidlib/>