# RC::LuaType::UObjectBase

Source: `/home/jason/Projects/Advanced-SCUM-Modding/third_party/UE4SS/UE4SS/include/LuaType/LuaUObject.hpp`
Kind: class

## Members

### UObjectBase(DerivedType *object)
### auto derives_from_object() -> bool override
### UObjectBase()=delete
### ~UObjectBase()=default
### auto construct(const LuaMadeSimple::Lua &lua, DerivedType *unreal_object) -> const LuaMadeSimple::Lua::Table
### auto construct(const LuaMadeSimple::Lua &lua, LuaMadeSimple::Type::BaseObject &construct_to) -> const LuaMadeSimple::Lua::Table
### auto setup_member_functions(const LuaMadeSimple::Lua::Table &table) -> void
