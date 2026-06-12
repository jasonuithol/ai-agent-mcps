# RC::LuaBackCompat

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaCustomMemberFunctions.hpp`
Kind: namespace

## Members

### auto StaticFindObject(UClass *ObjectClass, UObject *InObjectPackage, const wchar_t *OrigInName, bool bExactClass=false) -> UObject *
### auto StaticFindObject(const wchar_t *OrigInName) -> UObject *
### auto NotifyOnNewObject(const wchar_t *class_name, std::function< void(UObject *)> &callable) -> void
### auto lua_RegisterHook_wrapper(lua_State *) -> int
### auto lua_UObjectBase_IsA_wrapper(lua_State *) -> int
