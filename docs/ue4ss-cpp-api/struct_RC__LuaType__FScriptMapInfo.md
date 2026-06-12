# RC::LuaType::FScriptMapInfo

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaType/LuaTMap.hpp`
Kind: struct

## Members

### variable Unreal::FProperty * key
### variable Unreal::FProperty * value
### variable Unreal::FName key_fname
### variable Unreal::FName value_fname
### variable Unreal::FScriptMapLayout layout
### FScriptMapInfo(Unreal::FProperty *key, Unreal::FProperty *value)
### void validate_pushers(const LuaMadeSimple::Lua &lua)
Validates existence of lua pushers for this key/values in this structure.
Throws if a pusher for a key/value was not found lua Lua state to throw against.
