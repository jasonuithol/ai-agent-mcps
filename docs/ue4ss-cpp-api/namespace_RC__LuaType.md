# RC::LuaType

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaType/LuaAActor.hpp`
Kind: namespace

## Members

### typedef LuaMadeSimple::Type::Operation Operation
### typedef ObjectBase< DerivedType, LuaMadeSimple::Type::RemoteObject, ObjectName > RemoteObjectBase
### typedef ObjectBase< DerivedType, LuaMadeSimple::Type::LocalObject, ObjectName > LocalObjectBase
### typedef ObjectBase< uint8_t, LuaMadeSimple::Type::RemoteObject, UE4SSBaseObjectName > UE4SSBaseObject
### typedef UObjectBase< Unreal::UObject, UObjectName > UObject
### auto call_ufunction_from_lua(const LuaMadeSimple::Lua &lua) -> int
### auto auto_construct_object(const LuaMadeSimple::Lua &, Unreal::UObject *) -> void
### auto construct_fname(const LuaMadeSimple::Lua &) -> void
### auto construct_uclass(const LuaMadeSimple::Lua &) -> void
### auto construct_xproperty(const LuaMadeSimple::Lua &, Unreal::FProperty *property) -> void
### auto convert_lua_table_to_struct(const LuaMadeSimple::Lua &lua, Unreal::UScriptStruct *script_struct, void *data, int table_index, Unreal::UObject *base=nullptr) -> void
### auto convert_struct_to_lua_table(const LuaMadeSimple::Lua &lua, Unreal::UScriptStruct *script_struct, void *data, bool create_new_table=true, Unreal::UObject *base=nullptr) -> void
### auto push_unhandledproperty(const PusherParams &) -> void
### auto push_objectproperty(const PusherParams &) -> void
### auto push_classproperty(const PusherParams &) -> void
### auto push_int8property(const PusherParams &) -> void
### auto push_int16property(const PusherParams &) -> void
### auto push_intproperty(const PusherParams &) -> void
### auto push_int64property(const PusherParams &) -> void
### auto push_byteproperty(const PusherParams &) -> void
### auto push_uint16property(const PusherParams &) -> void
### auto push_uint32property(const PusherParams &) -> void
### auto push_uint64property(const PusherParams &) -> void
### auto push_structproperty(const PusherParams &) -> void
### auto push_arrayproperty(const PusherParams &) -> void
### auto push_setproperty(const PusherParams &) -> void
### auto push_mapproperty(const PusherParams &) -> void
### auto push_floatproperty(const PusherParams &) -> void
### auto push_doubleproperty(const PusherParams &) -> void
### auto push_boolproperty(const PusherParams &) -> void
### auto push_enumproperty(const PusherParams &) -> void
### auto push_weakobjectproperty(const PusherParams &) -> void
### auto push_nameproperty(const PusherParams &) -> void
### auto push_textproperty(const PusherParams &) -> void
### auto push_strproperty(const PusherParams &) -> void
### auto push_utf8strproperty(const PusherParams &) -> void
### auto push_ansistrproperty(const PusherParams &) -> void
### auto push_softobjectproperty(const PusherParams &) -> void
### auto push_interfaceproperty(const PusherParams &) -> void
### auto push_delegateproperty(const PusherParams &) -> void
### auto push_multicastdelegateproperty(const PusherParams &) -> void
### auto push_multicastsparsedelegateproperty(const PusherParams &) -> void
### auto push_functionproperty(const FunctionPusherParams &) -> void
### auto handle_unreal_property_value(const Operation operation, const LuaMadeSimple::Lua &, Unreal::UObject *base, Unreal::FName property_name, Unreal::FField *field) -> void
### auto is_a_implementation(const LuaMadeSimple::Lua &lua) -> int
### auto add_to_global_unreal_objects_map(Unreal::UObject *object) -> void
### auto is_object_in_global_unreal_object_map(Unreal::UObject *object) -> bool
### auto push_integer(const PusherParams &params) -> void
### auto auto_construct_property(const LuaMadeSimple::Lua &, Unreal::FProperty *) -> void
