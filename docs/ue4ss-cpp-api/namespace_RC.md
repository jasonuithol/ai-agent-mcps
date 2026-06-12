# RC

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/CrashDumper.hpp`
Kind: namespace

## Members

### enum GameThreadExecutionMethod

- `ProcessEvent`
- `EngineTick`
### enum DidLuaScanSucceed

- `Yes`
- `No`
### typedef size_t ModId
### typedef const std::function< DidLuaScanSucceed(void *)> LuaScriptMatchFoundFunc
### typedef const std::function< void(DidLuaScanSucceed)> LuaScriptScanCompleteFunc
### typedef Unreal::EObjectFlags EObjectFlags
### typedef Unreal::UObjectBaseUtility UObjectBaseUtility
### typedef Unreal::UObject UObject
### typedef Unreal::AActor AActor
### typedef Unreal::UClass UClass
### typedef Unreal::UStruct UStruct
### typedef Unreal::UScriptStruct UScriptStruct
### typedef Unreal::FField FField
### typedef Unreal::FName FName
### typedef Unreal::FString FString
### typedef Unreal::FProperty FProperty
### typedef Unreal::FIntProperty FIntProperty
### typedef Unreal::FInt8Property FInt8Property
### typedef Unreal::FInt16Property FInt16Property
### typedef Unreal::FInt64Property FInt64Property
### typedef Unreal::FByteProperty FByteProperty
### typedef Unreal::FFloatProperty FFloatProperty
### typedef Unreal::FObjectProperty FObjectProperty
### typedef Unreal::FWeakObjectProperty FWeakObjectProperty
### typedef Unreal::FClassProperty FClassProperty
### typedef Unreal::FBoolProperty FBoolProperty
### typedef Unreal::FArrayProperty FArrayProperty
### typedef Unreal::FStructProperty FStructProperty
### typedef Unreal::FNameProperty FNameProperty
### typedef Unreal::FTextProperty FTextProperty
### typedef Unreal::FStrProperty FStrProperty
### typedef Unreal::FUtf8StrProperty FUtf8StrProperty
### typedef Unreal::FAnsiStrProperty FAnsiStrProperty
### typedef Unreal::TArray< T > TArray
### typedef Unreal::UFunction UFunction
### typedef Unreal::TMap< T1, T2, T3, T4 > TMap
### typedef Unreal::FMapProperty FMapProperty
### typedef Unreal::UnrealScriptFunction UnrealScriptFunction
### typedef Unreal::FFrame FFrame
### typedef Unreal::UEnum UEnum
### typedef Unreal::FWeakObjectPtr FWeakObjectPtr
### typedef Unreal::FDelegateProperty FDelegateProperty
### typedef Unreal::FMulticastInlineDelegateProperty FMulticastInlineDelegateProperty
### typedef Unreal::FMulticastSparseDelegateProperty FMulticastSparseDelegateProperty
### typedef Unreal::FSetProperty FSetProperty
### typedef Unreal::FSoftClassProperty FSoftClassProperty
### typedef Unreal::FEnumProperty FEnumProperty
### typedef Unreal::FFieldPathProperty FFieldPathProperty
### typedef Unreal::TFieldIterator< T > TFieldIterator
### typedef Unreal::TFieldRange< T > TFieldRange
### typedef Unreal::FAssetData FAssetData
### typedef Unreal::UAssetRegistry UAssetRegistry
### typedef Unreal::UAssetRegistryHelpers UAssetRegistryHelpers
### variable std::unordered_map< Unreal::FName, Unreal::UScriptStruct * > g_script_struct_cache_map
### variable constexpr ModId InvalidModId
### auto constexpr TRY(CodeToTry code_to_try)
### auto setup_script_struct_cache_map() -> void
### auto setup_global_metatable(lua_State *) -> void
### auto UObjectBase_memberr_function_wrapper_MyTestFunc(lua_State *) -> int
### auto UObjectBase_member_function_wrapper_GetNamePrivate(lua_State *) -> int
### auto UObjectBase_member_function_wrapper_Cast(lua_State *) -> int
### auto FField_member_function_wrapper_CastField(lua_State *) -> int
### auto UEnum_member_function_wrapper_ForEachName(lua_State *) -> int
### auto UClass_member_function_wrapper_StaticClass(lua_State *) -> int
### auto UObjectBase_metamethod_wrapper_Index(lua_State *, void *) -> int
### auto UObjectBase_metamethod_wrapper_NewIndex(lua_State *, void *) -> int
### auto UFunction_metamethod_wrapper_Call(lua_State *, void *) -> int
### auto UObjectBaseUtility_metamethod_wrapper_Index(lua_State *, void *) -> int
### auto UObjectBaseUtility_metamethod_wrapper_NewIndex(lua_State *, void *) -> int
### auto ArrayTest_metamethod_wrapper_GC(lua_State *, void *) -> int
### auto LuaUScriptStruct_metamethod_wrapper_Index(lua_State *, void *) -> int
### auto LuaUScriptStruct_metamethod_wrapper_NewIndex(lua_State *, void *) -> int
### auto LuaUScriptStruct_metamethod_wrapper_GC(lua_State *, void *) -> int
### auto ArrayTest_member_function_wrapper_GetElementAtIndex(lua_State *) -> int
### auto ArrayTest_member_function_wrapper_ForEach(lua_State *) -> int
### auto lua_warn_wrapper(lua_State *) -> int
### auto lua_print_wrapper(lua_State *) -> int
### auto lua_FindAllOf_wrapper(lua_State *) -> int
### auto lua_RegisterKeyBind_wrapper(lua_State *) -> int
### auto AllocateMemory(size_t size) -> MemoryItem *
### auto FreeMemory(MemoryItem *memory_item) -> void
### auto FreeMemory(uintptr_t memory) -> void
### auto lua_Test_ReadBytes_wrapper(lua_State *lua_state) -> int
### auto lua_Test_ReadUInt8_wrapper(lua_State *lua_state) -> int
### auto lua_Test_ReadUInt16_wrapper(lua_State *lua_state) -> int
### auto lua_Test_ReadUInt32_wrapper(lua_State *lua_state) -> int
### auto lua_Test_ReadUInt64_wrapper(lua_State *lua_state) -> int
### auto lua_Test_ReadInt8_wrapper(lua_State *lua_state) -> int
### auto lua_Test_ReadInt16_wrapper(lua_State *lua_state) -> int
### auto lua_Test_ReadInt32_wrapper(lua_State *lua_state) -> int
### auto lua_Test_ReadInt64_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteBytes_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteUInt8_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteUInt16_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteUInt32_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteUInt64_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteInt8_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteInt16_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteInt32_wrapper(lua_State *lua_state) -> int
### auto lua_Test_WriteInt64_wrapper(lua_State *lua_state) -> int
### auto Test_GetUnsignedMemorySetup() -> MemoryItem *
### auto Test_GetSignedMemorySetup() -> MemoryItem *
### auto Test_GetPlayerControllerVTablePointer() -> MemoryItem *
### auto GetWorldTest() -> UWorld *
### auto GetArrayTest() -> Unreal::TArray< UObject * > &
### auto GetArrayTest2() -> Unreal::TArray< int16_t > &
### auto GetArrayTest3() -> Unreal::TArray< FName >
### auto Test_Get_UObject_Nullptr() -> UObject *
### auto get_mod_ref(const LuaMadeSimple::Lua &lua) -> class LuaMod *
### auto scan_complete_default_func(DidLuaScanSucceed) -> void
### auto scan_from_lua_script(std::filesystem::path &script_file_path_and_name, std::vector< SignatureContainer > &, LuaScriptMatchFoundFunc &match_found_func, LuaScriptScanCompleteFunc &scan_complete_func=&scan_complete_default_func) -> void
### auto setup_lua_scan_overrides(std::filesystem::path &working_directory, Unreal::UnrealInitializer::Config &) -> void
