# RC::LuaType::ObjectBase

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaType/LuaUObject.hpp`
Kind: class

## Members

### ObjectBase(ObjectType *object)
### ObjectBase(ObjectType &&object)
### ObjectBase()=delete
### ~ObjectBase()=default
### auto derives_from_actor() -> bool
### auto derives_from_name() -> bool
### auto derives_from_string() -> bool
### auto derives_from_text() -> bool
### auto derives_from_weak_object_ptr() -> bool
### auto derives_from_mod() -> bool
### auto derives_from_array() -> bool
### auto derives_from_class() -> bool
### auto derives_from_enum() -> bool
### auto derives_from_function() -> bool
### auto derives_from_object() -> bool
### auto derives_from_script_struct() -> bool
### auto derives_from_world() -> bool
### auto derives_from_property() -> bool
### auto derives_from_property_class() -> bool
### auto derives_from_ufunction() -> bool
### auto construct(const LuaMadeSimple::Lua &lua, Unreal::UObject *unreal_object) -> const LuaMadeSimple::Lua::Table
### auto construct(const LuaMadeSimple::Lua &lua, LuaMadeSimple::Type::BaseObject &construct_to) -> const LuaMadeSimple::Lua::Table
### auto setup_member_functions(const LuaMadeSimple::Lua::Table &table) -> void
