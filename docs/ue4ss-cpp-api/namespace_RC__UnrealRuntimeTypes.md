# RC::UnrealRuntimeTypes

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaCustomMemberFunctions.hpp`
Kind: namespace

## Members

### typedef ToLuaParams FromLuaParams
### variable std::unordered_map< FName, void(*)(lua_State *, ToLuaParams)> g_unreal_property_to_lua
### variable std::unordered_map< FName, void(*)(lua_State *, FromLuaParams)> g_unreal_property_from_lua
### auto populate_unreal_property_to_lua_map() -> void
### auto ObjectProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto ClassProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto Int8Property_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto Int16Property_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto IntProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto Int64Property_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto ByteProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto UInt16Property_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto UInt32Property_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto UInt64Property_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto StructProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto ArrayProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto FloatProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto DoubleProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto BoolProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto EnumProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto WeakObjectProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto NameProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto TextProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto StrProperty_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto function_to_lua(lua_State *lua_state, ToLuaParams) -> void
### auto ObjectProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto ClassProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto Int8Property_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto Int16Property_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto IntProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto Int64Property_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto ByteProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto UInt16Property_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto UInt32Property_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto UInt64Property_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto StructProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto ArrayProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto FloatProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto DoubleProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto BoolProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto EnumProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto WeakObjectProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto NameProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto TextProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto StrProperty_from_lua(lua_State *lua_state, FromLuaParams) -> void
### auto Array_Type_Handler_Ptr() -> void
### auto Array_Type_Handler_WChar_T() -> void
