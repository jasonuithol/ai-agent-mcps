# RC::LuaType::FScriptSetInfo

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaType/LuaTSet.hpp`
Kind: struct

## Members

### variable Unreal::FProperty * element
### variable Unreal::FName element_fname
### variable Unreal::FScriptSetLayout layout
### FScriptSetInfo(Unreal::FProperty *element)
### void validate_pushers(const LuaMadeSimple::Lua &lua)
Validates existence of lua pushers for this element in this structure.
Throws if a pusher for the element was not found lua Lua state to throw against.
