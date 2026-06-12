# RC::LuaLibrary

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaLibrary.hpp`
Kind: namespace

## Members

### enum ExportedFunctionStatus

- `NO_ERROR_TO_EXPORT` = 0
- `SUCCESS` = 1
- `VARIABLE_NOT_FOUND` = 2
- `MOD_IS_NULLPTR` = 3
- `SCRIPT_FUNCTION_RETURNED_FALSE` = 4
- `UNABLE_TO_CALL_SCRIPT_FUNCTION` = 5
- `SCRIPT_FUNCTION_NOT_FOUND` = 6
- `UNKNOWN_ERROR` = 7
- `UE4SS_NOT_INITIALIZED` = 8
### enum DefaultDataType

- `ConstCharPtr`
- `Float`
### typedef void(*)(const char *, const char *, int32_t, ReturnValue &) SetScriptVariableInt32Signature
### typedef void(*)(const char *, const char *, DefaultDataStruct &, ReturnValue &) SetScriptVariableDefaultDataSignature
### typedef void(*)(const char *, const char *, ReturnValue &, ScriptFuncReturnValue &) CallScriptFunctionSignature
### typedef bool(*)() IsUE4SSInitializedSignature
### variable const char * script
### variable const char * variable_name
### variable const char int32_t new_value
### variable const char int32_t ReturnValue & void
### variable const char DefaultDataStruct & external_data
### variable const char * function_name
### auto get_outputdevice_ref(const LuaMadeSimple::Lua &) -> const Unreal::FOutputDevice *
### auto set_outputdevice_ref(const LuaMadeSimple::Lua &, Unreal::FOutputDevice *) -> void
### auto global_print(const LuaMadeSimple::Lua &) -> int
### auto load_export(const LuaMadeSimple::Lua &) -> int
### auto deref_to_int32(const LuaMadeSimple::Lua &) -> int
### __declspec(dllexport) auto get_lua_state_by_mod_name(const char *mod_name) -> lua_State *
