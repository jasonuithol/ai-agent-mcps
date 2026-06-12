# RC::UE4SSRuntime

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/UE4SSRuntime.hpp`
Kind: struct

UE4SS Runtime Information.

This struct provides static functions to query UE4SS runtime state. These can be used by both C++ mods and Lua scripts to gracefully handle missing functionality or adapt behavior based on user configuration. Categories: Hook availability: Whether AOB scans succeeded for various hooks User preferences: Configuration choices that affect behavior Feature availability: Whether certain engine features were found

## Members

### auto IsEngineTickAvailable() -> bool
Check if the EngineTick function is available for hooking.
This checks if the AOB scan found UEngine::Tick. Required for: Frame-based delays (ExecuteInGameThreadAfterFrames, LoopInGameThreadAfterFrames) ExecuteInGameThread with EGameThreadMethod.EngineTick true if EngineTick function was found and can be hooked
### auto IsProcessEventAvailable() -> bool
Check if the ProcessEvent function is available for hooking.
This checks if the AOB scan found UObject::ProcessEvent. Required for: ExecuteInGameThread with EGameThreadMethod.ProcessEvent RegisterHook functionality true if ProcessEvent function was found and can be hooked
